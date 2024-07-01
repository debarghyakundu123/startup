import requests

url = "https://transloc-api-1-2.p.rapidapi.com/agencies.json"

querystring = {"callback":"call","geo_area":"35.80176,-78.64347|35.78061,-78.68218","agencies":"12"}

headers = {
	"x-rapidapi-key": "f2d923e2dbmsh928770be9f325adp1bcaa0jsnd1a38eeadd35",
	"x-rapidapi-host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())