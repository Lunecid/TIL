# Basic Command
>python 기본 문법 정리

## 기본적인 Python 변수
1. **저장**
     - 숫자: int
            - ex) `dust = 10`
     - 글자: String
            - ex) `dust ='5'`
     - 참, 거짓: boolean
            - ex) `dust = True or False`
    
2. **조건**
    - if 문: if, elif, else 로 구성
        - elif : else if 의 약자 
            ```python
                if age > 20: 
                    print('성인입니다') 

                elif age > 8:
                    print('청소년입니다')

                else: 
                    print('어린이입니다')`
            ```
3. **반복**
    - while 문: 일정 횟수를 지정하여 반복

        ```python
            while n < 4:
                print(menus[n])
                n = n + 1
         ```

    - for 문: for <1> in <2> : <2>의 내용을 조각, 조각낸 내용을 하나씩 꺼내서 새로운 변수 <2>로 할당

        ```python
            menus = ['백성은', '김규동', '최보규', '최원영'] 
            for gooik in menus:
                print(gooik)
        ```

## 데이터 나열 방식

- List: [] 대괄호를 사용하여 나열
- Dict: {} 중괄호를 사용하여 나열

## 새로운 도구 사용

- python 내에서 지원하는 도구 사용 : `import <>`
    
    ex)
    `random`
    - random.sample(뽑을 범위, 갯수)
    - random.choice()
- python 내에서 지원하지 않는 도구 사용 : install 후 import 
    <>
    - ex) `requests`

## 숫자 단순 나열이 아닌 범위 사용

- `range(a,b)`

    - range : a <= X < b
    
## 숫자 정렬
- `sorted()`: 오름차순 정렬
- `sorted(a, reverse=True)`: 내림차순 정렬

## 집합 형태
- `set()` : 집합 형태로 변형
    - & : 교집합
    
    ex)
    ```python
    print(set(lucky_number) & set(lotto_numbers))
    ```

