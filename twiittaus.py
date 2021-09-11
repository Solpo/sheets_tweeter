import ast, tweepy

def twiittaa(api, teksti: str):
    api.update_status(teksti)

def alusta(avaintiedosto: str) -> 'tweepy.api.API':
    with open(avaintiedosto) as f:
        avaimet = ast.literal_eval(f.read())
    auth = tweepy.OAuthHandler(avaimet["API_key"], avaimet["API_secret"])
    auth.set_access_token(avaimet["access_token"], avaimet["access_secret"])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    return api
