# 색을 보고 추상적인 단어를 도출하는 솔루션 개발    

<br>  

## 세부 주제      
- **✅ 특정 위치를 클릭했을 때 색깔이 존재한다면 어떤 색인지 설명 가능**                                  
 손가락 혹은 마우스가 위치한 곳에 색깔이 존재한다면 어떤 색인지 키워드로 전달
 
 <br>                                        

- **✅ 해당 웹페이지의 색깔을 추출하여 색 조합을 분석하여 해당 분위기 혹은 키워드 말하기**   
<p align="center">          
<img src="https://user-images.githubusercontent.com/63052097/152071678-a36c5a37-5900-4ea4-962b-4c8bf9116d4c.png" width=500 />             
</p>              

웹 페이지 링크가 담기면 해당 웹 페이지의 화면을 캡처하고 웹페이지에 존재하는 모든 색을 추출하고 색 조합을 분석하여 추상적인 키워드를 도출하는 솔루션

<br>        

- **✅ 특정 위치에 원하는 색깔 코드 넣어주는 기능**                  
‘color’를 말하고 구체적인 색 혹은 키워드를 말하면 해당 색에 대한 헥스코드 자동 작성  
  
<br>
<br>      

## 개발 동기    
우리는 눈을 통해서 색깔을 확인하기 때문에 "노란색", "주황색"과 같은 정보를 들으면 머리 속으로 색을 떠올릴 수 있다.<br>                  
그러나 상상해보자 우리가 태어날 때 부터 시력이 존재하지 않았다면 "노란색", "주황색"과 같은 정보를 들어도 색을 떠올릴 수 있을까?<br>                 
그렇다면 우리는 색깔 정보를 통해 무엇을 얻을까? 내가 생각한 답은 우리가 "노란색", "주황색"과 같은 색깔 정보를 얻는 것이 아닌 그 색깔 정보를 통해 그 색을 보면서 느낀 추상적인 감정을 얻는다고 생각한다.<br>                      
따라서 시각 장애인 분들에게 "노란색", "주황색"과 같은 색깔 정보를 알려주는 것보다 그 색이 주는 추상적인 감정에 대한 정보를 전달하면 어떨까? 라는 궁금증으로 이 프로젝트를 생각하게 되었다                  

<br>
<br>

## 개발 과정
 
### ✅ 해당 웹페이지의 색깔을 추출하여 색 조합을 분석하여 해당 분위기 혹은 키워드 말하기

- 사용한 라이브러리 : selenium, openCv, sklearn, numpy, matpltlib, pandas

- 파일 설명
```         
chromedriver.exe : 웹크롤링을 하기 위한 크롬 드라이버 
color.csv : 색깔의 rgb 범위 데이터
data.py : 색깔의 rgb 범위를 조정해주는데 도움을 주는 코드
feel.csv : 색깔 조합에 따른 키워드 데이터
screenshot.png : 입력받은 url의 화면 캡처
webToColor.py : main 파일
```               

- 사용법
```
1. webToColor.py를 실행시킨다.
2. 웹페이지의 url을 입력한다.
3. 해당 색깔 정보과 색깔 키워드 결과를 본다
```
이렇게 결과가 나옵니다.                 
<img src="https://user-images.githubusercontent.com/63052097/152073098-01fb7a28-7aff-4c87-ad25-a45ec5d4a060.png" width=500 />       
<img src="https://user-images.githubusercontent.com/63052097/152073102-f24e1e67-694d-489d-9ed4-d38ae00f189e.png" width=900 />             


- 원리
```
1. 해당 웹페이지 링크로 화면 캡처 : selenium 라이브러리와 크롬 드라이버를 통해 웹페이지 화면을 캡처 
2. 이미지에서 색깔 추출 : openCV와 KMean 클러스터링을 이용하여 대표 색깔 3개를 추출
```               

- TODO
```
1. 데이터 더 수집하기 
2. 시간 문제 해결하기 -> js로 언어로 바꿀까 고민중 
```

### 참고 자료 
- https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/
- https://hoood.tistory.com/405
- https://www.futurememories.se/en/cases/picular
- https://en.wikipedia.org/wiki/Web_colors#HTML_color_names
-  
