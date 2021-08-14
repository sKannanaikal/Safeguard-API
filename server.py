from flask import Flask, json, render_template
import random

SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*']


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/<int:length>', methods=["GET", "POST"])
def get_password(length):
	password = generate(length)
	json_data = {
		"Password": password
	}
	response = json.jsonify(json_data)
	response.headers.add("Access-Control-Allow-Origin", "*")
	return response

def generate(pass_length):
	if pass_length < 10:
		pass_length = 10
	elif pass_length > 30:
		pass_length = 30

	password = ''
	lower_count = random.randint(1, pass_length - 2)
	pass_length -= lower_count
	upper_count = random.randint(1, pass_length - 1)
	special_count = pass_length

	for _ in range(lower_count):
		password += chr(random.randint(65, 90))

	for _ in range(upper_count):
		password += chr(random.randint(97, 122))

	for _ in range(special_count):
		password += SPECIAL_CHARACTERS[random.randint(1, len(SPECIAL_CHARACTERS) - 1)]

	password_shuffle_container = list(password)
	for _ in range(10):
		random.shuffle(password_shuffle_container)

	shuffled_password = ''.join(password_shuffle_container)

	return shuffled_password

app.run(port=12000)