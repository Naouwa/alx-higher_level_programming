#!/usr/bin/node

// A function that returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
  let occurencesNum = 0;
  let i = 0;
  for (i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occurencesNum++;
    }
  }
  return occurencesNum;
};
