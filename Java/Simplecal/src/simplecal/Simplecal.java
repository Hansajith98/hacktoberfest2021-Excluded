package simplecal;
import java.util.Scanner;
public class Simplecal{    
   public static void main(String[] args) {
      double n1;
      double n2;
      double result;
      char options;
      Scanner reader = new Scanner(System.in);
      
      System.out.print("Enter First numbers: ");
      n1 = reader.nextDouble();
      
      System.out.print("Enter Second numbers: ");
      n2 = reader.nextDouble();
      
      System.out.print("\nEnter an operator (+, -, *, /): ");
      options = reader.next().charAt(0);
      switch(options) {
         case '+': result = n1 + n2;
            break;
         case '-': result = n1 - n2;
            break;
         case '*': result = n1 * n2;
            break;
         case '/': result = n1 / n2;
            break;
      default: System.out.printf("Error! You Enter incorrect operator");
         return;
      }
      System.out.print("\nYour Result is:\n");
      System.out.printf(n1 + " " + options + " " + n2 + " = " + result);
   }
}

