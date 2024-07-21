import requests
import json
import os
from dotenv import load_dotenv
from Task.upload_image.getDatas.get_product_img import get_img_path
from base64_invert.base64_to_img import img_to_base64

# sample_product = "https://imagedelivery.net/zea4eJK186SeWjCFHvF-jQ/97f81a05-2d9c-4ea3-9039-2b18672d9c00/1k"
sample_product_upload = "https://res.cloudinary.com/dhabktrg9/image/upload/h_1024,w_1024/quickstart_butterfly"

my_product = get_img_path()
my_product_base64 = [img_to_base64(product) for product in my_product]

new_base64_string = img_to_base64(my_product[0], with_header=True)
print(new_base64_string[:50])



if __name__ == '__main__':
    load_dotenv(verbose=True)
    remix_api_key = os.getenv('PHOTIO_SECRET_KEY')

    data = {
        "prompt": "product photograph of perfume, on the beach, perfume next to seashell",
        "product_image": sample_product_upload,
        "ref_image": "https://imagedelivery.net/zea4eJK186SeWjCFHvF-jQ/311f05e6-7b1f-4c05-c7f0-12f77cb48200/1k"

    }

    body_data = json.dumps(data)

    # Set the necessary headers
    headers = {
        'X-Photio-Key': remix_api_key,
        'Content-Type': 'application/json'

    }

    response = requests.post('https://api.photio.io/v1/inference/remix', headers=headers, data=body_data)
    print(response)
    print(response.json())
