# javascript


## 변수 선언

    1. var 
    2. let
        - 재할당이 불가능
    3. const
        - 재할당, 재선언이 불가능

### 타입선언

```js
    let stringvar = "hello"
    let numberVar = 10
    let boolVar = true
    let arrayVar = []
    let objectVar = {}

    // objectVar['name'] = 'kim'
    objectVar.name = "Kim"
    objectVar.location = "seoul"

    // my_dict = Dict()
    let myObj = new Object()
```

### 연산자

```js
myVarA == myVarB // 값만 비교
myVarA === myVarB /// 타입까지 비교
```

## 반복문

```js

// while
let i = 0
while(i<5) {
    console.log(i)
    i++
}

//for
for (let i=0; i=5; i++) {
    console.log(i)
}
//for2 
let myArray = [1,2,3,4,5]

for (let i=0; i <myArray.length; i++) {
    console.log(myArray[i])
}
//for in
for (let item in myArray) {
    console.log(item)
    console.log(myArray[item])
}
//for of
for (let item of myArray) {
    console.log(item)
}
// forEach(map과 비슷한 함수)
myArray.forEach(function(item,index,array){
    console.log(item,index,array)
})
```

## 함수

```js
function multiply1(num1, num2) {
    let result = num1 * num2
    return result
}

// 함수표현식
let multiply2 = function(num1, num2) {
    let result = num1 * num2
    return result
}

// 화살표함수
let multiply3 = (num1, num2) => {
    let result = num1 * num2
    return result
}

// 화살표 함수 생략 1
// {} 안에 코드가 return 하는 문장 하나만 있는 경우 -> {}, return 생략가능 
let multiply4 = (num1, num2) => num1 * num2

// 화살표 함수 생략 2
// () 안에 매개변수가 하나만 있다면 () 생략 가능
let multiply5 = num1 => num1 * 2
```

## 이벤트

```js
//이벤트 리스너

let myH1 = documnet.querySelector('h1')
myH1.addEventListener("click", function(e){
    console.log(e)
})


let myinput = document.querySelector("input")
myinput.addEventListener("keydown", function(e) {
    console.log(e)
})

let myImage = document.querySelector('img') 
myImage.addEventListener("click",function(){
    let src = myImage.getAttribute("src")

    if (src === "본래URL") {
        myImage.setAttribute("src", "바꿀URL")
    } else {
        myImage.setAttribute("src","본래URL")
    }
})
```

## 비동기

```js

console.log("hi")
setTimeout(function(){console.log('hello')},1000)
console.log("bye")


const URL = "외부링크"

// let response = fetch(URL)
// console.log(response)

// let result = response.json()
// console.log(result)
// 위와 같은 방법을 쓸 경우 url이 불러와지기 전에 밑의 코드가 실행되어 에러가 나온다

fetch(URL)
    .then(response => response.json())
    .then(json => console.log(json))

async function fetchAndPrint(){
    let res = await fetch(URL)
    let result = await res.json()

    console.log(result)
}

liElements.forEatch(funtion(li){
    ...
})

liElements.forEach(funtion(li){
    li.addEventListener("click",function(e){
        ...
    })
})

```


