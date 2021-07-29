from config import api_key,api_secret
from vonage import Client, Sms

client = Client(key=api_key, secret=api_secret)
sms = Sms(client)

def send_message(body):
	responseData = sms.send_message(body)

	if responseData["messages"][0]["status"] == "0":
	    return "success"
	else:
	    return f"Alert failed with error: {responseData['messages'][0]['error-text']}"
