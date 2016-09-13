#Log Tweets
Logs tweets of specified user(s) to a json file and stdout.

*Required files:*

- `id.txt` list of user ids to follow
- `creds.txt` credentials for twitter app, line by line in the following order: 0=access_token,1=access_token_secret,2=consumer_key,3=consumer_secret

###Requirements

- requests
- tweepy