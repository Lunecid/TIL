# Error

## SyntaxError

```python

if True:
    pass
else
# SyntaxError: expected ':'

print('hi
# SyntaxError: incomplete input
```
```python
if True print('hello')

# SyntaxError: invalid syntax
```

## exception

```python
print(5/0)
#ZeroDivisionError

print(hello)
#NameError

1 + '1'
#TypeError

'1' + 1
#TypeError

import random

random.sample([1,2,3,4])
#TypeError

random.sample([1,2,3,4]2,2,3)
#TypeError

int('4.5')
#ValueError

numbers = [1,2,3,4]
numbers.index(100)
#ValueError

my_dic = {
    'apple': '사과',
    'banana': '바나나',
}
my_dict['watermelon']
#KeyError

import asdf
#ModuleNotFoundError

while True:
    continue
#KeyboardInterrupt 무한 반복되는 코드이기 때문에 직접 종료해줘야한다 그때 나오는 에러 
```

---
## 예외처리
```python
try:
    code
except 예외:
    code
```

```python
try:
    num = int(input('숫자를 입력해주세요 :'))
    print(f'{num}의 세제곱은 {num**3}입니다.')
except ValueError:
    print('숫자를 입력하라고')

# 두 가지의 예외처리를 처리할 때
try:
    num = int(input('100을 나눌 값을 입력해주세요'))
    print(f'100을 {num}으로 나누면 {100/num}입니다')
except ValueError:
    print('입력한 정보는 숫자가 아닙니다.')
except ZeroDivisionError:
    print('수학적으로 0으로는 나눌 수 없습니다.')

# 전체 에러를 한꺼번에 처리할 때
try: 
    num = int(input('100을 나눌 값을 입력해주세요'))
    print(f'100을 {num}으로 나누면 {100/num}입니다')
except:
    print('에러발생')


try: 
    print(asdf)
    num = int(input('100을 나눌 값을 입력해주세요'))
    print(f'100을 {num}으로 나누면 {100/num}입니다')
except (ValueError,ZeroDivisionError):
    print('에러발생')
except:
    print('너 잘못 됐어')
# 전체 에러를 받아드리는 except는 마지막에 존재해야한다.

# 에러의 이름을 as로 선언할 수 있다
try:
    my_list = [1,2,3]
    print(my_list[100])
except IndexError as err:
    print('범위에 문제가 있습니다')
    print (err)

# else : 예외가 발생하지 않을 경우 실행되는 코드
try:
    numbers = [1,2,3]
    num = numbers[100]
except:
    print('문제 발생')
else:
    print(num ** 3)

# finally : 예외 상황과 무관하게 무조건 최종적으로 실행되는 코드
try:
    numbers = [1,2,3]
    num = numbers[1]
except:
    print('문제 발생')
finally:
    print('end')

# 예외를 강제로 발생시키는 상황에서 사용
raise

for i in range(100):
    if i == 50:
        print(i)
        raise

# 연습
def my_div(num1, num2):
    try:
        print(f'{num1}을 {num2}로 나누면 {num1/num2}란다.')
    except ZeroDivisionError:
        print('0으로는 나눌 수 없단다 꼬마야')
    except TypeError:
        print('너 누가 그렇게 가르치디')
        # return None
    except:
        print('알 수 있을지도 모르는 오류 발생')
    else:
        print('오류없음')
    finally:
        print('QED')
        
print(my_div(5, 0))
print(my_div('5','0'))
print(my_div(5,2))
# print(my_div([1,2,3],4))
```