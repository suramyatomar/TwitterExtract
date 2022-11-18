## Introduction:

This is a simple script that was created to extract data from Twitter that the Official Twitter Export seems to miss. It uses Tweepy to export this data from Twitter, Specifically we export:

* Owned Lists (Including Followers and Members of the list) 
* Subscribed Lists with Followers and Members of the List
* List of all Followers (ScreenName, Fullname and ID)
* List of all Following (ScreenName, Funnname and ID)

I might extend it to also process the remaining data, but not doing that now since the Official Twitter Export seems to get all the remaining data. Once you download the official export, I suggest that you use https://github.com/timhutton/twitter-archive-parser to process it to make it more local. 

This script was created in a few hours because I needed it. It is not productionized (Doesn't have much error checking etc) but it works for me. Feel free to add additional checks if you want. 

## Installation

Requires tweepy package to be installed. Run the following command to install the package:

```pip3 install tweepy```

### Twitter Developer Account

You need to have a Twitter Developer Account in order to use the API. Follow these steps to register for the account:

- Visit https://developer.twitter.com/en/apply/user and Apply for a Developer Account
- Verify your email
- After verifying your email, you will be sent to a welcome screen. Name your app and click on Get keys.
- Make Sure you save a copy of the Key's somewhere secure because the system doesn't show them to you afterwords (at least not that I could find). You will have to regenerate the keys if you forget.
- Rename the api.conf_sample to api.conf and update it with the keys you downloaded and you are ready

## How to Use:

The script is configured to accept the screenname of the user you want to export as a command line parameter. To run issue the following command:

```python3 ExtractData.py

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

