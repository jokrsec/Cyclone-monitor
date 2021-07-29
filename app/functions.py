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

def send_alert(phones, intensity):
	for phone in phones:
		phone = phone.strip().replace(' ', '')

		text = "Cyclone alert - \
		\nCyclone is approching your area\nIntensity is {}% \
		\nPlease take required steps to be safe \
		\nBy:\nAuthorities\n\n".format(intensity)

		body = {
	        "from": "Vonage",
	        "to": "{}".format(phone),
	        "text": text,
		}

		res = api_helper.send_message(body)
		if res != "success":
			return res
	return "Alert sent successfully"