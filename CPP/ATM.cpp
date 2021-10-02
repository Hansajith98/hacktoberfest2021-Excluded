#include<iostream>
#include<stdio.h>
using namespace std;
void showMenu()
{
    cout<<"***********Menu***********"<<endl;
    cout<<"1.Check Balance"<<endl;
    cout<<"2.Deposit"<<endl;
    cout<<"3.Withdrawl"<<endl;
    cout<<"4.Exit";
    cout<<"**************************"<<endl;
}
int main()
{
    int number, balance = 500;
    do
{
    showMenu();
    cout<<"Select Option : ";
    cin>>number;
    switch (number)
    {
     case 1: cout<<"Balance is "<<balance<<" rupees"<<endl;break;
     case 2: cout<<"Deposit Amout : ";
     double deposit;
     cin>> deposit;
     balance += deposit;
     break;
     case 3: cout<<"Withdraw Amout : ";
     double withdraw;
     cin>>withdraw;
     if(withdraw <=balance)
     balance -= withdraw;
     else
     cout<<"Insufficient balance"<<endl;
     break;
    }
}
while(number!=4);
return 0;
}