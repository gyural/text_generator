from PIL import Image
import os
def resize_image(img_path, target_size=(1024, 1024)):
    # 이미지 열기
    img = Image.open(img_path)

    # 이미지 resizing
    resized_img = img.resize(target_size, )  # ANTIALIAS 옵션을 사용하여 이미지를 부드럽게 resizing

    return resized_img


# 테스트를 위한 예제
def resize_images_in_directory(directory_path, output_directory, target_size=(1024, 1024)):
    """디렉토리에 있는 모든 이미지를 리사이즈하고 출력 디렉토리에 저장합니다."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    count = 1
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')) and filename != '.DS_Store':
            image_path = os.path.join(directory_path, filename)
            resized_img = resize_image(image_path, target_size)
            output_filename = f"test-{count}{os.path.splitext(filename)[1]}"  # 새로운 파일명 생성
            output_path = os.path.join(output_directory, output_filename)
            resized_img.save(output_path)
            print(f"Saved resized image to {output_path}")
            count += 1

if __name__ == '__main__':
    dir_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/bg-removed'  # 이미지 경로를 지정하세요
    output_dir = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/sample-apple/resized_images'  # 리사이즈된 이미지를 저장할 경로

    resize_images_in_directory(dir_path, output_dir)

    # 저장된 이미지를 확인하기 위해 첫 번째 이미지를 출력
    first_image = os.path.join(output_dir, os.listdir(output_dir)[0])
    Image.open(first_image).show()