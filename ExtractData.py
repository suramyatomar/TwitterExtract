#!/usr/bin/env python3
"""
    ExtractData - Python code to Extract additional data from Twitter that is not exported via the Twitter Export
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
import tweepy
from configparser import ConfigParser


# read the API details from the config file.
def config(filename='api.conf', section='dev'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to dev
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


###
# Function to check if URL is actually down vs just locally down
###
DEBUG = 0
params = config()

consumer_key = params['consumer_key']
consumer_secret = params['consumer_secret']
access_token = params['access_token']
access_token_secret = params['access_token_secret']

auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

api = tweepy.API(auth)

# By Default we extract data for SuramyaTomar but it can be overridden by passing a command line parameter
if len(sys.argv) > 1:
    InputName = sys.argv[len(sys.argv) - 1]
else:
    InputName = "SuramyaTomar"

# get the UserID for the screen name provided
InputUserID = api.get_user(screen_name=InputName).id

# Export Followers

file = open(str(InputUserID) + "_followers", 'w')

for value in tweepy.Cursor(api.get_followers, user_id=InputUserID, count=200).items():
    entry = str(value.id) + "|" + value.screen_name + "|" + value.name + "\n"
    if DEBUG:
        print(api.wait_on_rate_limit)
    file.write(entry)

file.close()

# Export Following List
file = open(str(InputUserID) + "_following", 'w')

for value in tweepy.Cursor(api.get_friends, user_id=InputUserID, count=200).items():
    entry = str(value.id) + "|" + value.screen_name + "|" + value.name + "\n"
    if DEBUG:
        print(entry)
        print(api.wait_on_rate_limit)
    file.write(entry)
file.close()

# get All Lists owned/subscribed to by the User provided.

for value in api.get_lists(user_id=InputUserID):
    if value:
        file = open(str(InputUserID) + "_lst_" + str(value.id), 'w')
        file.write(value.name + '\n')
        for page in tweepy.Cursor(api.get_list_members, list_id=value.id, count=200).items():
            if page:
                entry = str(page.id) + "|" + page.screen_name + "|" + page.name + "\n"
                if DEBUG:
                    print(api.wait_on_rate_limit)
                file.write(entry)
        file.close()
