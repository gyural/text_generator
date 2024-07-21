from bs4 import BeautifulSoup
from html_data import html_data

if __name__ == '__main__':
    # HTML 데이터
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html_data, 'html.parser')

    # img 태그를 찾고 src 속성을 추출
    img_tags = soup.find_all('img')

    # 각 img 태그의 src 속성 추출 및 텍스트 파일에 저장
    with open('image_sources.txt', 'w') as file:
        for img_tag in img_tags:
            img_src = img_tag.get('src')
            if img_src:
                file.write(img_src + '\n')