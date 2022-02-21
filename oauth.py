# Discord OAuth

# modules
import os
import requests

# OAuth
class OAuth:
	client_id = 894131041390977074
	client_secret = os.getenv('CLIENT_SECRET')
	redirect_uri = "https://cross.berrybots.tk/oauth/user"
	scope = "identify%20emails%20guilds"
	discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=894131041390977074&redirect_uri=https%3A%2F%2Fcross.berrybots.tk%2Foauth%2Fuser&response_type=code&scope=email%20guilds%20identify"
	discord_token_url = "https://discord.com/api/oauth2/token"
	discord_api_url = "https://discord.com/api"

	def __init__(self):
		pass

	@staticmethod
	def get_access_token(code):
		self = OAuth

		payload = {
			"client_id" : self.client_id,
			"client_secret" : self.client_secret,
			"grant_type" : "authorization_code",
			"code" : code,
			"redirect_uri" : self.redirect_uri,
			"scope" : self.scope
		}

		access_token = requests.post(url=self.discord_token_url, data=payload).json()

		if "access_token" not in access_token:
			access_token["access_token"] = None

		return access_token["access_token"]
	
	@staticmethod
	def get_user_data(access_token):
		self = OAuth
		
		url = self.discord_api_url + "/users/@me"
		headers = {
			"authorization" : "Bearer " + access_token
		}

		user_object = requests.get(url=url, headers=headers).json()
		return user_object


