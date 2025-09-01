/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let x = s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase()
let reversed = x.split('').reverse().join('');

return  x == reversed
};