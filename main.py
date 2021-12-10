import requests
from twilio.rest import Client
import os
from data import Data

# This is imported from Data Class
results = Data("NIO", 3)
response = results.response

# This function is responsible for sending a text message using Twilion API
def send_message(body_text):
    account_sid =os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                  body=body_text,
                                  from_='447492879246',
                                  to='447462555605'
                              )
# This function will compare the price in the last 2 days and send a text notification accordingly.
def check_for_updates():
    open_balance_past_day = response[1]['open']
    open_balance_current_day = response[0]['open']
    # Defining the Increase/Decrease arrow sign.
    if open_balance_past_day > open_balance_current_day:
        sign = "🔻"
    else:
        sign = "🔺"
    # Defining the message body for when I will send the text message.
    message_body = f"{sign}Headlines: 🗞️ {response[0]['symbol']} Alert!\n💥Here's the News:" \
                   f"\nPrice at open for the past day is: {open_balance_past_day}" \
                   f"\nPrice at open for current day: {open_balance_current_day}"
    # Compare the past day's vs current day's price at open and send notification via Twilio API
    if open_balance_past_day + (open_balance_past_day * 0.05) >= open_balance_current_day >= open_balance_past_day + (open_balance_past_day * 0.05):
        send_message(message_body)
    else:
        list_of_results = []
        for stock in response:
            list_of_results.append(
                f"{stock['symbol']} oppened with {stock['open']} on {stock['date']}.High: {stock['high']} and Low: {stock['low']}")
        for news in list_of_results:
            send_message(f"📰News Alert\n {news}")


check_for_updates()


