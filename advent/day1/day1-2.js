const fs = require("fs");
const data = fs.readFileSync("./day1/input1.txt", "utf-8").split("\n");

const digits = "0123456789".split("");

const basic = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
];

const digitsWords = basic.map((el) => el[0] + el + el[el.length - 1]);

function changeToDigits(text) {
  basic.forEach((basicWord, index) => {
    text = text.replaceAll(basicWord, digitsWords[index]);
  });
  basic.forEach((basicWord, index) => {
    text = text.replaceAll(basicWord, basic.indexOf(basicWord) + 1);
  });
  return text;
}

function reverse(s) {
  return s.split("").reverse().join("");
}

let result = 0;

data.forEach((str) => {
  let first = "";
  let last = "";
  let newstr = changeToDigits(str);

  for (let i = 0; i < newstr.length; i++) {
    if (digits.includes(newstr[i])) {
      first = newstr[i];
      break;
    }
  }

  let reversedStr = reverse(newstr);
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
