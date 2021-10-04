/*
This programs converts an Arithmatic Expression in string form to
integer form and solves and gives the output of Numeric Expression
*/

package com.company;
import java.util.*;

public class expression {
    String expn;
    expression() {
        expn = "";
    }

    void input(String ex) {
        expn = ex;
    }

    public static void main(String[] args) {
        expression ob = new expression();
        ob.input("20+7");                           //String input (Arithmatic Expression)
        System.out.println(ob.expn);                //Display Expression
        System.out.println(ob.getfinalval());       //Solve numeric expression to give output
    }

    long getfinalval() {
        String S = "+-*/";
        long a, b; int p=-1;
        char ch;
        for (int i = 0; i < 4; i++) {
            if (expn.indexOf(S.charAt(i))>=0)
                p = expn.indexOf(S.charAt(i));
        }
        if (p==-1)
        {
            System.out.println("Invalid Input");
            return -999;
        }
        a = Long.parseLong(expn.substring(0, p));
        b = Long.parseLong(expn.substring((p + 1)));
        long s = 0;
        ch = expn.charAt(p);
        switch (ch) {
            case '*':
                s = a * b;
                break;
            case '+':
                s = a + b;
                break;
            case '/':
                s = a / b;
                break;
            case '-':
                s = a - b;
                break;
        }
        return s;
    }
}
