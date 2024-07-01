import http.server
import socketserver
import urllib.parse
import json
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import base64

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/search'):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query).get('query', [''])[0]
            url = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            images_data = []

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                images = soup.find_all('img')[1:7]  # Only fetch the first 6 images

                for img in images:
                    img_url = img['src']
                    img_response = requests.get(img_url)
                    img_data = img_response.content
                    image = Image.open(BytesIO(img_data))
                    image.thumbnail((500, 500))
                    buffered = BytesIO()
                    image.save(buffered, format="JPEG")
                    img_str = base64.b64encode(buffered.getvalue()).decode()
                    images_data.append(f"data:image/jpeg;base64,{img_str}")

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(images_data).encode())

            else:
                self.send_error(500, 'Failed to retrieve images')

        else:
            super().do_GET()

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\nServer stopped.")
