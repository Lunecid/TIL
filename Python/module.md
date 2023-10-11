# Module

```python
import fibo

print(fibo)

fibo.fib_loop(10)

fibo.fib_rec(5)
```

# 패키지

```python

myPackage/
    __init__.py
    math/
        __init__.py
        fibo.py
        fomula.py
```
패키지 안에 `__init__.py` 파일이 있어야 패키지로 인식

```python

import myPackage

from myPackage.math import fomula

fomula.pi

fomula.my_max(1,2)

import myPackage

myPackage.math.fomula.my_max(1,2)
# from import 를 하지 않고 .을 통하여 파일 경로를 타고가서 불러올 수 있다 하지만 경로가 길어질수록 불편하기 때문에 권장하지 않는다

from myPackage.math.fibo import *
# *를 쓰면 math경로의 모든 함수를 불러오므로 메모리를 많이 차지한다. 따라서 필요한 것만을 뽑아 쓰는 것이 낫다

fomula = 1234
from myPackage.math import fomula as f

print(fomula)
print(f)

# as 를 사용하여 불러올 객체의 이름을 바꿔서 선언할 수 있다.
```

## 파이썬 내장 패키지

- math

    : 수학적 메소드를 불러 올 수 있다 자세한 것은 공식문서 참조
```python
import math

math.pi

math.e

math.ceil(p)

math.floor(p)

math.factorial(10)
```

- random

```python

import random

random.random()

random.randint(a,b)
# a,b까지 범위의 정수의 난수 생성

#seed
random.seed()
random.random()

a = [1,2,3,4,5]
random.suffle(a)

rcp = ['가위','바위','보']
random.choice(rcp)
```

- datetime

```python
from datetime import datetime

datetime.now()

datetime.today()
# today = datetime.today()와 출력 결과가 다르다

datetime.utcnow()
# 본초자오선 기준 시각

now = datetime.now()
now.strftime('%Y년%m월%d일 %A')
# 시간을 str로 formating 해서 출력 


# 메소드를 바로 실행 가능
now.year


now.day

# -> 0~6 / 월~일
now.weekday()

# 특정 날짜를 대입하기
day = datetime(y,m,d)
print(day)

#timedelta 모듈사용, 시간 연산에 사용되는 함수
from datetime import timedelta

future = timedelta(days = 3)
day + future 

new_year = datetime(2024,1,1)
now = datetime.now()

print(new_year - now)
# -> d-day 출력

now = datetime.now()
f = timedelta(days = 100)

print(now + f)
# 100일 뒤 출력

```