# 외부 API를 활용하기 위한 작업

1. 활용하려 하는 API의 도메인 주소를 가져온다.
    ex) Url = '주소'

2. 가져온 Url을 requests.get() 을 사용하여 데이터 소스를 불러온다.
    ex) `res = requests.get(Url)`

3. 불러온 데이터 소스를 원하는 형식으로 가공한다.
    ex) `data = res.json()`

    - 불러온 데이터 형식이 복잡하다면 다음과 같이 시행한다.
        1. `from pprint import pprint`
        2. `print` 대신 `pprint` 활용

4. 불러온 데이터 중 원하는 데이터를 변수에 할당한다.
    - 원하는 데이터는 반드시 불러온 데이터 속의 변수를 사용한다.
        ex) `변수명 = data['데이터속변수명']`

5. 데이터 정제하기
    - 원하는 데이터를 정제하기 위해서는 해당 데이터가 존재하는 위치를 찾아 상위에서 하위로 내려와야 한다. 
    - []는 하나의 상위를 뜻한다.

    ex)
    ```python
    items = data['response']['body']['items']
    ```
