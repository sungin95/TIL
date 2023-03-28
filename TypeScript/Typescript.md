![캡처](Typescript.assets/캡처.JPG)

Type를 사용하면 형태를 저장해서 재활용 할 수 있다. 

![캡처](Typescript.assets/캡처-16798292104902.JPG)

읽기 전용 처리

![캡처](Typescript.assets/캡처-16798348143484.JPG)

Tuple

3개 타입 동시 넣기 

![캡처](Typescript.assets/캡처-16798351197168.JPG)

리드 온리 추가

![캡처](Typescript.assets/캡처-16798349960666.JPG)



타입을 알수 없는 경우라면?

![캡처](Typescript.assets/캡처-167983655913010.JPG)

활용법

![캡처](Typescript.assets/캡처-167983671206614.JPG)

void (return 값이 없을때) 자동 인식

![캡처](Typescript.assets/캡처-167983688332916.JPG)

에러를 발생 never

![캡처](Typescript.assets/캡처-167983698333418.JPG)

응용 1

![캡처](Typescript.assets/캡처-16798818022491.JPG)

오버로딩

![캡처](Typescript.assets/캡처-16799072459833.JPG)

예시

![캡처](Typescript.assets/캡처-16799075151485.JPG)

옵션

![캡처](Typescript.assets/캡처-16799077023017.JPG)

![캡처](Typescript.assets/캡처-16799096927429.JPG)

제네릭

![캡처](Typescript.assets/캡처-167991006462711.JPG)

![캡처](Typescript.assets/캡처-16799104030311.JPG)

제네릭 2개 이상

![캡처](Typescript.assets/캡처-16799121807383.JPG)



![캡처](Typescript.assets/캡처-16799132781885.JPG)



![캡처](Typescript.assets/캡처-16799141558737.JPG)



![캡처](Typescript.assets/캡처-16799156349359.JPG)



![캡처](Typescript.assets/캡처-167991584177911.JPG)

Class

![캡처](Typescript.assets/캡처-16799226654561.JPG)

abstract class

직접 새로운 인스턴스를 만들 수는 없다. 

![캡처](Typescript.assets/캡처-16799230775685.JPG)

메서드에도 private를 할 수 있다. 

![캡처](Typescript.assets/캡처-16799232106177.JPG)

추상 메서드 

![캡처](Typescript.assets/캡처-16799234187439.JPG)

인스턴스와 메서드에서만 접근하려면 private를 사용하지만 

자식 클라스에서 사용하고 싶으면 protected를 사용하면 된다. 

![캡처](Typescript.assets/캡처-167992448677211.JPG)

private class안에서만

public 모두(안써줘도 됨)

protected class안과 상속된 class에서 사용 가능

abstract는 상속만 가능하다???

제네릭 딕셔너리

![캡처](Typescript.assets/캡처-16799700145991.JPG)



![캡처](Typescript.assets/캡처-16799712718273.JPG)

class 타입

![캡처](Typescript.assets/캡처-16799715405505.JPG)



```typescript
type Words = {
    [key: string]: string
}

class Dict {
    private words: Words
    constructor(){
        this.words = {}
    }

    add(word:Word){
        if(this.words[word.term]===undefined){
            this.words[word.term]=word.def;
        }
    }

    def(term:string){
        return this.words[term];
    }
    static 
}

class Word {
    constructor(
        public readonly term:string, 
        public readonly def:string
    ){}
}

const kimchi = new Word("kimchi", "super cool food");

const dict = new Dict();

dict.add(kimchi);


console.log("KIMCHI:", dict.def("kimchi"));
```

readonly도 가능하다. 



인터페이스 

```typescript
type Team = "red" | "blue" | "yellow"
type Health = 1|5|10

type Player = {
    nickname:string,
    team:Team,
    health: Health
}

const nico :Player = {
    nickname:"nico",
    team:"red",
    health:1
}
```

이걸 interfaces로 변경

```typescript
type Team = "red" | "blue" | "yellow"
type Health = 1|5|10

interface Player  {
    nickname:string,
    team:Team,
    health: Health
}

const nico :Player = {
    nickname:"nico",
    team:"red",
    health:1
}
```

interface는 오로지 오브젝트의 모양을 타입스크립트에게 설명해 주기 위해서만 사용되는 키워드 이다. 

그래서 

```typescript
interface Hello = string  # 사용 불가 
```

인터페이스는 상속을 받을 수 있다. 

```typescript
interface User {
    readonly name:string
}

interface Player extends User {

}
const nico : Player = {
    name:"nico"
}
```

각각 만들어도 합칠 수 있다. 

```typescript
interface User {
    name:string
}
interface User{
    lastName:string
}
interface User {
    health:number
}

const nico:User = {
    name:"nico",
    lastName:"n",
    health:10
}
```



```typescript
abstract class User {
    constructor(
        protected firstName:string,
        protected lastName:string
    ){}
    abstract sayHi(name:string):string
    abstract fullName():string 
}
class Player extends User{
    fullName(){
        return `${this.firstName} ${this.lastName}`
    }
    sayHi(name:string){
        return `Hello ${name}. My name is ${this.fullName()}` 
    }
}
```

상속받는 클래스가 어떻게 동작해야할 지 일러주기 위해서 추상클래스 사용

그런데 컴파일하게 되면 그냥 클래스가 됨. 

이때, interface를 사용하게 됨

```typescript
interface User {
    firstName:string,
    lastName:string,
    sayHi(name:string):string
    fullName():string 
}
interface Human {
    health:number
}
class Player implements User, Human{
    constructor(
        public firstName:string,
        public lastName:string,
        public health:number
    ){}
    fullName(){
        return `${this.firstName} ${this.lastName}`
    }
    sayHi(name:string){
        return `Hello ${name}. My name is ${this.fullName()}` 
    }
    
}
// 함수도 사용 가능
function makeUser(user: User){
    return "hi"
}

makeUser({
    firstName:"nico",
    lastName:"las",
    fullName: () => "xx",
    sayHi: (name) => "string"
})
```





복습 type and interface

```typescript
type PlayerA = {
    name:string
}
type PlayerAA = PlayerA & {
    lastName:string
}
const playerA: PlayerAA ={
    name:"nico",
    lastName:"xxx"
}
///
interface PlayerB {
    name:string
}
interface PlayerBB extends PlayerB{
    lastName:string
}
interface PlayerBB {
    health:number
}
const playerB: PlayerBB = {
    name:"nico",
    lastName:"xxx",
    health:12
}
```

 

```typescript
interface SStorage<T> {
    [key:string]:T
}

class LocalStorage<T> {
    private storage: SStorage<T> = {}
    set(key:string, value:T){
        this.storage[key] = value;
    }
    remove(key:string){
        delete this.storage[key]
    }
    get(key:string):T {
        return this.storage[key]
    }
    clear(){
        this.storage = {}
    }
}

const stringsStorage = new LocalStorage<string>()

stringsStorage.get("key")
stringsStorage.set("hello", "hihi")

const booleansStorage = new LocalStorage<boolean>

booleansStorage.get("xxx")
booleansStorage.set("hello",true)
```

