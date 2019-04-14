import requests
from config import Config
def get_news_sources():
	url="https://newsapi.org/v2/sources"
	params={"apiKey":Config.APIKEY,"category":"entertainment",
	"language":"en"}
	res= requests.get(url,params=params)
	if res.status_code==200:
		data=res.json()
		return data["sources"]

	return False


def get_articles(source_id):
	url="https://newsapi.org/v2/top-headlines"
	params={"apiKey":Config.APIKEY,"sources":source_id,
	"language":"en"}
	res= requests.get(url,params=params)
	if res.status_code==200:
		data=res.json()
		return data["articles"]
	return False