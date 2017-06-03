from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

ImageUrl = ""

def getUrl(ImageUrl):
    ImageUrl = ImageUrl[0]
    ImageUrl = str(ImageUrl)
    ImageUrl = ImageUrl[15:]
    ImageUrl = ImageUrl[:-23]
    print(ImageUrl)
    return ImageUrl

def download_Image(ImageUrl):
    name = ImageUrl[23:]
    name = name[:-18]+".jpg"
    try:
        urllib.request.urlretrieve(ImageUrl,name)
    except:
        name = name[:-9]+".jpg"
        urllib.request.urlretrieve(ImageUrl,name)
    print("image name : {0}\n".format(name))

while(1):
    print("URL을 입력하세요. 0입력시 종료")
    URL = str(input())
    if(URL == '0'):
        break

    try:
        html = urlopen(URL)
        bsObj = BeautifulSoup(html, "html.parser")
        ImageUrl = bsObj.findAll("meta", {"property" : "og:image"})
        ImageUrl = getUrl(ImageUrl)
        
    except:
        print("URL에서 이미지를 가저오는 중 문제가 생겼습니다.\nURL을 확인 해 주세요.\n")

    download_Image(ImageUrl)
