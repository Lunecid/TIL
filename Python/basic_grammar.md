# Python Basic Grammar

## 1. 데이터 타입
1. number
    - int: 정수
    - float: 소수 포함
    - complex: 허수 포함
        - `.imag`: 허수 부분 출력
        - `.real`: 실수 부분 출력
2. Boolean

   : `True`, `False` 로 이루어진 타입

    - True: Type은 int형, 숫자 1로 표현된다.
    - False: Type은 int형, 숫자 0으로 표현된다.

3. None

    : 데이터가 없음을 의미한다. != 0

4. String
    
    : 문자열 표현
    -  `'`,`"`로 표현한다. 단, 둘 중 하나의 표현을 계속 사용하는 것을 권장한다.
        - `'` 내에 `'`를 사용하고 싶은 경우, 
        ```python
        print("안녕하세요. '백성은'입니다.")   # "와' 동시사용
        print('안녕하세요. \'백성은\'입니다.') # escape문 사용
        ```
    - `input()` 을 이용하여 입력값을 표현할 떄, 이 값은 String 값으로 출력된다.
    
### String interpolation
    1. %-formatting
    2. str.format()
    3. f-string

```python
age = 25
1. print('홍길동은 %s살입니다.'% age)
2. print('홍길동은 ()살입니다.'.format(age))
3. print(f'홍길동은 {age}살입니다.')
```

---

## 2. 연산자

1. 산술연산자

    : + - * / 
    
    - a**b: a에 b를 제곱
    - a//b: a를 b로 나눈 몫을 출력
    - a%b: a를 b로 나눈 나머지를 출력  
        - `divmod(a,b)`: a = 몫, b = 나머지를 출력하는 함수
2. 비교연산자

    : > < >= <= == != 

3. 논리연산자

    : and(&&) or(||) not(!)
    
    1. and: 양쪽 모두 `True`일 때, `True`를 반환
        ```python
        print(True and True)
        print(True and False)
        print(False and True)
        print(False and False)

        print(3 and 5)
        print(3 and 0)
        print(0 and 5)
        print(0 and 0)
        # and의 단축평가: 앞과 뒤가 모두 True 일 경우, 뒤의 True 값을 출력
        ```
    2. or: 양쪽 모두 `False`일 떄, `False`를 반환. 즉, 하나만 `True`여도 `True`를 반환
        ```python
        print(True and True)
        print(True and False)
        print(False and True)
        print(False and False)

        print(3 and 5)
        print(3 and 0)
        print(0 and 5)
        print(0 and 0)
        # or의 단축평가: 앞과 뒤가 모두 True 일 경우, 앞의 True 값을 출력, 하나만 True일 경우 True값을 출력
        ```
4. 복합연산자

    : a += -= *= /= //= %= **= b 
        
    - a와 b를 연산한 값을 다시 a에 할당한다.
5. 기타연산자

- 문자열과 리스트끼리의 산술연산자 사용: 
    ```python
    a = 'hi'
    b = 'hello'
    #concatenation
    a+b = 'hihello'

    a = [1,2,3]
    b = [9,8,7]
    a+b = [1,2,3,9,8,7]
    ```
- in: 글자나 리스트 내의 해당 데이터가 존재하는 지 판별하는 연산자
    ```python
    #containment
    print('a' in 'apple')
    print(1 in [1,2,3])
    ```
- is: 데이터의 메모리 주소를 비교하는 연산자
    ```python
    a = 123123
    b = 123123
    print(a is b)
    -> False
    a = 10
    b = 10
    print(a is b)
    -> True # 자주 사용하는 데이터(-5~256)은 같은 주소에 할당되어 있다.
    ```

---

### 연산자 우선순위

0. ()를 통해 그룹
1. **
2. 산술연산자(*,/)
3. 산술연산자(+,-)
4. 비교연산자, is, in
5. not
6. and, or


---

## 3. 형변환

1. 임시적 형변환

    : 고의로 형변환을 하지 않아도, 시스템에서 계산을 하기 위해 자동으로 형변환을 해주는 형변환

    ```python
    a = True
    b = False
    c = 1

    print(a+c)
    -> 2
    print(a+b)
    -> 1

    int_num = 3
    float_num = 3.3
    complex_num = 3 + 3j

    print(int_num + float_num)
    -> 6.3
    print(int_num + complex_num)
    -> 6 + 3j
    ```

2. 명시적 형변환 

    : 서로 다른 형태를 연산하기 위하여 명시적으로 같은 형태로 변환하는 형변환

    ```python
    a = 1
    b = '번'
    print(str(a) + b)
    -> 1번

    age = int(input())

    print(bool(''))
    -> False # ''안은 공백이기 때문에 False 출력
    print(bool([1,2,3]))
    -> True
    ```
---

## 4. 시퀀스(Sequence) 자료형
    
    : 시퀀스는 데이터의 순서대로 나열된 자료구조(순서대로 나열되어있다는 것은 정렬된 것과는 다르다.)

1. List(배열)

