import base64
import os

def base64_to_img(base64_string, output_path):
    """
    Base64 문자열을 이미지 파일로 변환하여 저장합니다.

    :param base64_string: Base64 인코딩된 문자열 (data:image/png;base64,iVBORw0KGgo... 형태)
    :param output_path: 변환된 이미지 파일을 저장할 경로
    """
    if ',' in base64_string:
        header, base64_data = base64_string.split(',', 1)
    else:
        base64_data = base64_string

    image_data = base64.b64decode(base64_data)

    with open(output_path, 'wb') as file:
        file.write(image_data)

def img_to_base64(img_path, with_header=True):
    """
    이미지 파일을 Base64 인코딩된 문자열로 변환합니다.

    :param img_path: 이미지 파일의 경로
    :return: Base64 인코딩된 문자열
    """
    # 이미지 파일을 바이너리 모드로 열기
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # 'data:image/png;base64,' 형태로 반환 (확장자에 따라 'image/jpeg', 'image/gif' 등으로 변경 가능)
    if(with_header):
        return f"data:image/png;base64,{encoded_string}"
    else:
        return encoded_string
def img_to_base64_dir(dir_path, with_header=True):
    """
    디렉토리 내의 모든 이미지 파일을 Base64 인코딩된 문자열로 변환합니다.

    :param dir_path: 이미지 파일들이 있는 디렉토리 경로
    :param with_header: 헤더를 포함할지 여부
    :return: Base64 인코딩된 문자열 리스트
    """
    base64_strings = []
    image_extensions = ('.png')

    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith(image_extensions):
                img_path = os.path.join(root, file)
                print(f"Encoding {img_path}...")
                try:
                    base64_str = img_to_base64(img_path, with_header)
                    base64_strings.append(base64_str)
                except Exception as e:
                    print(f"Failed to encode {img_path}: {e}")

    return base64_strings


if __name__ == '__main__':
    img_dir = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/resized_images'
    base64_list = img_to_base64_dir(img_dir)
    print(len(base64_list))
