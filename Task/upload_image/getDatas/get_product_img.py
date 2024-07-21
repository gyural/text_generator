import os

base_url = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample'

sample_apple_dir = base_url + '/sample-apple'
sample_sensualing_dir = base_url + '/sample-sensualing'


def get_img_path(directory = sample_apple_dir):
    # 지원하는 이미지 파일 확장자
    image_extensions = ('.png')

    # 디렉토리 내의 모든 파일 경로를 리스트로 반환
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_paths.append(os.path.join(root, file))

    return image_paths

if __name__ == '__main__':
    image_paths = get_img_path(sample_apple_dir)
    # print(image_paths)