- 선언: 변수이름 = [value1,value2,value3]
- 접근: 변수이름[index]
- 선언 후, 변수를 변경가능하다.

    ```python
    location = ['서울','대전','부산']
    print(location)
    print(type(location))
    -> list

    print(location[2])
    -> 부산
    print(location[-1])
    -> 부산
    print(location[-2])
    -> 대전

    location[2] = '제주'
    print(location)
    ```

2. Tuple

- 선언: 변수이름 = (Value1, Value2, Value3)
- 접근: 변수이름[index]
- list와 유사하지만 수정불가능(immutable)하다.

    ```python
    t = (1,2,3)
    print(t)
    print(type(t))
    print(t[2])
    ```

3. range

- range(n): 0부터 n-1까지 범위
- range(n,m): n부터 m-1까지 범위
- range(n,m,s): n부터 m-1까지 범위, +s만큼 증가하는 범위

    ```python
    r = range(5)
    print(r)
    print(type(r))

    r = range(5,15,2)
    print(r)
    list(r)
    -> [5,7,9,11,13]
    ```

4. String

    : 문자열 표현

5. 시퀀스에서 사용 가능한 연산/함수

    ```python
    my_list = [1,2,3,4,5]
    my_tuple = (11,22,33,44,55)
    my_range = range(1,10,2)
    my_string = '일이삼사오'

    # indexing
    print(my_list[1]) -> 2
    print(my_tuple[1]) -> 33
    print(my_range[1]) -> 3
    print(my_string[1]) -> 이

    # slicing
    # 3은 포함 x 3 미만 
    print(my_list[1:3]) -> [2,3]
    print(my_tuple[1:3]) -> (22,33)
    print(my_range[1:3]) -> range(3,7,2)
    print(my_string[1:3]) -> 이삼

    # 제일 뒤는 간격
    print(my_list[1:4:2]) -> [2,4]
    print(my_range[2:7:2]) -> range(5,11,4) 
    
    print(my_list[:3]) # 처음부터 시작해주세요의 의미
    -> [1,2,3]

    #in
    print(1 in my_list)
    print(11 in my_tuple)
    print(1 in my_range)
    print('일' in my_string)

    #not in
    print(11 not in my_list) -> True
    print(100 not in my_tuple) -> True
    print(1 not in my_range) -> False
    print('구' not in my_string) -> True

    # concatenation
    print(my_list + [1,2,3,4,5])
    print(my_tuple + (1,2,3))


    # *
    print(my_string*3) -> my_string이 3번 반복
    print(my_list*3)

    print([[0]*10]*10) -> 0이 10개 있는 리스트가 가로세로 10번 반복
    ```

    - `len(my_list)`: list의 길이 출력
    - `min(my_tuple)`: tuple에서 가장 작은 값 출력
    - `max(my_range)`: range에서 가장 큰 값 출력
    - `my_list.count(1)`: list에서 1이 몇 개 있는지 출력

---

## 5. 시퀀스 데이터가 아닌 자료구조

    : 수학엥서 사용하는 집합과 동일하게 처리(중복된 값 없음)

1. set
    
    : 수학에서 사용하는 집합과 동일학게 처리(중복된 값이 없음)
    - 선언: 변수이름 = {value1, value2, value3}

    ```python
    my_set_a = {1,2,3,4,5}
    my_set_b = {1,3,5,7,9}

    print(my_set_a - my_set_b) # 차집합
    print(my_set_a | my_set_b) # 합집합
    print(my_set_a & my_set_b) # 교집합


    my_list = {1,2,3,4,5,12,3,2,3,1,3,5,6,7,2,2,}
    print(set(my_list))
    -> {1,2,3,4,5,6,7,12}
    # 리스트에서 중복된 값을 모두 지우고 싶을 때 set()을 사용한다.
    ```

2. dictionary

    - 선언: 변수이름{key1:value1, key2:value2, key3:value3}
    - 접근: 변수이름[key]
    - dictionary는 key와 value가 쌍으로 이루어져있다.
    - key에는 immutable한 모든 값을 사용가능(불변값: string, integer...)
    - value에는 모든데이터 가능(list, dict도 가능)

    ```python
    my_dict = {'서울': '02', '경기': '031'}
    my_dict['서울']

    dict_a = {
        'name': 'seongeun',
        'age': 24,
        'location': 'Busan',
        'numbers': [1,2,3,4,5],
        'friends': {
        'a': 10,
        'b': 11,
            },
    
    }
    print(dict_a['name']) -> seongeun
    print(dict_a['numbers'][3]) -> 4
    print(dict_a['friends']['b']) -> 11

    ```

    - `.keys()` : dict의 모든 key값 출력
    - `.values()`: dict의 모든 value값 출력


---

## 6. 제어문

### 조건문(if문)

```python
if <조건식>: 
    if의 조건식이 참인 경우 실행하는 코드
else:
    if의 조건식이 거짓인 경우 실행하는 코드

```

