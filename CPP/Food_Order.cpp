#include<iostream>
#include<fstream>
using namespace std;
class food
{


private:
    int order, bill;

    string name, pass, nname, npass, orderagain ,alogin, name1, pass1;

public:
    void signup()
    {
        string samename;

        cout<<"----------------"<<endl;
        cout<<"     SIGN UP"<<endl;
        cout<<"----------------"<<endl;
        cout<<"Enter your username:";
        cin>>name;
        ifstream objsamename;
        objsamename.open("name.txt", ios::in);
        if(objsamename)
        {
        objsamename.seekg(0, ios::beg);
        while(!objsamename.eof())
        {
            getline(objsamename,samename);
            if(name==samename)
            {
                cout<<"User name already taken."<<endl;
                signup();
            }
        }
        }
        objsamename.close();
        cout<<"Create your password:";
        cin>>pass;
        filewrite();
        cout<<"Sign up complete."<<endl<<endl;
        login();

    }

    void login()
    {
        system("CLS");
        cout<<"----------------"<<endl;
        cout<<"     LOGIN"<<endl;
        cout<<"----------------"<<endl;
        cout<<"Username:";
        cin>>nname;
        cout<<"Password:";
        cin>>npass;
        check();
    }
    void filewrite()
    {
     ofstream objname, objpass;
     objname.open("name.txt", ios::out|ios::app);
     if(!objname)
     {
         cout<<"File not created."<<endl;
     }
     else
     {
         objname<<name<<endl;
     }
     objname.close();
     objpass.open("password.txt", ios::out|ios::app);
     if(!objpass)
     {
         cout<<"ERROR"<<" File not created."<<endl;
     }
     else
     {
         objpass<<pass<<endl;
     }
     objpass.close();

    }
    void check()
    {
        int c=0;
        ifstream objname, objpass;
        int countn=0, countp=0;
        objname.open("name.txt", ios::in);
        objpass.open("password.txt", ios::in);
        objname.seekg(0,ios::beg);
        objpass.seekg(0, ios::beg);
        while(!objname.eof())
        {

            getline(objname,name1);
            countn=countn+1;
            if(nname==name1)
            {
                while(!objpass.eof())
                {
                getline(objpass,pass1);
                countp=countp+1;
                if(countn==countp)
                {
                if(npass==pass1)
                {
                   c=1;
                   info();
                   menu();
                }
                }
                }
            }
        }
        if(c==0)
        {
            cout<<"Wrong name or password. Please enter again."<<endl;
            login();
        }
        else
        {
            cout<<"Login successful."<<endl;
        }
        objname.close();
        objpass.close();
    }

      void asignedup()
    {
        system("CLS");
            cout<<"------------------------"<<endl;
            cout<<"Welcome to Quick Order"<<endl;
            cout<<"------------------------"<<endl;
            cout<<"Already signed up?"<<endl<<"Enter Y to login and N to sign up:";
            cin>>alogin;
            if(alogin=="Y"||alogin=="y")
            {
                login();
            }
            else if(alogin=="N"||alogin=="n")
            {
            signup();
            login();
            }
            else
            {
                cout<<"No match found."<<endl;
                asignedup();

            }
    }

    void info()
    {
        cout<<endl<<"Hi there. "<<"What would you like to order today?"<<endl;
    }
    void menu()
    {
        system("CLS");
        cout<<"----------------"<<endl;
        cout<<"     MENU"<<endl;
        cout<<"----------------"<<endl;
        cout<<"1.Pizzas"<<endl<<"2.Burgers"<<endl<<"3.Biryani"<<endl;
        cout<<"Please enter your choice:";
        cin>>order;
        if(order==1)
        {
            pizza();
        }
        else if(order==2)
        {
            burger();
        }
        else if(order==3)
        {
            biryani();
        }
        else
        {
            cout<<"No match. Please select from the menu"<<endl;
            menu();
        }

    }
    void pizza()
    {
        int toppings, psize, quantity, gst;
        string pizza1="Peri Peri", pizza2="Cheesy Burst Pizza", pizza3="Paneer Pizza", pizza4="Chicken Pizza";
        system("CLS");
        cout<<"----------------"<<endl;
        cout<<"     TOPPINGS"<<endl;
        cout<<"----------------"<<endl;
        cout<<endl<<"1."<<pizza1<<endl<<"2."<<pizza2<<endl<<"3."<<pizza3<<endl<<"4."<<pizza4<<endl;
        cout<<"Please enter your choice of toppings:";
        cin>>toppings;
        if(toppings>=1 && toppings<=4)
        {
            cout<<"----------------"<<endl;
            cout<<"     SIZE"<<endl;
            cout<<"----------------"<<endl;
            cout<<endl<<"1.Small Rs.100"<<endl<<"2.Medium Rs.150"<<endl<<"3.Large Rs.200"<<endl;
            cout<<"Please select the size:";
            cin>>psize;
        }
        if(psize>=1&& psize<=3)
        {
            system("CLS");
           cout<<"Enter the quantity:";
           cin>>quantity;
        }
        switch(psize)
        {
        case 1:
            gst=5*quantity;
            bill= (100*quantity)+gst;
            break;
        case 2:
            gst=7*quantity;
            bill= 150*quantity+gst;
            break;
        case 3:
            gst=10*quantity;
            bill= 200*quantity+gst;
            break;
        default:
            cout<<"------ERROR------"<<endl;
            cout<<"No match found. Please choose again"<<endl;
            menu();
            break;

        }
        system("CLS");
        cout<<endl<<"--------------------"<<endl;
        cout<<"Bill and Your Order"<<endl;
        cout<<"--------------------"<<endl;
        switch(toppings)
        {
        case 1:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Pizza"<<"          "<<"GST"<<"       "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"      "<<pizza1<<"       "<<"5%="<<gst<<"         "<<bill;
            break;
        case 2:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"     "<<"Pizza"<<"                "<<"GST"<<"      "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"    "<<pizza2<<"        "<<"5%="<<gst<<"        "<<bill;
            break;
        case 3:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"    "<<"Pizza"<<"                "<<"GST"<<"       "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"      "<<pizza3<<"           "<<"5%="<<gst<<"       "<<bill;
            break;
        case 4:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Price("<<pizza4<<")"<<"    "<<"GST"<<"      "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"          "<<"200"<<"                 "<<"5%="<<gst<<"       "<<bill;
            break;
        default:
                cout<<"No match found. Please try again"<<endl;
                menu();
                break;
        }
        oagain();
    }

