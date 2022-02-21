# CrossBerry Web Server

# modules
import flask
import threading
import os
import oauth
import logging

# disable logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# variables
OAuth = oauth.OAuth

# class
class Folder:
	global_variables = {}

	def __init__(self, *options, **specific_options):
		self.global_variables = specific_options["global_variables"] if "global_variables" in specific_options else options[0] if len(options) > 0 else {}

	def fileread(self, filename:str, **inputs):
		if os.path.isfile(filename):
			f = open(filename, 'r')
			data = f.read()
			f.close()
			inputs.update(self.global_variables)
			for arg in (new_list := [x for x in inputs]):
				data = data.replace('{{' + arg + '}}', inputs[arg])
			return data
		else:
			return ""

# functions initialization
app_folder = Folder({
	"meta" : """
		<meta name="description" content="A Cross-Server Connector Bot! It connects one chat to other chats whether it be global chat or private chat! Now connect servers together!">
		<meta property="og:url" content="https://chat.berrybots.tk/">
		<meta property="og:type" content="website">
		<meta property="og:title" content="ChatBerry">
		<meta property="og:description" content="A Cross-Server Connector Bot! It connects one chat to other chats whether it be global chat or private chat! Now connect servers together!">
		<meta property="og:image" content="{{icon}}">
		<meta name="twitter:card" content="summary_large_image">
		<meta property="twitter:domain" content="chat.berrybots.tk">
		<meta property="twitter:url" content="https://chat.berrybots.tk/">
		<meta name="twitter:title" content="ChatBerry">
		<meta name="twitter:description" content="A Cross-Server Connector Bot! It connects one chat to other chats whether it be global chat or private chat! Now connect servers together!">
		<meta name="twitter:image" content="{{icon}}">
	""",
	"app_name" : "ChatBerry",
	"icon" : "https://github.com/Berry-Foundations/ChatBerry/blob/main/ChatBerry.png?raw=true",
	"icon_white" : "https://github.com/Berry-Foundations/ChatBerry/blob/main/ChatBerry%20White.png?raw=true"
})

# functions
file = app_folder.fileread

# app
app = flask.Flask("ChatBerry")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route('/')
def home():
	return file('web/index.html', discord_login=OAuth.discord_login_url)

@app.route('/stylesheet')
def stylesheet():
	return file("web/style.css")

@app.route('/javascript')
def javascript():
	default_bot_permissions = "275418132032"
	
	return file('web/script.js', default_bot_permissions=default_bot_permissions)

@app.route('/oauth/user')
def oauth_user():
	token_error = "true"
	
	user = {}
	user_data_keys = "[]"
	user_data_values = "[]"

	if "code" in flask.request.args:
		code = flask.request.args['code']

		access_token = OAuth.get_access_token(code)
		token_error = "false"
		
		if access_token is None:
			token_error = "true"
		else:
			user = OAuth.get_user_data(access_token)
			user_data_keys = str(list(user.keys()))
			user_data_values = str(list(user.values())).replace('True', 'true').replace('False', 'false').replace('None', 'null')

	return file('web/oauth/user/user.html', token_error=token_error, user_data_keys=user_data_keys, user_data_values=user_data_values)

@app.route('/oauth/login-failure')
def oauth_login_failure():
	return file('web/oauth/user/login/failure.html')

@app.route('/login-failure')
def login_failure():
	return file('web/oauth/user/login/failure.html')

@app.route('/oauth/welcome')
def welcome():
	return file('web/oauth/user/login/welcome.html')

@app.route('/logout')
def logout():
	return file('web/oauth/user/login/logout.html')

@app.route('/profile')
def profile():
	return file('web/account/profile.html')

@app.route('/my-servers')
def myservers():
	return file('web/account/my-servers.html')

@app.route('/oauth/bot')
def oauth_bot():	
	return file('web/oauth/bot/bot.html')

# run servers
def web_run(host:str, port:str):
	app.run(host=host, port=port)

def run(host, port, **kwargs):
	web_thread = threading.Thread(target=web_run, args=[kwargs["host"] if "host" in kwargs else host, kwargs["port"] if "port" in kwargs else port])
	web_thread.start()

