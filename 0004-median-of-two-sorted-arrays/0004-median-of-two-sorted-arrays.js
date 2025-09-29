/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {

    let x= [...nums1,...nums2].sort((a,b)=>a-b)
let mid = Math.floor(x.length/2)
    if( x.length % 2 == 0){
        return (x[mid] +x[mid-1])/2
    }
     return x[mid] 
    
};