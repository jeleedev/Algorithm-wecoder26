function solution(orders) {
  let order = [],
    foods = [];

  orders.map((e) => {
    const items = e.split(' ');
    const [user] = items;

    if (order[user] == undefined) {
      order[user] = [...items];
    } else {
      order[user] = [...order[user], ...items];
    }
  });

  for (let key in order) {
    order[key] = [...new Set(order[key])];
    foods.push(order[key]);
  }
  const max = Math.max.apply(
    Math,
    foods.map((e) => e.length)
  );
  return foods.filter((e) => e.length === max).map((e) => e[0]);
}
