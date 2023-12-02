const fs = require("fs");
const data = fs.readFileSync("./day1/input1-1.txt", "utf-8").split("\n");

const digits = "0123456789".split("");

function reverse(s) {
  return s.split("").reverse().join("");
}
let result = 0;
data.forEach((str) => {
  let first = "";
  let last = "";

  for (let i = 0; i < str.length; i++) {
    if (digits.includes(str[i])) {
      first = str[i];
      break;
    }
  }

  let reversedStr = reverse(str);
  for (let i = 0; i < reversedStr.length; i++) {
    if (digits.includes(reversedStr[i])) {
      last = reversedStr[i];
      break;
    }
  }

  number = parseInt(first + last);
  result += number;
});

console.log(result);
