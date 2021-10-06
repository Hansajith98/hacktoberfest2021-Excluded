import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Scanner in = new Scanner(System.in);
        
            int n = in.nextInt();
            
            int b = in.nextInt();
            
            int p = in.nextInt();
         
            double sumBi=0, sumPi=0;
            
            for(int i = 0; i < n; i++){
                int Bi = in.nextInt();
                sumBi += Bi;
                int Pi = in.nextInt();
                sumPi += Pi;
            }
            
            double value = Math.ceil(sumBi/10)*b + Math.ceil(sumPi/10)*p;
            int result = (int)value;
            System.out.print(result);
            
            in.close();
    }
}