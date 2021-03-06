"""
This is made to be used within Amazon Lambda serverless architecture .
"""

import os
import logging
import urllib
import requests
import json

# Grab the Bot OAuth token from the environment.
BOT_TOKEN = os.environ["BOT_TOKEN"]
# Define the URL of the targeted Slack API resource.
# We'll send our replies there.
SLACK_URL = os.environ['WEBHOOK_URL']


# We will specify a request URL in slack and slack with try to verify the url
# the code below checks to see if slack is verifying the url with a challenge
# if so it will echo the challenge
def receive(event, context):
    data = json.loads(event['body'])
    print("Got data: {}".format(data))
    return_body = "ok"

    if data["type"] == "url_verification":
        print("Received challenge")
        return_body = data["challenge"]

    return {
        "statusCode": 200,
        "body": return_body
    }

def lambda_handler(data, context):
    """Handle an incoming HTTP request from a Slack chat-bot.
    """
    # Grab the Slack event data.
    slack_event = data['event']
    
    # We need to discriminate between events generated by 
    # the users, which we want to process and handle, 
    # and those generated by the bot.
    if "bot_id" in slack_event:
        logging.warn("Ignore bot event")
    else:
        # Get the text of the message the user sent to the bot,
        # and reverse it.
        text = slack_event["text"]
        reversed_text = text[::-1]
        
        # Get the ID of the channel where the message was posted.
        channel_id = slack_event["channel"]
        

        #)
        
        payload = {'text':reversed_text} 
        headers = {'Content-type': 'application/json', 'User-Agent':'curl/7.64.1'} 


        # Fire off the request!



        r = requests.post(SLACK_URL, data=json.dumps(payload), headers=headers)
        print(r.text)
       # Fire off the request!


    # be nice and return a 200
    return "200 OK"
