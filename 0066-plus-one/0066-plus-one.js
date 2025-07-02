/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
         let x = BigInt(digits.join(""));
        let increment= x+1n
        let newarr = increment.toString().split('').map(Number)
        return newarr
};