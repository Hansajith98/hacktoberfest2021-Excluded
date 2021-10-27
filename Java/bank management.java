import java.util.*;
class bank
{
  public int damount,wamout,currentblance,pin;
  String sname;
  String atype;
  public void custmdetail()
  {
	  System.out.println("****CUSTOMOR DETAILS ARE *****");
	  System.out.println("name: "+sname);
	  System.out.println("accounttype: "+atype);
	  System.out.println("Pin: "+pin);
	  System.out.println("currentblance: "+currentblance);
	  
  }
  public void tryagain()
  {
	  Scanner sc=new Scanner(System.in);
	  System.out.println("Enter your amount with star account");
	  currentblance=sc.nextInt();
  }
  public void createaccount()
  {
	  Scanner sc=new Scanner(System.in);
	  System.out.println("Enter the name");
	  sname=sc.nextLine();
	  System.out.println("Enter the accounttype");
	  atype=sc.nextLine();
	  System.out.println("Enter the 4 digit pin");
	  pin=sc.nextInt();
      System.out.println("Enter your amount with star account");
       currentblance=sc.nextInt();
	   if(currentblance<5000)
	   {
		   System.out.println("sorry! this amout is not valide to open account");
		   tryagain();
	   }	   
  }
  public void depo()
  {
	  Scanner sc=new Scanner(System.in);
	  System.out.println("enter the deposit amount");
	   damount=sc.nextInt();
	   if(damount>100)
	   {
	   currentblance=currentblance+damount;
	   }
	   else{
		   System.out.println("Sorry!you can deposit greter than 100 hundred try again");
		   depo();
	   }			  
  }
  public void withrodw()
  {
	  Scanner sc=new Scanner(System.in);
	  System.out.println("enter the withdraw amounts");
	  wamout=sc.nextInt();
	  if(currentblance<500)
	  {
		  System.out.println("efficient fund try again");
		  withrodw();
	  }
	  else
		  currentblance=currentblance+wamout;
  }
  public void balanceinquiry()
  {
	  System.out.println("now your currentblance:" +currentblance);
  }

	  public static void main(String args[])
	  { bank b1=new bank();
	   for(int i=0;i<=3;i++)
	   {
	     System.out.println("1.Create new Account");
		 System.out.println("2.deposite money");
		 System.out.println("3.withrodw money");
	     System.out.println("4.blance inquire");
		 System.out.println("5.Accountinfo");
	      int ch;
		  do{
		   Scanner sc=new Scanner(System.in);
		   System.out.println("enter your choise");
		    ch=sc.nextInt();
		  switch(ch)
		  {
			case 1:
			  b1.createaccount();
			  break;
		    case 2:
			  b1.depo();
			  break;
	       case 3:
			  b1.withrodw();
			  break;
		    case 4:
			  b1.balanceinquiry();
			  break;
		    case 5:
			  b1.custmdetail();
			  break;
		  }
		   }
		   while(ch!=3);
	  }
	  }
}	  
  
			  
			 
		  
	  
