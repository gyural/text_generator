import base64

def base64_to_img(base64_string, output_path):
    """
    Base64 문자열을 이미지 파일로 변환하여 저장합니다.

    :param base64_string: Base64 인코딩된 문자열 (data:image/png;base64,iVBORw0KGgo... 형태)
    :param output_path: 변환된 이미지 파일을 저장할 경로
    """
    # Base64 문자열이 'data:image/'로 시작하는지 확인
    if ',' in base64_string:
        header, base64_data = base64_string.split(',', 1)
    else:
        base64_data = base64_string

    # Base64 문자열을 디코딩하여 바이너리 데이터로 변환
    image_data = base64.b64decode(base64_data)

    # 디코딩된 데이터를 이미지 파일로 저장
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

if __name__ == '__main__':
    test_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/resized_images/test-1.png'
    output_test_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/resized_images/output_test.png'

    # 원본 이미지를 Base64 인코딩
    base64_string = img_to_base64(test_path)
    print("Base64 Encoded String:")
    print(base64_string[:100])  # 출력된 문자열의 앞부분만 표시

    # Base64 문자열을 다시 이미지 파일로 디코딩
    base64_to_img(base64_string, output_test_path)

    # 디코딩된 이미지를 다시 Base64 문자열로 인코딩
    new_base64_string = img_to_base64(output_test_path)

    # 원본 Base64 문자열과 새로운 Base64 문자열 비교
    if base64_string == new_base64_string:
        print("Test passed: The Base64 strings match.")
    else:
        print("Test failed: The Base64 strings do not match.")