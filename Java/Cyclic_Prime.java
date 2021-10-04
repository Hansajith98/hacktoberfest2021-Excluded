package com.company;
import java.net.SocketOption;
import java.util.*;

public class Cyclic_Prime {
    public static void main(String[] args) {

        int a = 131;
        String s1 = a + "", s2 = "";
        int l = s1.length(), p = 1, c = 0;

        do {
            int x = Integer.parseInt(s1);
            for (int i = 2; i < x; i++)
                if (x % i == 0) c++;
            if (c == 0) {
                s2 = s1.charAt(l - 1) + s1.substring(0, l - 1);
            } else {
                p = -1;
                break;
            }
        } while (s1.equals(s2));
        if (p == 1)
            System.out.println("Cyclic");
        else
            System.out.println("Not Cyclic");
    }
}