1. `if` 문은 반드시 참/거짓을 판단 할 수 있는 `조건식`과 함께 사용한다.
2. `조건식`이 참인 경우 : 이후의 문장을 실행한다.
3. `조건식`이 거짓인 경우 : else: 이후의 문장을 실행한다.

```python
my_string = input()

if my_string == '12/25':
    print('크리스마스입니다.')
else: 
    print('크리스마스가 아닙니다.')

#num을 2로 나눈 나머지는 0,1 두가지 경우가 있다.
#if 조건식에 0,1 은 자동형변환이 일어나 False, True로 변환된다.
num = input('숫자를 입력해주세요: ')
num = int(num)

if num % 2:
    print('홀수 입니다.')
else: 
    print('짝수 입니다.')


num = input('숫자를 입력해주세요: ')
num = int(num)

if num % 2 == 0:
    print('짝수 입니다.')
else: 
    print('홀수 입니다.')
```

#### elif

```python
if <조건식>:
    if 조건이 참인 경우 실행
elif <조건식>:
    elif 조건이 참인 경우 실행
else: 
    위의 조건식에 하나도 부합하지 않는 경우 실행

score = int(input())

# 90점이상 A (95이상이라면 good 추가)
# 80점이상 B
# 70점이상 C
# 나머지 F

if score >= 90:
    print('A')
    if score >= 95:
        print('good')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
```

#### 조건표현식

```python
true_value if <조건식> else false_value

# ex)
num = 10
result = '홀수' if num % 2 == 1 else '짝수'
print(result)
```

---

### While 문

```python
    while <조건식>:
        실행할 코드


# ex)
greating = ''

while greating != '안녕':
    greating = input('안녕이라고 말해 : ')
# 미래가 보장되지 않는 상황에서 사용하는 경우가 잦다.
```

### for 문

- 정해진 범위 내의 반복

    ```python
    for variable in sequence:
        실행할 코드

    # ex)
    numbers = [1,2,3,4,5]

    for number in numbers:
    print(number)

    word = input('단어를 입력하세요')

    for char in word:
    print(char)
    #문자열도 하나의 시퀀스가 될 수 있다.

    for i in (1,2,3,4,5):
    print(i)

    # 핵심은 어떤 구조든 반복문 처리를 할 수 있다는 점

    #2. 1~30까지 숫자 중에서 홀수를 모아서 리스트로 출력

    list = []
    for i in range(31):
        if i % 2 != 0:
            # print(i)
            list.append(i)
            # x.append(): 내용을 x에 저장한다.

    print(list)

    for item in enumerate(menus):
    print(item)
    # enumerate()는 결괏값이 튜플로 출력된다.

    for index,menu in enumerate(menus):
    print(index,menu)
    # 튜플로 출력하고 싶지 않을 떄 (x,y)형태로 사용가능하다.
    ```

### dictionary 반복

1. for key in dict:
2. for key in dict.keys():
3. for value in dict.value():
4. for key, value in dict.item():


```python
# 1.
blood_type = {
    'A' : 5,
    'B' : 4,
    'O' : 2,
    'AB' : 3,
}
print('혈액형 목록은 다음과 같습니다.')
for key in blood_type:
    print(key)

# 2.
print('혈액형 목록은 다음과 같습니다.')
for key in blood_type.keys():
    print(key)

total_value = 0

# keys 뿐만 아니라 values 도 가능
for value in blood_type.values():
    total_value += value
print(f'총인원은 {total_value}명입니다.')

# items 도 가능 
for key,value in blood_type.items():
    print(f'{key}형은 {value}명입니다.')
```

### break, continue

```python

for i in range(100):
    print(i)
    if i > 10:
        print('10넘으면 다메')
        break

rice = ['보리','보리','보리','보리','보리','보리','보리','쌀','보리','보리',]

for index,key in enumerate(rice):
    print(key)
    if key == '쌀':
        print(f'{index+1}번째만에 쌀 잡았다')
        break
     
```

- continue 
    : continue 이후의 코드를 실행하지 않고 다음 반복을 실행

```python
age = [10,20,30,40,33,59]

for a in age:
    if a <= 20:
        continue
    print(f'{a}살은 성인입니다.')
```

- else 
    : else문은 끝까지 반복이 진행이 된 후 실행합니다. (break를 만나지 않은 경우)

```python

for i in range(12):
    print(i)
    if i > 10:
        break

else: 
    print('break 못만남')

numbers = [1,2,3,4,5]
print(1 in numbers) -> True
print(99 in numbers) -> False

numbers = [1,2,3,4,5]
target = 5

for number in numbers:
    if number == target:
        print(number)
        print(number in numbers)
        break

else:
    print(f'{target}은/는 numbers에 없습니다.')
    print(target in numbers)
   
    
```

### True, Pass 문

```python
def login():
    pass

def logout():
    pass

```

### match 문

```python

match value:
    case 조건:
        실행할 코드
    case 조건:
        실행할 코드 
    case _:
        실행할 코드

# ex)
status = 404
match status:
    case 400:
        print('bad request')
    case 404:
        print('not found')
    case _:
        print('something is wrong')
```

