# 웹페이지를 입력받아 모든 색을 추출하고 색 조합으로 keyword 분석 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import cv2
import time
from sklearn import cluster
from sklearn.cluster import KMeans
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd

# 색깔 비율 확인 
#def color_rate(clt):
#    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
#    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
#
#    hist = hist.astype("int64")
#    hist /= hist.sum()
#
#    return hist

# plot 만드는 함수 
#def plot_colors(hist, centroids):
#    bar = np.zeros((50, 300, 3), dtype="uint8")
#    startX = 0
#
#    for (percent, color) in zip(hist, centroids):
#        endX = startX + (percent * 300)
#        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
#                      color.astype("uint8").tolist(), -1)
#        startX = endX
#
#    return bar

# csv를 list로 변환
def data(file):
    file_path = file
    list = []
    with open(file_path, "r") as f:
      lines = f.read().splitlines()
      list = [line.split(',') for line in lines]  
    return list

# 색깔 확인하는 함수 
def colorCheck(r_d, c_d):
    check = []
    for d in r_d:
        for c in c_d:
            lower = np.array(c[1:4])
            lower = lower.astype(np.int64)
            upper = np.array(c[4:7])
            upper = upper.astype(np.int64)

            if (d[0] >= lower[0] and d[0] <= upper[0]) != 1:
                continue
            if (d[1] >= lower[1] and d[1] <= upper[1]) != 1:
                continue
            if (d[2] >= lower[2] and d[2] <= upper[2]) != 1:
                continue
            check.append(c[0])
    
    return check

# 추상 단어 도출 함수
def colorTofeel(d, check):
    for data in d:
        if check[0] not in data:
            continue
        if check[1] not in data:
            continue
        if check[2] not in data:
            continue

        return data[4:]

            
if __name__ == '__main__':
    
    # headless : 크롬브라우저가 열리지 않고 크롤링
    # https://beomi.github.io/gb-crawling/posts/2017-09-28-HowToMakeWebCrawler-Headless-Chrome.html
    # https://www.hanumoka.net/2020/07/06/python-20200706-python-selenium-headless/
    option = Options()
    option.add_argument('headless')
    option.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=option)

    # 스크린샷 캡처 
    url = input("url을 입력하세요: ")
    browser.get(url)
    time.sleep(5)

    screenshot = browser.save_screenshot('screenshot.png')
    browser.quit

    # img 색상 처리 
    img = cv2.imread('screenshot.png') # img.shape = 3 (height, widht, channel = RGB 3채널을 의미)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR을 HSV 시스템으로 변경
    img = img.reshape(img.shape[0]*img.shape[1],3) # width와 height를 한 개의 array로 통합

    # k개의 데이터 평균을 만들어 clustering
    k = 3
    clt = KMeans(n_clusters=k)
    clt.fit(img)

    # 데이터 수집
    color = clt.cluster_centers_.astype(np.int64)
    color_data = data('color.csv')
    feel_data = data('feel.csv')

    color_name = colorCheck(color, color_data)
    
    print(color_name)
    print(colorTofeel(feel_data, color_name))
    
    #hist = color_rate(clt)
    #bar = plot_colors(hist, clt.cluster_centers_)
    #plt.figure()
    #plt.axis("off")
    #plt.imshow(bar)
    #plt.show()

    
