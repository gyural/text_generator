from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def find_optimal_font_size(draw, text, font_path, box_width, box_height):
    # 초기 폰트 크기 설정
    font_size = 1
    test_font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textbbox((0, 0), text, font=test_font)[2:]

    # 텍스트가 박스 안으로 들어갈 때까지 폰트 크기를 키워가며 테스트
    while text_width < box_width and text_height < box_height:
        font_size += 1
        test_font = ImageFont.truetype(font_path, font_size)
        text_width, text_height = draw.textbbox((0, 0), text, font=test_font)[2:]

    # 텍스트가 박스를 넘어가는 마지막 크기의 폰트를 반환
    return font_size - 1

def add_text_to_image(image_path, text_boxes, font_size, text_color, font_path=None):
    # 이미지 열기
    image = Image.open(image_path).convert("RGBA")
    txt = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)

    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
        print("기본 폰트를 불러올 수 없습니다. 고정 크기 기본 폰트를 사용합니다.")

    for box, text in text_boxes:
        (x0, y0), (x1, y1) = box
        # 박스 크기 계산
        box_width = x1 - x0
        box_height = y1 - y0

        # 최적의 폰트 크기 찾기
        optimal_font_size = find_optimal_font_size(draw, text, font_path, box_width, box_height)
        font = ImageFont.truetype(font_path, optimal_font_size)

        # 텍스트 줄바꿈 처리
        lines = []
        words = text.split()
        current_line = words[0]

        for word in words[1:]:
            test_line = current_line + " " + word
            width, _ = draw.textbbox((0, 0), test_line, font=font)[2:]
            if width > box_width:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line

        if current_line:
            lines.append(current_line)

        # 텍스트 삽입 위치 계산 (중앙 정렬)
        total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] for line in lines)
        text_y = y0 + (box_height - total_text_height) / 2

        for line in lines:
            text_width, text_height = draw.textbbox((0, 0), line, font=font)[2:]
            text_x = x0 + (box_width - text_width) / 2
            draw.text((text_x, text_y), line, font=font, fill=text_color)
            text_y += text_height

    combined = Image.alpha_composite(image, txt)
    return combined

def show_image(image):
    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    # 설정 값
    image_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/resized_image.png'
    font_size = 20
    text_color = (255, 0, 0, 255)  # 텍스트 색상 (RGBA)
    font_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/DejaVuSans.ttf'

    # 텍스트와 박스 좌표 입력
    text_boxes = [
        ([(50, 50), (300, 100)], 'This is a long text that may overflow the box and needs to be wrapped.'),
        ([(100, 200), (250, 250)], 'Short text.'),
        ([(50, 300), (350, 350)], 'Another very long text that needs to be wrapped into multiple lines.')
    ]

    # 함수 호출
    image_with_text = add_text_to_image(image_path, text_boxes, font_size, text_color, font_path)
    show_image(image_with_text)