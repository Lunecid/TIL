# 문자열 메소드

```python
a = 'hello my name is seongeun'
a[0] = 'H' 
# 문자열은 immutable 하기 때문에 수정이 불가능

a.capitalize()
# capitalize()는 return 값을 내놓을 뿐이지 본래 a 값의 내용을 바꾸지 않는다 ( a = a.capitalize() 를 해야 저장됨 )

a.title()
# 문장의 첫글자를 모두 대문자로 바꾸기

a.lower()
# 첫글자를 소문자로 바꾸기

my_list = ['hi','my','name']
''.join(my_list)

# -> himyname
```

- `.strip([chars])`

    : 단어의 공백을 없애주거나 특정 문자를 지우고 싶을 때 사용

```python
my_string = '       hello \n     '
print(my_string)
print(my_string.strip())

my_string2 = 'lonelyrorilonely'
print(my_string2.strip('lonely'))
print(my_string2.lstrip('lonely'))
print(my_string2.rstrip('lonely'))
```

- `.replace(old,new[, count])`

    : 원하는 글자를 다른 글자로 바꾸고 싶을 때 사용

```python
a = 'woooooooooow'
a.replace('o','w', 3)

# -> 'wwwwooooooow'
```

- `.find(x)`

    : x가 몇 번째 인덱스인지 찾기 위해서 사용

```python
a = 'apple'
print(a.find('p'))
print(a.find('p'))

print(a.find('z'))

# for i in range(len(a)):
#     if 'p' == a[1]:
#         print(i)
#         break
#     else:
#         print(-1)

```

- `.index(x)`

    : find와 마찬가지이지만 x 값이 존재하지 않을 경우 오류가 발생


```python
a = 'apple'
print(a.index('a'))
print(a.index('z'))
```

- `.split(x)`

    : 문자열을 리스트의 원소형태로 변환시켜주는 메소드

```python
a = 'my name is'
print(a)
a.split() # -> ['my','name','is']
a.split('_') # -> ['my name is']
```

- `.count(x)`

    : 문자열에 x와 같은 문자가 몇 개 존재하는 지 알려주는 메소드

```python
'woooooooooow'.count('o')

# -> 10
```

---
# 리스트 메소드

```python
numbers = [1,5,2,6,2,1]
```

- `.append(x)`

    : 리스트 끝에 x 값을 삽입하기 위하여 사용

```python
numbers.append(10)
print(numbers)

# -> [1,5,2,6,2,1,10]
```

- `.extend(iterable)`

    : 리스트에 다른 리스트를 이어붙이기 위하여 사용

```python
a = [99,100]

numbers.extend(a)
print(numbers)
print(numbers + a)
```

- `.insert(idx,x)`

    : 리스트 내에 원하는 글자를 삽입하기 위하여 사용

```python
numbers.insert(3,3.5)
print(numbers)
```

- `.remove(x)`

    : 리스트에서 원하는 글자를 지우기 위하여 사용

```python
numbers.remove(3.5)
print(numbers)
```

- `.pop()`

    : 리스트의 인덱스를 지울 때 사용

```python
numbers.pop()
print(numbers)

numbers.pop(0)
print(numbers)

num = numbers.pop()
print(num)

# -> 2 지워지는 데이터가 출력
```

- `.sort()`

    : 리스트를 정렬

```python
numbers = [7, 1, 5, 5]
print(numbers)

print(numbers.sort())
print(numbers)

# 내림차순으로 정렬
numbers.sort(reverse=True)
print(numbers)

sorted(numbers) 
# 원본이 수정되지 않는다. but, return 값은 정렬된 것을 출력
```

- `.reverse()`

    : 리스트를 뒤집어서 출력

```python
numbers = [7,1,5,5,1,5,5,7]
print(numbers)
numbers.reverse()
print(numbers)

numbers = numbers[ : : -1 ] # reverse의 다른 표현
print(numbers)
```

---

## List Copy

```python

origin_list = [1,2,3]
copy_list = origin_list

print(origin_list)
print(copy_list)

copy_list[0] = 100
# -> copy 값만 변경해도 원본의 값도 변경된다

print(origin_list)
print(copy_list)

a = [1,2,3]
# b = list(a)
# b = a는 주소가 같아지는거지 값이 같아지는 게 아니다.
b = a[ : ]
# b라는 새로운 리스트 생성해야 함

b[0] = 100
print(a)
print(b)

a = [1, 2, [99, 100]]
b = a[ : ]

b[2][1] = 1000 
# 리스트 내의 리스트를 불러올 때

print(a)
print(b)

#리스트 내의 리스트를 복사해서 복수의 리스트를 만들 때
import copy
a = [1, 2, [99, 100]]
b = copy.deepcopy(a) # 리스트 안에 리스트가 있는 deep한 상황일 때 사용하는 메소드

b[2][1] = 1000

print(a) # -> 변경 x 본래 리스트
print(b)
```

