function addsum(nums, target) {
    let index = []
    let total = 0
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                index.push(i, j)
            }
        }
    }
    console.log(index)
};
//addsum([3,2,4],6)