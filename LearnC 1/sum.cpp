#include<iostream>
using namespace std;
//int sum(int a,int b);

int sum(int a,int b){
    int c=a+b;
    return c;
}



int main(){
    int num1,num2;
    cout<<"Enter the first number: "<<endl;
    cin>>num1;
    cout<<"Enter the second number: "<<endl;
    cin>>num2;
    cout<<sum(num1,num2);

    return 0;
}

