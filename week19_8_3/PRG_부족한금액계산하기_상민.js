function solution(price, money, count) {
    let answer = 0;
    let totalPrice = 0
    const range = Array.from({length: count}, (x, i) => i + 1);
    range.forEach(temp => {
        totalPrice += price * temp
    })
    if (money > totalPrice) {
        answer = 0
    } else {
        answer = Math.abs(money - totalPrice)
    }
    return answer;
}
