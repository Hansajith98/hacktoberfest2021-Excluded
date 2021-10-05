package com.company;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int myNumber = (int)(Math.random()*100);
        int myGuess = 0;

        do {
            System.out.println("Guess my number (1-100) : ");
            myGuess = sc.nextInt();

            if (myGuess == myNumber) {
                System.out.println("WOHOO .... YOU HAVE GUESSED IT RIGHT");
                break;
            }
            else if (myGuess > myNumber) {
                System.out.println("Your number is too large");
            }
            else {
                System.out.println("Your number is too small");
            }
        } while(myGuess >= 0);

        System.out.println("My number was : ");
        System.out.println(myNumber);
    }
}
