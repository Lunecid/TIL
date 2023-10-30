# HTML

- 기본적인 실행 방법 및 구조
    - ! Tab 을 통해 기본적인 구조를 불러온다
    - 기본구조 : `<태그이름 속성명="속성값" 속성명2="속성값2">내용</태그이름>`
- head
    : 문서 정보들을 담는 공간
    - `<title>내용</title>` : 브라우저 탭 상에 내용이 뜬다
    - `link` : 여러가지 링크로 불러온 내용을 추가한다. ex) `shortcut icon` 등등

- body
    : 브라우저 화면에 나타나는 정보들을 담는 공간
    - `h1~6` : 제목,소제목 등 타이틀을 나타낼 때 사용
    - `p` : 문장을 나타낼 때 사용
    - `a href` : 하이퍼링크를 연결할 때 사용
    - `img` : img를 넣을 때 사용
    - `table` : 표를 생성
        - `tr` : table row 의 약자
        - `th` : table header 의 약자
        - `td` : table data의 약자
    - `ul` : unordered list 의 약자, 번호가 없다  
    - `ol` : ordered list 의 약자, 번호가 존재
    - `li` : `ul`,`ol` 의 내부에 값을 넣을 떄 사용 
    
    - `form` : 사용자의 입력정보를 받고 싶을 떄 사용
        - `input` : 여러타입의 데이터 존재, 사용자의 입력정보를 받아옴
            - `radio` : 중복이 되지 않는 선택 상자, name값을 동일하게 해 중복이 안되게 할 수 있다
            - `text` : 기본적인 text를 입력 받는다 
                - `placeholder`: default text가 출력된다
            - `number` : 숫자 값만 입력 가능, step, min, max, value 가 존재
            - `checkbox` : 중복이 가능한 체크 상자
            - `email`: email 형식이 아니면 거부 발생
            - `password` : 입력값이 검은색 점으로 표시
            - `date`: 날짜 데이터 출력
            -`color`: 원하는 색상 선택 가능
            -`submit`: 제출 버튼 표시
        - `label` : 데이터에 라벨을 붙힐 때 사용
            - label의 for 입력값과 input의 id 값이 일치해야 label을 선택헀을 때 선택이 가능해진다.
            - value : 사용자의 입력 정보가 표시 된다 
        - `br` : 줄바꿈
        - `hr` : 줄바꿈 + 가로줄 생성
        - `select`: dropdown select 상자를 생성하기 위해 사용 
        - `div`: 해당 코드를 하나의 데이터로 관리하기 위해 사용 
        







