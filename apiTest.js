fetch('https://reqbin.com/echo/get/json')
   .then(response => response.text())
   .then(text => console.log(text))

   let array = ['JavaScript', 'Clear', 'Array', 'Example'];

array.length = 0;

console.log(array.length);
console.log(array);