---
## List comprehension

```python
numbers = list(range(1,11))
print(numbers)

# [1, 8, 27 ... 1000] -> 세제곱 만들기

result = []

for number in numbers:
    result.append(number**3)
print(result)

result2 = [number ** 3 for number in numbers ]
print(result2)

# 짝수만 고르기
even_list = []
for number in numbers:
    if number % 2 == 0:
        even_list.append(number)

print(even_list)

# 짝수만 고르기 (list.comprehension)
even_list2 = [ number for number in numbers if number % 2 == 0]
print(even_list2)

words = 'My name is hong'
vowels = 'aeiou'

# => my nm s hng

# 1. for문 
words_list = []

for word in words:
    words_list.append(word)
    for vowel in vowels:
        if vowel == word:
            words_list.remove(word)

print(''.join(words_list))


for word in words:
    if word not in vowels:
        result.append(word)

print(''.join(words_list))

words_list = [ word for word in words if word not in vowels]
print(words_list)
print(''.join(words_list))

```

---

# 딕셔너리 메소드

```python
info = {
    'name': 'seongeun',
    'location': 'seoul',
}

# .pop(key[, default])
print(info)
print(info.pop('location'))

print(info)
print(info.pop('location', 'hello'))

print(info)
print(info.pop('location', None))

# .update()
info.update(name='park')
print(info)

# .get(key[, default])
print(info.get('name')) # -> park value만 출력
print(info.get('phone')) # get은 해당하는 값이 없어도 에러는 출력되진 않는다
print(info.get('phone','해당키가없습니다.어쩔건데'))

```

## dict comprehension

```python

# for
# {1: 1, 2: 8, 3:9 ...}
result={}
numbers = range(1,11)
for number in numbers:
    result[number] = number ** 3
print(result)

# comp
result2 = { number : number ** 3 for number in range(1,11) }
print(result2)

# 
dust = {
    '서울': 100,
    '대구': 30,
    '부산': 50,
    '광주': 80,
    '제주': 20
}

# result = {
#     '서울': 100,
#     '부산': 50,
#     '광주': 80
# }

result = {}
for city in dust:
    if dust[city] >= 50:
        result[city] = dust[city]
print(result)

for k, v in dust.items():
    if v >= 50:
        result[k] = v
print(result)

result2 = {city : '나쁨' for city in dust if dust[city] >= 50}
print(result2)



```

---

# 세트 메소드

```python

fruits = {'apple', 'banana', 'melon'}

# .add(x)
fruits.add('watermelon')
print(fruits)

# .update()
fruits.update('grape')
print(fruits) # -> 문자 하나하나가 모두 세트에 배열
fruits.update({'grape'})
print(fruits) # -> 단어로 배열하려면 {} 사용
fruits.update({'grape','orange'})
print(fruits)

# .remove()
fruits.remove('orange')
print(fruits)

# .pop()
fruits.pop()
print(fruits)
```

# map, filter, zip

- map(funtion, iterable)

```python
a = [1,2,3]
number_str = map(str, a)
print(number_str)
# -> <map object at 0x105b97760>
print(list(number_str))
# -> ['1', '2', '3']

def cube(x):
    return x ** 3

print(cube(5))
print(cube(100))

result = []
for i in a:
    result.append(i ** 3)

print(result)

result2 = map(cube, a)
print(list(result2))

a = '1 3 5 7 9'
number = list(map(int, a.split()))
print(numbers)
```

- filte(funtion, iterbale) 

    : filter 에 들어가는 funtion은 T/F을 반환해야 합니다.


```python

numbers = [1,2,3,4,5]

def is_odd(x):
    # if x % 2 == 1:
    #     return True
    # else:
    #     return False

    return bool(x%2)

# for
result = []
for number in numbers:
    if is_odd(number):
        result.append(number)
print(result)

result2 = filter(is_odd, numbers)
print(list(result2))

```

- zip

```python
a = [1,2,3]
b = [100,200,300]

result = zip(a,b)
print(result) # -> <zip object at 0x106343840>
print(list(result))
# -> [(1, 100), (2, 200), (3, 300)]

```