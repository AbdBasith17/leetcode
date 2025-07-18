/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let m = init
    function increment(){
        return m+=1
    }
    function reset(){
        return m = init
    }
    function decrement(){
        return m-=1
    }
    return {increment,reset,decrement}
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */