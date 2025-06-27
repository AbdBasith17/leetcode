/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
 let x = s.trim().split(" ");
 let lastword = x[x.length-1]
return lastword.length  
};