/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    for (i=1;i<=x;i++){
        if (x/i==i){
            return i
        }
          else if (i*i > x ){
            return i -1
          }
          
        
    }
    return 0
};