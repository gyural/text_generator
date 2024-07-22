import os
from dotenv import load_dotenv
import requests

load_dotenv(verbose=True)
remove_api_key = os.getenv('REMOVE_BG_API_KEY')

def remove_bg_img_url(img_path, output_path):
    """
    한 이미지의 배경을 제거합니다.
    :param img_path:
    :param output_path:
    :return:
    """
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img_path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': remove_api_key},
    )
    if response.status_code == requests.codes.ok:
        with open(output_path, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

def remove_bg_img_dir(dir_path, output_dir_path):
    """
    디렉토리 내의 모든 이미지 파일에서 배경을 제거합니다.

    :param dir_path: 원본 이미지 파일들이 있는 디렉토리 경로
    :param output_dir_path: 배경 제거된 이미지 파일들을 저장할 디렉토리 경로
    """
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    image_extensions = ('.png')

    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith(image_extensions):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir_path, file)

                print(f"Processing {input_path}...")
                try:
                    remove_bg_img_url(input_path, output_path)
                    print(f"Saved to {output_path}")
                except Exception as e:
                    print(f"Failed to process {input_path}: {e}")


if __name__ == '__main__':
    input_directory = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/resized_images'  # 원본 이미지 파일들이 있는 디렉토리 경로
    output_directory = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/bg-removed'  # 배경 제거된 이미지 파일들을 저장할 디렉토리 경로

    remove_bg_img_dir(input_directory, output_directory)