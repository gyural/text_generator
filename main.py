from combine import add_img2img
from font.font_gene import get_final_text_img
from Rcnn import detect_objects
from get_area import get_max_non_overlapping_box


if __name__ == '__main__':
    img_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/resized_image.png'  # 이미지 경로를 지정하세요
    _, boxes, _, _ = detect_objects(img_path)
    max_non_overlapping_boxes = get_max_non_overlapping_box(boxes)
    print(max_non_overlapping_boxes)