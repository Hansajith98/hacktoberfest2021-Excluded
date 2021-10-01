let p1 = new Promise((resolve, reject) => {
    setTimeout(() => resolve("one"), 200);
});

let p2 = new Promise((resolve, reject) => {
    setTimeout(() => resolve("two"), 300);
});

let p3 = new Promise((resolve, reject) => {
    setTimeout(() => resolve("three"), 100);
});

let p4 = new Promise((resolve, reject) => {
    setTimeout(() => reject("four"), 500);
});

let p5 = new Promise((resolve, reject) => {
    setTimeout(() => reject("five"), 100);
});

let p6 = 20;

function settleAllPromise(promiseArray) {
    let resultArray = [];
    let promiseExecuted = 0
    return new Promise((resolve, reject) => {
        promiseArray.forEach(async(promise, index) => {
            try {
                const response = await promise;
                resultArray[index] = {
                    status: 'fulfilled',
                    value: response
                }
            }
            catch(err){
                resultArray[index] = {status:'rejected',reason:err}
            }
            finally{
                promiseExecuted++;
                if(promiseExecuted === promiseArray.length){
                    resolve(resultArray);
                }
            }
        })
    })
}

settleAllPromise([p1, p2, p3, p4, p5, p6]).then((res) => console.log(res));
/* Output: 
[
  { status: 'fulfilled', value: 'one' },
  { status: 'fulfilled', value: 'two' },
  { status: 'fulfilled', value: 'three' },
  { status: 'rejected', reason: 'four' },
  { status: 'rejected', reason: 'five' },
  { status: 'fulfilled', value: 20 }
]
*/
