from combine import add_img2img, show_image
from font.font_gene import get_final_text_img
from Rcnn import detect_objects
from get_area import get_max_non_overlapping_box
from PIL import Image
import os

def get_text_combined_image(img):
    _, boxes, _, _ = detect_objects(img)

    max_non_overlapping_boxes = get_max_non_overlapping_box(boxes)
    result_img = Image.open(img).convert("RGBA")
    for box in max_non_overlapping_boxes:
        txt_img = get_final_text_img(box)
        result_img = add_img2img(result_img, txt_img)

    return result_img

def get_ad_data():
    base_path = '/Users/imgyuseong/PycharmProjects/text_generator/resized_images/'
    return [base_path + filename for filename in os.listdir(base_path) if filename.lower().endswith('.jpg')]

if __name__ == '__main__':

    # Test 1 Image
    # img_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/resized_image.png'  # 이미지 경로를 지정하세요
    # result_IMG = get_text_combined_image(img_path)
    # show_image(result_IMG)

    # TEST Many Image
    print(get_ad_data())
    for idx, data in enumerate(get_ad_data()):
        result_img = get_text_combined_image(data)
        output_filename = f"result-{idx}.jpg"  # 새로운 파일명 생성
        output_path = os.path.join('/Users/imgyuseong/PycharmProjects/text_generator/result_images/', output_filename)
        result_img = result_img.convert('RGB')
        result_img.save(output_path)
        show_image(result_img)