from app.models import User
from app import db
from app.api_helper import send_message
import re

def is_valid_phone(phone):
	pattern = "^\+(?:[0-9] ?){6,14}[0-9]$"
	return re.match(pattern, phone)

def is_valid_email(email):
	pattern = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
	return re.match(pattern, email)

def is_valid_username(username):
	pattern = "^[a-zA-Z\s_-]{4,16}$"
	return re.match(pattern, username)

def get_users_phones():
	users = User.query.all()
	phones = db.session.query(User.phone).all()
	return phones

def send_alert(acc):
	phones=get_users_phones()
	for phone in phones:
		print(phone)
		text = "disaster alert - \nDisaster is approching with probability of {}% \nPlease take required steps to be safe \nBy:\nAuthorities\n\n".format(acc)

		body = {
			"from": "Vonage",
			"to": "{}".format(phone[0]),
			"text": text,
		}

		res = send_message(body)
		if res != "success":
			return res
	return "Alert sent successfully"
