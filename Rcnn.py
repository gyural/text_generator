import torch
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image
import matplotlib.pyplot as plt
from get_area import get_max_non_overlapping_box, plot_avariable_area

# COCO 데이터셋 클래스 이름들
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A',
    'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
    'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut',
    'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table', 'N/A',
    'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book', 'clock',
    'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

def detect_objects(img_path, threshold=0.5):
    # 모델 로드
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    # 이미지 로드 및 전처리
    img = Image.open(img_path).convert("RGB")
    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),  # 이미지를 텐서로 변환
        torchvision.transforms.Resize((800, 800))  # 이미지 크기를 조정
    ])
    img_tensor = transform(img).unsqueeze(0)  # 배치 차원 추가

    # 예측 수행
    with torch.no_grad():
        predictions = model(img_tensor)

    # 예측 결과 처리
    pred_classes = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in predictions[0]['labels'].cpu().numpy()]
    pred_boxes = [[(i[0], i[1]), (i[2], i[3])] for i in predictions[0]['boxes'].cpu().numpy()]
    pred_scores = predictions[0]['scores'].cpu().numpy()

    # 신뢰도가 threshold 이상인 객체만 필터링
    filtered_boxes = []
    filtered_classes = []
    filtered_scores = []

    for box, score, cls in zip(pred_boxes, pred_scores, pred_classes):
        if score > threshold:
            filtered_boxes.append(box)
            filtered_classes.append(cls)
            filtered_scores.append(score)

    return img, filtered_boxes, filtered_classes, filtered_scores
def plot_results(img, boxes, classes, scores):
    # 바운딩 박스와 클래스를 이미지에 표시
    plt.figure(figsize=(8, 8))
    plt.imshow(img)
    ax = plt.gca()

    for box, cls, score in zip(boxes, classes, scores):
        (x0, y0), (x1, y1) = box
        ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, edgecolor='red', linewidth=2))
        ax.text(x0, y0, f'{cls}: {score:.2f}', bbox=dict(facecolor='yellow', alpha=0.5), fontsize=10, color='black')

    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    img_path = '/Users/imgyuseong/PycharmProjects/text_generator/datas/resized_image.png'  # 이미지 경로를 지정하세요
    img, boxes, classes, scores = detect_objects(img_path)

    print("Detected objects:")
    for cls, box, score in zip(classes, boxes, scores):
        print(f"Class: {cls}, Box: {box}, Score: {score:.2f}")
    plot_results(img, boxes, classes, scores)
    area = get_max_non_overlapping_box(boxes)
    print(area)

    plot_avariable_area(area)