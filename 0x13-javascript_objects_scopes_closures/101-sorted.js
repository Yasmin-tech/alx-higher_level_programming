#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const values = Object.values(dict);
const valuesUniq = [...new Set(values)];
const newDict = {};
for (const j in valuesUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valuesUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valuesUniq[j]] = list;
}
console.log(newDict);
