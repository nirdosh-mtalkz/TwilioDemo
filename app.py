import os
from twilio.rest import Client
from dotenv import dotenv_values

config = dotenv_values(".env")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


# message = client.messages.create(
#   to="+918081701067",
#   from_="+16086556107",
#   body = "Hello Testing from trial phone number......"
# )
#print(message.sid)


# call = client.calls.create(
#   to="+918081701067",
#   from_="+16086556107",
#   url="https://demo.twilio.com/welcome/voice/voice.xml"
# )
#print(call.sid)


print("Call Records")
for call in client.calls.list():
    print("%s %s"%(call.to,call.from_))

print("Messages Records")
for sms in client.messages.list():
    print("%s %s"%(sms.to,sms.from_))