
import java.util.Arrays;

public class bubbleSort {
    public static void main(String[] args) {
        int arr [] = {1,80,-56,4,7,2,9,5};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
    static void sort(int [] arr){

        for (int i = 0; i <arr.length ; i++) {
            boolean swap = false;
            for (int j = 1; j < arr.length-i ; j++) {
                if (arr[j]<arr[j-1]){
                    int temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                    swap = true;
                }
            }
            if (swap == false){
                break;
            }
        }
    }

}
