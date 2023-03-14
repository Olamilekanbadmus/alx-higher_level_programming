#!/usr/bin/node

const dict = require('./101-data.js').dict;

let newDic = {};
for (let key in dict) {
  if (newDic[dict[key]] === undefined) {
    newDic[dict[key]] = [];
  }
  newDic[dict[key]].push(key);
}

console.log(newDic);
