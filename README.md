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

<br>     

## 코드 뜯어보기  

### 시간 측정
<img src="https://user-images.githubusercontent.com/63052097/152330631-5a941a33-f04f-4e24-b091-ba8232255580.png" width=300 />  
time 라이브러리를 활용하여 시간을 측정해보았다.    

- 첫 번째 time 시점 = url 입력 받고 웹브라우저를 열고 5초동안 대기 후 시점     
- 두 번째 time 시점 = 해당 웹페이지의 screenshot을 이미지로 저장하고 끝난 시점    
- 세 번째 time 시점 = screenshot을 imrea 메소드로 처리하고 reshape 메소드로 데이터를 처리하고 끝난 시점     
- 네 번재 time 시점 = KMeans() 알고리즘으로 학습시키고 난 후의 시점     
   

첫 번재 두번째 세번째 time은 거의 비슷했고(url을 입력받고 난 후 시각은 대략 4초였다.) 네 번째 tiem은 대략 20초 내외로 걸렸다. 종료시점과 비슷하게 끝난다.        

<br>

### 데이터 feauture 확인
<img src="https://user-images.githubusercontent.com/63052097/152319219-025fd7de-e6bf-4c0f-88e7-66c11749ed56.png" width=200 />        
<img src="https://user-images.githubusercontent.com/63052097/152319452-5c4ab934-2077-4115-9992-9b02707083b0.png" width=200 />      

- imread 메소드 실행 후 반환한 결과 값(데이터 프레임이 아닌 넘파이 배열)은 다음과 같았다. 3차원 배열이었으며 각 픽셀(axis0 : 높이의 개수, axis1: 너비의 개수)에 해당하는 rgb 값(axis2)이 리턴되었다.            

<br>     

<img src="https://user-images.githubusercontent.com/63052097/152320109-e3fb945f-f411-49a8-8d08-bdf265e2cc1a.png" width=200 />           
<img src="https://user-images.githubusercontent.com/63052097/152326403-8099aa7a-ca8c-41c6-9774-96a250c5cbac.png" width=200 />        

- reshape 메소드 실행 후 반환한 결과 값은 다음과 같았다. 2차원 배열이었고 각 픽셀(axis0 : 높이X너비의 개수)에 해당하는 rgb 값(axis1)이 리턴되었다.                  
- 이때 rgb는 3개의 값을 가지므로 feature는 r,g,b의 각 값이며 3개의 특성을 갖는다는 것을 알 수 있다.       

## 참고 자료 
- https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/
- https://hoood.tistory.com/405
- https://www.futurememories.se/en/cases/picular
- https://en.wikipedia.org/wiki/Web_colors#HTML_color_names

## TODO

1. 먼저 관련 논문자료를 읽어보지 못한 것에 대해 아쉬움이 남는다. 특히 데이터를 수집하고 정리하는 일이 어려웠다. 빅데이터에 기반한 어울리는 색채 추천 시스템 이라는 논문을 보고 싶었으나 논문자료가 안 열려서 볼 수 없어 직접 문의해볼 생각이다. https://academic.naver.com/article.naver?doc_id=308062755         
2. 본래 hsv 색채 공간을 활용하고자 했는데 hsv 시스템을 사용할 경우 KMeans() 모델에서 색 추출하고 결과를 보면 예상 색과 다르게 나와 rgb 시스템을 사용했다. 왜 hsv 시스템을 사용하면 예상 결과가 나오지 않는지 그 원인을 파악해야 한다.       
3. 데이터 수집          
4. 위의 프로그램을 실행시켜보면  대략 30초~40초 정도 기다려야 결과를 볼 수 있다. 그런데 https://github.com/lokesh/color-thief color-thief라고 이미지에서 색채를 추출하는 패키지가 있는데 javascript 언어로 구현되어 있고 정말 빠르게 색 추출이 가능하다. 이 코드의 원리를 분석해서 파이썬으로 코드를 계속 구현할지 그냥 아예 javascript로 코드를 작성할지 고민해볼 필요가 있다.       
 
