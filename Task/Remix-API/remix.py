import requests
import json

data = {
"prompt": "product photograph of perfume, on the beach, perfume next to seashell",
"product_image": "https://imagedelivery.net/zea4eJK186SeWjCFHvF-jQ/97f81a05-2d9c-4ea3-9039-2b18672d9c00/1k",
"ref_image": "https://imagedelivery.net/zea4eJK186SeWjCFHvF-jQ/311f05e6-7b1f-4c05-c7f0-12f77cb48200/1k"

}

body_data = json.dumps(data)

# Set the necessary headers
headers = {
'X-Photio-Key': '{X-Photio-Key}',
'Content-Type': 'application/json'

}

response = requests.post('https://api.photio.io/v1/inference/remix', headers=headers, data=body_data)