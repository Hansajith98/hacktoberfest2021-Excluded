/*  C++ Program to demonstrate an Example of Multiple Inheritance  */

#include<iostream>
using namespace std;

        class M
        {
                protected:
                int m;
                public :
                void get_M(int );
        };
        class N
        {
                protected:
                int n;
                public:
                void get_N(int);
        };
        class P: public M, public N
        {
                public:
                void display(void);
        };

        void M::get_M(int x)
        {
                m=x;
        }
        void N::get_N(int y)
        {
                n=y;
        }
        void P::display(void)
        {
        cout<<"\n\tm = "<<m<<endl;
        cout<<"\n\tn = "<<n<<endl;
        cout<<"\n\tm*n = "<<m*n<<endl;
        }
        int main()
        {
                P p;
                p.get_M(10);
                p.get_N(20);
                p.display();
                return 0;
        }
