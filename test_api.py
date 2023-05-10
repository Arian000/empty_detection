import requests
import json
import base64

url = "http://localhost:8000/detect/"

with open("data/photo_09.jpg", "rb") as f:
    img_data = f.read()

payload = {"image": str(base64.b64encode(img_data), "utf-8")}
headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, data=json.dumps(payload))

result = response.json()
print(result)