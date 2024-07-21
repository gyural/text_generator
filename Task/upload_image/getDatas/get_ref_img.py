import random

base_dir = '/Task/Remix-API/image_sources.txt'


def get_reference_img(num=5):
    # 텍스트 파일을 열어 각 줄을 리스트로 읽음
    with open(base_dir, 'r') as file:
        lines = file.readlines()

    # 각 줄의 공백을 제거한 후 리스트로 만듦
    img_urls = [line.strip() for line in lines]

    # 리스트에서 중복 없이 랜덤하게 num개의 URL 선택
    random_img_urls = random.sample(img_urls, min(num, len(img_urls)))

    return random_img_urls


if __name__ == '__main__':
    random_img_urls = get_reference_img()
    # print(random_img_urls)