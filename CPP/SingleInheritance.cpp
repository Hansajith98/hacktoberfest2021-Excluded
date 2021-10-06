/* C++ program to demonstrate an Example of Single Inheritance  */

#include<iostream>
using namespace std;
class B
{
    int a;
    public:
    int b;
    void get_ab();
    int get_a();
    void show_a();
};

class D: private B
{
    int c;
    public:
    void mul();
    void display();
};

void B::get_ab()
{
    cout<<"\nEnter Values for a and b :: ";
    cin>>a>>b;
}

int B::get_a()
{
    return a;
}

void B::show_a()
{
    cout<<"\na = "<<a<<"\n";
}

void D::mul()
{
    get_ab();
    c=b*get_a();
}

void D::display()
{
    show_a();
    cout<<"\nb = "<<b<<"\n";
    cout<<"\nc = "<<c<<"\n\n";
}


int main()
{

                        D d;
                        d.mul();
                        d.display();
                        d.mul();
                        d.display();
                        return 0;

}
