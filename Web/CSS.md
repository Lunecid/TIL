# CSS

- CSS(cascading style sheets) 

## 적용 방법:
1. `<h1 style="color: blue">Chelsea</h1>` : 기존 코드 내에 sytle을 넣어 적용
2. ```HTML
    <style>
        /*
        선택자 {
            속성명1: 속성값;
            속성명2: 속성값;
        }
        */
        h2 {
            color: skyblue;
        }
    ```
    : 기존 코드를 위에 따로 선택자를 만들어 변수를 저장

3. 따로 css파일을 만들어서 링크를 불러와 적용
`<link rel="stylesheet" href="./mystyle.css">`

## 우선순위

1. id
    : `#id {}` 로 선언, 가장 최우선 순위로 적용

2. class
    : `.class {}`로 선언 id보다는 후순위

3. 기본 sytle

## 여러 요소
- `color` : 폰트 색을 변경, rgb값 설정 가능
- `background-color`: 배경 색을 변경
- `text-align` : 글자 정렬 
![CSS](https://blog.hubspot.com/hs-fs/hubfs/Google%20Drive%20Integration/Update%20css%20margin%20vs%20padding-2.png?width=650&name=Update%20css%20margin%20vs%20padding-2.png)
- `border` : 테두리 설정 (border: px,style,color)형태로 사용
    - `border-radius` : 테두리의 가장자리를 둥글게 설정
- `padding`: 컨텐츠를 제외한 Border까지의 영역 top, bottom 으로 영역 설정
- `margin` : 영역의 여백을 설정하고 싶을 때 사용
- `font-family`: link를 통해 `<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tangerine">` 와 같은 형태로 폰트를 외부에서 불러온 후 클래스로 `font-family`를 설정하고 class로 폰트를 설정하면 해당 폰트로 변경 
- `display` 
    -`inline`: `span` 형태와 같은 데이터가 있는 공간만을 차지한다. 
    -`block` : 해당 데이터가 block 형태로 출력, 줄바꿈이 무조건 된다
    -`none`: 해당 데이터가 출력이 되지 않는다
    -`flex` : 데이터의 표시가 가변형이 된다 

