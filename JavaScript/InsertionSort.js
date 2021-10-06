// Insertion Sort implementation in Javascript

function Insertion_Sort(array){
  let temp, i, j;
  for( i = 1; i < array.length ; i++ ){
    temp = array[i];
    for( j = i-1; j >= 0 && array[j] > temp; j-- ){
      array[j+1] = array[j];
    }
    array[j+1] = temp;
  }
  return array;
}

array = [4, 3, 6, 9, 5, 1, 8, 7, 2];

console.log(Insertion_Sort(array));

/*
Input:
[4, 3, 6, 9, 5, 1, 8, 7, 2]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
*/
