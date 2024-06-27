from combine import add_img2img, show_image
from font.font_gene import get_final_text_img
from Rcnn import detect_objects
from get_area import get_max_non_overlapping_box
from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    img_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/resized_image.png'  # 이미지 경로를 지정하세요
    _, boxes, _, _ = detect_objects(img_path)
    print(boxes)
    max_non_overlapping_boxes = get_max_non_overlapping_box(boxes)
    print(max_non_overlapping_boxes)
    result_img = Image.open(img_path).convert("RGBA")
    for box in max_non_overlapping_boxes:
        txt_img = get_final_text_img(box)
        result_img = add_img2img(result_img, get_final_text_img(box))

    show_image(result_img)