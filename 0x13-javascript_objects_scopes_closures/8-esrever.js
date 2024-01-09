#!/usr/bin/node

// A function that returns the reversed version of a list:

exports.esrever = function (list) {
  const revList = [];
  let element = 0;
  for (element = list.length - 1; element >= 0; element--) {
    revList.push(list[element]);
  }
  return (revList);
};
