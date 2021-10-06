import java.lang.*;
import java.io.*;
import java.util.*;

public class RS{
    public static void main(String[] args)
    {
        String input = "JAVACOMPILER";
 
        
        byte[] BA = input.getBytes();
 
        byte[] res = new byte[BA.length];
 
        for (int i = 0; i < BA.length; i++)
            res[i] = BA[BA.length - i - 1];
 
        System.out.println(new String(res));
    }
}
