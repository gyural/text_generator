import torch
from PIL import Image
import matplotlib.pyplot as plt




if __name__ == '__main__':
    # 모델 로드 (yolov5s: small version)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # 이미지 로드
    img = '/Users/imgyuseong/PycharmProjects/text_generator/dats/testImage.png'  # 이미지 경로를 지정하세요

    # 객체 탐지 수행
    results = model(img)

    # 결과 표시
    results.show()

    # 결과를 matplotlib를 사용하여 표시하려면:
    results.render()  # 탐지 결과를 이미지에 그립니다.
    img_with_boxes = results.imgs[0]  # 탐지 결과가 그려진 이미지

    # PIL 이미지를 matplotlib로 표시
    plt.imshow(Image.fromarray(img_with_boxes))
    plt.axis('off')  # 축 숨기기
    plt.show()