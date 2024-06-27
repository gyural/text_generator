import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
def get_max_non_overlapping_box(existing_boxes, image_size=(800, 800)):
    # 이미지 크기
    img_width, img_height = image_size

    # 겹치지 않는 최대 바운딩 박스를 저장할 리스트
    max_non_overlapping_boxes = []

    # 방향별로 최대 크기의 바운딩 박스를 찾기
    for direction in ['top', 'bottom']:
        if direction == 'left':
            max_width, max_height = float('inf'), img_height
            for (x0, y0), (x1, y1) in existing_boxes:
                if x0 < max_width:
                    max_width = x0
            max_width_box = [(0, 0), (max_width, img_height)]
            max_non_overlapping_boxes.append(max_width_box)

        elif direction == 'right':
            max_width, max_height = float('inf'), img_height
            for (x0, y0), (x1, y1) in existing_boxes:
                if img_width - x1 < max_width:
                    max_width = img_width - x1
            max_width_box = [(img_width - max_width, 0), (img_width, img_height)]
            max_non_overlapping_boxes.append(max_width_box)

        elif direction == 'top':
            max_width, max_height = img_width, float('inf')
            for (x0, y0), (x1, y1) in existing_boxes:
                if y0 < max_height:
                    max_height = y0
            max_height_box = [(0, 0), (img_width, max_height)]
            max_non_overlapping_boxes.append(max_height_box)

        elif direction == 'bottom':
            max_width, max_height = img_width, float('inf')
            for (x0, y0), (x1, y1) in existing_boxes:
                if img_height - y1 < max_height:
                    max_height = img_height - y1
            max_height_box = [(0, img_height - max_height), (img_width, img_height)]
            max_non_overlapping_boxes.append(max_height_box)

    return max_non_overlapping_boxes


def plot_avariable_area(bounding_boxes, img_size=(800, 800)):
    # 바운딩 박스를 위한 반투명 색상 정의
    colors = [(255, 0, 0, 128), (0, 0, 255, 128), (0, 255, 0, 128),
              (255, 255, 0, 128), (0, 255, 255, 128), (255, 0, 255, 128)]

    image = Image.new('RGB', img_size, color=(255, 255, 255))
    overlay = Image.new('RGBA', img_size, color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 각 바운딩 박스를 이미지에 그리기
    for i, box in enumerate(bounding_boxes):
        draw.rectangle(box, fill=colors[i], outline=colors[i][:3] + (255,), width=3)

    # 이미지를 합성하여 반투명한 색상 적용
    image = Image.alpha_composite(image.convert('RGBA'), overlay)

    # 이미지 출력
    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis('off')  # 축 숨기기

    # plt.show() 대신 savefig를 사용하여 공백 없이 이미지 저장
    plt.savefig('/Users/imgyuseong/PycharmProjects/text_generator/datas/text_boxes.png', bbox_inches='tight', pad_inches=0)
