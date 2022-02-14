function solution(price) {
  const len = price.length;
  let answer = new Array(len).fill(-1);

  for (let i = 0; i < len - 1; i++) {
    for (let j = i + 1; j < len; j++) {
      if (price[i] < price[j]) {
        answer[i] = j - i;
        break;
      }
    }
  }
  return answer;
}
