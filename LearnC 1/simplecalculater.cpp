#include<iostream>
using namespace std;
int main() {
    int a,b,c,d;
    cout<<"Simple Calculater";
    cout<<"\nEnter First Number: ";
    cin>>a;
    cout<<"\nEnter Second Number: ";
    cin>>b;
    cout<<"\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n\nEnter Your Choice(1/2/3/4): ";
    cin>>c;
    switch (c)
    {
        case 1:
            d=a+b;
            cout<<"\nSum of "<<a<<" and "<<b<<" is ="<<d;
            break;
        case 2:
            if(b==0)
                cout<<"\nError! Division by Zero is not allowed.";
            else
            d=a-b;
            cout<<"\nDifference between "<<a<<" and "<<b<<" is= "<<d;
            break;
        case 3:
            d=a*b;
            cout<<"\nProduct of "<<a<<" and "<<b<<" is ="<<d;
            break;
        case 4:
            if(b==0)
            cout<<"\nError! Division by Zero is not allowed.";
            else
            d=a/b;
            cout<<"\nDivision of "<<a<<" and "<<b<<" is= "<<d;
            break;
        default :cout<<"\nWrong choice entered.";
    }
}