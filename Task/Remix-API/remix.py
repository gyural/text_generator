import requests
import json
import os
from Task.upload_image.getDatas.get_ref_img import get_reference_img
from Task.upload_image.getDatas.get_product_img import get_img_path
from dotenv import load_dotenv

# 정상 호출시 output 이미지 출력
def get_remix_img(product_url, ref_url):

    # load ENV DATA
    load_dotenv(verbose=True)

    remix_api_key = os.getenv('PHOTIO_SECRET_KEY')

    data = {
    "prompt": "product photograph",
    "product_image": f"{product_url}",
    "ref_image": f"{ref_url}",
    # "negative_prompt" : "worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch"
    }

    body_data = json.dumps(data)
    # Set the necessary headers
    headers = {
    'X-Photio-Key': f'{remix_api_key}',
    'Content-Type': 'application/json'

    }
    response = requests.post('https://api.photio.io/v1/inference/remix', headers=headers, data=body_data)
    res_json = response.json()
    if response.status_code == 200:

         return res_json.body
    else:
        print("error-detect")
        print(res_json)
        return False

if __name__ == '__main__':
    # ref_list = get_reference_img()
    # product_list = get_img_path()

    fileName = 'remix_img.txt'
    # with open(fileName, 'a') as file:  # Append mode to write multiple lines
    #     for product_url in product_list:
    #         for ref_url in ref_list:
    #             remix_img = get_remix_img(product_url, ref_url)
    #
    #             if remix_img:
    #                 file.write(f'{remix_img}' + '\n')

    sample_product = "https://res.cloudinary.com/dhabktrg9/image/upload/h_1024,w_1024/quickstart_butterfly"
    sample_ref = ["https://imagedelivery.net/zea4eJK186SeWjCFHvF-jQ/311f05e6-7b1f-4c05-c7f0-12f77cb48200/1k"]
    with open(fileName, 'a') as file:
        for ref_url in sample_ref:
            remix_img = get_remix_img(sample_product, ref_url)
            if remix_img:
                file.write(remix_img + '\n')

