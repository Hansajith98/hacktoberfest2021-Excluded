package Matrix;

public class Spiral_traversal {
	static void Spiral(int arr[][], int r, int c) {
		int top=0, bottom = r-1, left=0, right = c-1;
		while(top<=bottom && left<=right) {
			for(int i=left;i<=right;i++)
				System.out.print(arr[top][i]+" ");
			top++;
			for(int i=top;i<=bottom;i++)
				System.out.print(arr[i][right]+" ");
			right--;
			if(top<=bottom) {
				for(int i=right;i>=left;i--)
					System.out.print(arr[bottom][i]+" ");
				bottom--;
			}
			if(left<=right) {
				for(int i=bottom;i>=top;i--)
					System.out.print(arr[i][left]+" ");
				left++;
			}
		}
	}
	
	public static void main(String[] args) {
		int arr[][] = {	{1,2,3,4},
						{5,6,7,8},
						{9,10,11,12}	};
		int r = arr.length;
		int c = arr[0].length;
		System.out.println("Array: ");
		Matrix obj1 = new Matrix();
		obj1.print(arr, r, c);
		System.out.println("\nSpiral Traverse");
		Spiral(arr,r,c);
		
	}

}
