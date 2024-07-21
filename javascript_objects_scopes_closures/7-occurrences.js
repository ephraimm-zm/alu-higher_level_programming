#!/usr/bin/node

exports.nb0curences = function (list, searchElement) {
  let counter = 0;
  for (const element of list) {
    if (element === searchElement) {
      counter++;
    }
  }
  return counter;
};
