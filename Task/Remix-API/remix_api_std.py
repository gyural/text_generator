import requests
import json
import os
from dotenv import load_dotenv
from Task.base64_invert.base64_to_img import img_to_base64, base64_to_img, img_to_base64_dir
from getDatas.get_ref_img import get_reference_img

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
         return res_json["body"]
    else:
        print("error-detect")
        print(res_json)
        return False
def get_remix_dir(image_dir, output_dir):
    product_list_base64 = img_to_base64_dir(image_dir)
    sample_ref = get_reference_img()
    for idx1, ref_url in enumerate(sample_ref):
        for idx2, product_uri in enumerate(product_list_base64):
            remix_img = get_remix_img(product_uri, ref_url)
            if remix_img:
                base64_to_img(remix_img, f'{output_dir}/{idx1}-{idx2}.png')

if __name__ == '__main__':
    product_dir = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/resized_images'
    output_dir = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/remix_output'
    get_remix_dir(product_dir, output_dir)

