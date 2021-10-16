import java.io.*;
import java.io.*;
import java.util.*;

class Postfix
{
    public Double evaluate(String str){
        LinkedList<Double> stack=new LinkedList<Double>();
        
        for(int i=0;i<str.length();i++){
            Character x=str.charAt(i);
            if(Character.isDigit(x)){
                stack.push(Double.parseDouble(String.valueOf(x)));
            }
            else{
                Double a=stack.pop();
                Double b=stack.pop();
                if(x=='+'){
                    stack.push(b+a);
                    
                }
                else if(x=='-'){
                    stack.push(b-a);
                }
                else if(x=='*'){
                    stack.push(b*a);
                }
                else if(x=='/'){
                    stack.push(b/a);
                }
                else if(x=='^'){
                    stack.push(Math.pow(b,a));
                }
                else if(x=='%'){
                    stack.push(b%a);
                }
            }
        }
        return stack.pop();
    }
}
class Main{

    public static void main(String args[]) throws Exception{
        //fill your code here
       BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        
        System.out.println("Enter postfix expression to be evaluated:");
        Postfix obj=new Postfix();
        
        String ch=br.readLine();
        
        double sd=obj.evaluate(ch);
        System.out.println("Result is : "+(int)Math.floor(sd));
        
    }
}
