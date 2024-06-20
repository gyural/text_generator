from PIL import Image
def resize_image(img_path, target_size=(800, 800)):
    # 이미지 열기
    img = Image.open(img_path)

    # 이미지 resizing
    resized_img = img.resize(target_size, )  # ANTIALIAS 옵션을 사용하여 이미지를 부드럽게 resizing

    return resized_img


# 테스트를 위한 예제
if __name__ == '__main__':
    img_path = '/datas/testImage.png'  # 이미지 경로를 지정하세요
    resized_img = resize_image(img_path)

    # resizing된 이미지 저장 예제
    resized_img.save('/Users/imgyuseong/PycharmProjects/text_generator/resized_image.png')

    # 저장된 이미지를 확인하기 위해 출력
    resized_img.show()