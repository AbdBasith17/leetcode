/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
     let reverse = s.split(" ")
    let x = []
    for (let i=0;i<reverse.length;i++){
       x.push(reverse[i].split("").reverse().join(""))

    }
    return x.join(" ")
};