#include<iostream>
using namespace std;

void myFunction(int n);
void myFunction(char c);

int main(){

    myFunction(12);
    myFunction('name');
    return 0;
}

void myFunction(int n){
    cout << n*5 << endl;
}

void myFunction(char c){
    cout << "name: " << c << endl;
}
