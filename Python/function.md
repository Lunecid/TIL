# 함수(function)

## 함수의 선언과 충돌


- 함수의 선언

```python
     def func_name(parameter1, parameter2):
    code1
    code2
    ...
    return value
```
- 함수의 호출(실행)
  func_name(parameter1,parameter2)

```python
  def rectangle(height, width):
    area = height * width
    perimeter = (height + width) * 2
    print(area, perimeter)
```

## 함수의 return

- return 값을 만나는 순간 함수는 해당 값을 반환하고 함수를 종료한다.
- 만약, return이 없다면 None을 자동 반환한다.
- return은 오직 하나의 객체만 반환한다.

```python
# 두개의 정수를 받아서 큰 수를 출력

def my_max2(num1,num2):
    # return 'hello' 여기서 멈춘다.
    
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return num1

# return 과 print의 차이: 입력값을 함수는 return을 하는게 목적이다. 

    my_max2(1,2)
    a = my_max(5,5)
    print(a)

# 함수의 결괏값은 할당이 가능하다.

def my_def2(x):
    print(x*2)
    # return None

    a = my_def2(5) # -> 10
    print(a)
    # -> None, print문으로 설정된 값과 함숫값의 차이
```
## 함수의 인수

### 위치인수

기본적으로 함수는 인수의 위치로 판단합니다.

```python

def cylinder(r, h):
    return 3.14 * r**2 * h

print(cylinder(10,5)) # 1570
print(cylinder(5, 10)) # 785

def greeting(name):
    return f'{name}님 안녕하세요!'

greeting('성은')
# -> '성은님 안녕하세요!'

greeting() # -> 오류발생

def greeting(name='익명',age):
    return f'{name}님 {age}이네요. 안녕하세요!'

# -> 오류발생: 인수 name의 기본값으로 설정한 '익명' 으로 인한 오류

def greeting(age, name = '익명'):
    return f'{name}님 {age}살 안녕하세요!'

# 기본값을 할당할 인수는 뒤에 써야한다.
```

## 키워드 인자

함수를 호출(실행)할 때 내가 원하는 위치에 직접적으로 특정인자를 전달 가능

```python

def greeting(age, name = '익명'):
    return f'{name}님 {age}살 안녕하세요!'

print(greeting(10,'홍길동'))
print(greeting(10))
print(greeting(name='홍길동',age=30))

```
### 가변 인자 리스트
- 인자 앞에 *을 붙여 쓸 경우 무수히 많은 인자가 들어갈 수 있다는 의미
```python
    def func(*parms):
        code
        ...
    
# ex)

def my_max(*numbers):
    result = numbers[0]

    for num in numbers:
        if num > result:
            result = num
    return result
```

### 정의되지 않은 키워드 인자 처리하기
```python
def func(**kwargs):
    code
    ...

# 몇개의 밸류, 어떤 키가 들어올지 모를때 사용

def fake_dict(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}는 {value}입니다.')
```

## dictonary를 인자로 넣기(unpacking)

```python
def sing_up(id, pw, pw_confirmation):
    if pw == pw_confirmation:
        print(f'{id}님 회원가입이 완료되었습니다.')
    else:
        print('비밀번호가 일치하지 않습니다.')

account = {
    'id': 'jdc05124',
    'pw': '1234',
    'pw_confirmation': '1234'
}
sing_up(**account)
```

### lambda 표현식

- 임시 함수 생성을 위해 사용

```python
lambda paramter: expression

(lambda x, y: x+y)(1,2) #x,y에 return이 생략됨

```

## 타입힌트

```python
def my_sum(a: int, b: int) -> int:
    return a+b
# 인자 뒤에 :(데이터타입) -> (데이터타입)을 이용하여 어떤 데이터타입인지 표시
```

## 이름공간(scope)

python에서 사용되는 이름들은 이름공간(namespace)에 저장되어있습니다.

- Local scope: 정의된 함수 내부
- Enclosed scope: 상위 함수
- Global scope: 함수 밖의 변수 혹은 import된 모듈
- Built-in scope: python이 기본적으로 가지고 있는 함수 혹은 변수

```python
# 함수 내에서의 a와 밖의 a의 차이
a = 1

def local_scope(a):
    print(a)

local_scope(5)
print(a)

a = 10

def global_scope():
    global a 
# a를 global로 선언했을 경우, 어디에서나 a는 같은 값을 가진다
    print(a)

global_scope()
```

## 재귀(recursive)

재귀 함수는 함수 내부에서 자기 자신을 호출하는 함수를 의미한다.

```python
# 팩토리얼(n! = 1*2*3*...*n)
def fact(n):
    result = 1

    while n > 1:
        result = result * n
        #result *= n

        n = n - 1
    return result

print(fact(5))

# n! = 1 * 2 * 3 * ... * n-1 * n

def factorial(n):
    if n <= 1:
        return 1
    else: 
        return factorial(n-1)*n

print(factorial(5))
```

## 피보나치 수열

- F(0) = F(1) = 1
- F(N) = F(N-1) + F(N-2)

```python
# 반복문

def fib_loop(n):
    result = [1,1]

    for i in range(1,n):
        end1 = result[-1]
        end2 = result[-2]

        fib_num = end1 + end2

        result.append(fib_num)
    return result[-1]

print(fib_loop(10))

# 재귀 (단점으로는 실행시간이 너무 오래 걸린다는 단점이 있다)

def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)
print(fib_rec(10))
```