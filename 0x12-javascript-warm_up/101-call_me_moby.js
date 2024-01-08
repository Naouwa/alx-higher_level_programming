#!/usr/bin/node

// A function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  for (let f = 0; f < x; f++) theFunction();
};
