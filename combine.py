from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def add_img2img(base_image, overlay_image):
    """
    기본 이미지 위에 다른 이미지를 중앙에 겹쳐 배치합니다.

    :param base_image: 기본 이미지 경로 또는 PIL Image 객체.
    :param overlay_image: 겹쳐질 이미지 경로 또는 PIL Image 객체.
    :return: 결합된 PIL Image 객체.
    """
    # 기본 이미지 로드
    if isinstance(base_image, str):
        base = Image.open(base_image).convert("RGBA")
    else:
        base = base_image.convert("RGBA")

    # 겹쳐질 이미지 로드
    if isinstance(overlay_image, str):
        overlay = Image.open(overlay_image).convert("RGBA")
    else:
        overlay = overlay_image.convert("RGBA")

    # 새로운 이미지 생성
    combined = Image.new('RGBA', base.size, (255, 255, 255, 0))

    # 기본 이미지를 새로운 이미지에 복사
    combined.paste(base, (0, 0))

    # 겹쳐질 이미지를 중앙에 복사
    combined.paste(overlay, (0, 0), overlay)

    return combined
# @param image{object image}
def show_image(image):
    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def show_boxes(image_path, text_boxes):
    if isinstance(image_path, str):
        image = Image.open(image_path).convert("RGBA")
    else:
        image = image_path.convert("RGBA")
    draw = ImageDraw.Draw(image)
    for box, _ in text_boxes:
        draw.rectangle(box, outline="red", width=2)
    return image

if __name__ == '__main__':

    base_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/resized_image.png'
    overlay_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/temp_image.png'
    base_img = Image.open(base_path).convert("RGBA")
    overlay_img = Image.open(overlay_path).convert("RGBA")

    combined = add_img2img(base_img, overlay_img)
    css_textbox = ([(50, 50), (400, 400)], "This is a test text!!")
    boxed_combined = show_boxes(combined, text_boxes=[css_textbox])

    # show_image(combined)
    show_image(boxed_combined)
