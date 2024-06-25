from html2image import Html2Image
from PIL import Image
import os

def render_text_to_image(html_template_path, text, font_size, image_width, image_height, bbox):
    # Read the HTML template
    with open(html_template_path, 'r', encoding='utf-8') as file:
        html_template = file.read()

    # Replace placeholders with actual values
    html_content = html_template.replace('{{ text }}', text)
    html_content = html_content.replace('{{ font_size }}', str(font_size//2))
    html_content = html_content.replace('{{ image_width }}', str(image_width//2))
    html_content = html_content.replace('{{ image_height }}', str(image_height//2))
    html_content = html_content.replace('{{ bbox_x0 }}', str(bbox[0]//2))
    html_content = html_content.replace('{{ bbox_y0 }}', str(bbox[1]//2))
    html_content = html_content.replace('{{ bbox_width }}', str((bbox[2] - bbox[0])//2))
    html_content = html_content.replace('{{ bbox_height }}', str((bbox[3] - bbox[1])//2))

    # Create an Html2Image instance
    hti = Html2Image()

    # Generate a temporary output image path
    temp_image_path = 'temp_image.png'

    # Convert HTML to image
    hti.screenshot(html_str=html_content, save_as=temp_image_path, size=(image_width//2, image_height//2)
                   )

    # Load the generated image into a PIL Image object
    image = Image.open(temp_image_path)

    # Optionally, delete the temporary image file
    # os.remove(temp_image_path)

    return image

if __name__ == '__main__':
    html_template_path = 'font.html'
    text = 'This is a test text!'
    font_size = 30
    image_width = 800
    image_height = 800
    bbox = [50, 50, 750, 750]  # x0, y0, x1, y1

    image = render_text_to_image(html_template_path, text, font_size, image_width, image_height, bbox)
    image.show()  # Display the image