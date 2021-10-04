public class palin{
	static boolean Palindrome(String str)
	{
		int j = 0, i = str.length() - 1;
		while (j < i) {
			if (str.charAt(j) != str.charAt(i))
				return false;
			j++;
			i--;
		}
		return true;
	}
	public static void main(String[] args)
	{
		String str = "anna";
		if (Palindrome(str))
			System.out.print("Yes");
		else
			System.out.print("No");
	}
}
