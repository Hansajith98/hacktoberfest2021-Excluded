import java.math.BigInteger;  
public class BigIntegerExample2 {  
    public static void main(String args[]) throws Exception {  
        // Initialize result  
        BigInteger bigInteger = new BigInteger("17");  
        //returns the signum function of this BigInteger  
        BigInteger bigInteger2 = new BigInteger("171");  
        System.out.println("Signum value for "+bigInteger2+" : "+ bigInteger2.signum());  
        //returns the next prime integer that is greater than this BigInteger.  
        BigInteger sub=bigInteger2.subtract(bigInteger);  
        System.out.println(bigInteger2+"-"+bigInteger+" : "+sub);  
  
       // returns the quotient after dividing two bigInteger values  
        BigInteger quotient=bigInteger2.divide(bigInteger);  
        System.out.print(bigInteger2+" / "+bigInteger+" :     Quotient : "+quotient);  
  
        //returns the remainder after dividing two bigIntger values  
        BigInteger remainder=bigInteger.remainder(bigInteger2);  
        System.out.println("       Remaider : "+remainder);  
  
        //returns a BigInteger whose value is ?this << val?  
        BigInteger shiftLeft=bigInteger.shiftLeft(4);  
        System.out.println("ShiftLeft value : "+shiftLeft);  
    }  
}  
