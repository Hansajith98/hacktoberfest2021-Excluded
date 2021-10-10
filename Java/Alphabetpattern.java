package Edureka;
import java.util.Scanner;
public class PatternA {
// Java program to print alphabet A pattern
void display(int n)
{
// Outer for loop for number of lines
for (int i = 0; i<=n; i++) {
// Inner for loop for logic execution
for (int j = 0; j<= n / 2; j++) {
// prints two column lines
if ((j == 0 || j == n / 2) && i != 0 ||
// print first line of alphabet
i == 0  && j != n / 2 ||
// prints middle line
i == n / 2)
System.out.print("*");
else
System.out.print(" ");
}
System.out.println();
}
}
public static void main(String[] args)
{
Scanner sc = new Scanner(System.in);
PatternA a = new PatternA();
a.display(7);
}
}
