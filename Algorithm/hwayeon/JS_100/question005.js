// for문 계산하기

// 다음 코드의 출력 값으로 알맞은 것은?
var a = 10;
var b = 2;

for(var i=1; i<5; i+=2){ 
    a += i;
}

console.log(a+b);

// 답안
// i가 1부터 4까지 2step으로 증가하므로 i = 1, 3
// a = 10 + 1 + 3
// b = 2
// console.log(a+b); = 16
