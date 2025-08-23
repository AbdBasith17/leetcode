/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
      const count = {};
      const majority = Math.floor(nums.length/2)

      for (let num of nums){
        count[num] = (count[num] ||0) + 1;
        if( count[num]> majority){
            return num
        }
      }
        
    
};