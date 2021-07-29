from app import app, bcrypt, db
from flask import render_template, request, flash, redirect, url_for
from app.models import User
from app.api_helper import *
from app.functions import *

@app.route('/', methods=['GET'])
def index():
	return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == "POST":
		username = request.form.get('username')
		email = request.form.get('email')
		phone = request.form.get('phone')

		# validation
		if not is_valid_email(email):
			flash("Email is invalid")
			return redirect(url_for('register'))
		if not is_valid_phone(phone):
			flash("Phone number is invalid")
			return redirect(url_for('register'))
		if not is_valid_username(username):
			flash("Invalid characters in username")
			return redirect(url_for('register'))

		user_with_email = User.query.filter_by(email=email).first()
		user_with_phone = User.query.filter_by(phone=phone).first()

		if user_with_email or user_with_phone:
			flash("Request already exists!")
			return redirect(url_for('register'))

		user = User(username=username, email=email, phone=phone)
		db.session.add(user)
		db.session.commit()

		flash("Request was successfull!")
		return redirect(url_for('index'))

	return render_template('register.html')




