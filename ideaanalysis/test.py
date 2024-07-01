import requests

url = "https://google-search72.p.rapidapi.com/search"

# Ask the user for the search query
query = input("Enter your search query: ")

querystring = {"q": query, "lr": "en-US", "num": "10"}

headers = {
    "x-rapidapi-key": "f2d923e2dbmsh928770be9f325adp1bcaa0jsnd1a38eeadd35",
    "x-rapidapi-host": "google-search72.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    try:
        data = response.json()
        # Check if 'items' key exists in the response
        if 'items' in data:
            results = data['items']
            # Iterate over each search result item
            for item in results:
                print(f"Title: {item.get('title', '')}")
                print(f"Link: {item.get('link', '')}")
                print(f"Snippet: {item.get('snippet', '')}\n")
        else:
            print("No search results found.")
    except ValueError:
        print("Response is not valid JSON.")
else:
    print(f"Failed to fetch search results. Status code: {response.status_code}")