    void burger()
    {
        int order,bill, quantity, gst;
        string orderagain, bur1="Chicken Burger", bur2="Veg. Aloo Tikki Burger", bur3="Deep Fried Burger";
        cout<<endl<<"1."<<bur1<<" (Rs.200)"<<endl<<"2."<<bur2<<" (Rs.100)"<<endl<<"3."<<bur3<<" (Rs.150)"<<endl;
        cout<<"Please enter your choice:";
        cin>>order;
        if(order>=1&& order<=3)
        {
            cout<<"Enter the quantity:";
            cin>>quantity;
        }
        switch(order)
        {
        case 1:
            gst=10*quantity;
            bill=200*quantity+gst;
            break;
        case 2:
            gst=5*quantity;
            bill=100*quantity+gst;
            break;
        case 3:
            gst=7*quantity;
            bill=150* quantity+gst;
            break;
        default:
            cout<<"------ERROR------"<<endl;
            cout<<"No match found. Please try again"<<endl;
            menu();
            break;
        }
        cout<<endl<<"--------------------"<<endl;
        cout<<"Bill and Your Order"<<endl;
        cout<<"--------------------"<<endl;
        switch(order)
        {
        case 1:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Price("<<bur1<<")"<<"      "<<"GST"<<"    "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"          "<<"200"<<"                    "<<"5%="<<gst<<"           "<<bill;
            break;
        case 2:
           cout<<"-----------------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Price("<<bur2<<")"<<"      "<<"GST"<<"      "<<"Total bill"<<endl;
            cout<<"-----------------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"          "<<"100"<<"                            "<<"5%="<<gst<<"           "<<bill;
            break;
        case 3:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Price("<<bur3<<")"<<"    "<<"GST"<<"      "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"          "<<"150"<<"                     "<<"5%="<<gst<<"          "<<bill;
            break;
        default:
            cout<<"No match found. Please try again"<<endl;
            menu();
            break;
        }
        oagain();
    }
    void biryani()
    {
        int order, bill, quantity, gst;
        string orderagain, bir1="Chicken Biryani", bir2="Veg. Biryani", bir3="Lucknowi Biryani";
        cout<<endl<<"1."<<bir1<<" (Rs.220)"<<endl<<"2."<<bir2<<" (Rs.190)"<<endl<<"3."<<bir3<<" (Rs.250)"<<endl;
        cout<<"Please enter your choice:";
        cin>>order;
        if(order>=1&& order<=3)
        {
            cout<<"Enter the quantity:";
            cin>>quantity;
        }
        switch(order)
        {
        case 1:
            gst=11*quantity;
            bill=220*quantity+gst;
            break;
        case 2:
            gst=9*quantity;
            bill=190*quantity+gst;
            break;
        case 3:
            gst=12*quantity;
            bill=250*quantity+gst;
            break;
        default:
            cout<<"No match found. Please try again."<<endl;
            menu();
            break;

        }
        cout<<endl<<"--------------------"<<endl;
        cout<<"Bill and Your Order"<<endl;
        cout<<"--------------------"<<endl;
        switch(order)
        {
        case 1:
             cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Price("<<bir1<<")"<<"      "<<"GST"<<"    "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"          "<<"220"<<"                    "<<"5%="<<gst<<"           "<<bill;
            break;
        case 2:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Price("<<bir2<<")"<<"      "<<"GST"<<"    "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"          "<<"190"<<"                   "<<"5%="<<gst<<"        "<<bill;
            break;
        case 3:
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"Quantity "<<"   "<<"Price("<<bir3<<")"<<"      "<<"GST"<<"    "<<"Total bill"<<endl;
            cout<<"-------------------------------------------------------------"<<endl;
            cout<<"    "<<quantity<<"          "<<"250"<<"                      "<<"5%="<<gst<<"      "<<bill;
            break;
        default:
            cout<<"------ERROR------"<<endl;
            cout<<"No match found. Please try again"<<endl;
            menu();
            break;
        }
       oagain();
    }
      void oagain()
        {
        string alogin;
        cout<<endl<<"Would you like to order again."<<endl<<"Enter Y for yes and N for no:";
        cin>>orderagain;
        if(orderagain=="Y" || orderagain=="y")
        {
            menu();
        }
        else if(orderagain=="N" || orderagain=="n")
        {
            cout<<"Your order is successfully completed. Thank you"<<endl<<endl;
            asignedup();
        }
        else
        {
            cout<<"No match found. Please try again"<<endl;
            oagain();
        }
        }
};
int main()
{
        food obj;
        obj.asignedup();
        return 0;
}
