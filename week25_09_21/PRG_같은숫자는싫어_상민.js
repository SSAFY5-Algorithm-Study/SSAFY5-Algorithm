function solution(arr) {
  var answer = [];
  var previous = null;
  arr.forEach((e, idx) => {
    if (idx === 0 || e !== previous) {
      answer.push(e);
      previous = e;
    }
  });
  return answer;
}
