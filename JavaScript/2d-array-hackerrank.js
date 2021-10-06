function hourglassSum(arr) {
    let highestSum = -9 * 7 - 1;
    for(let index1 = 1;index1 < arr.length - 1;index1++){
        for(let index2 = 1;index2 < arr[0].length - 1;index2++){
            let sum = 0;
            for(let indexTop=-1+index2;indexTop<2+index2;indexTop++){
                sum += arr[index1-1][indexTop];
            }
            sum += arr[index1][index2];
            for(let indexBottom=-1+index2;indexBottom<2+index2;indexBottom++){
                sum += arr[index1+1][indexBottom];
            }
            highestSum = sum > highestSum ? sum : highestSum;
        }
    }
    return highestSum;
}
