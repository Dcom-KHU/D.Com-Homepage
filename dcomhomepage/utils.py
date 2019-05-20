import time
import random
import string
from bs4 import BeautifulSoup

def getfilename(filename):
    return str(time.time()) + filename


def extractImage(html):
    """
    html Document의
    이미지를 추출 합니다.
    """

    soup = BeautifulSoup(html, 'html.parser')
    img = soup.select_one('img')

    if img is None:
        return None
    else:
        return img.get('src', None)


def extractText(html):
    """
    html Document의
    텍스트를 추출합니다.
    """

    soup = BeautifulSoup(html, 'html.parser')
    return soup.text


def make_random_string():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(20))
