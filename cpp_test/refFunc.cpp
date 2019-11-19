#include<iostream>

using namespace std;

void cby(int num1, int num2){
    int temp = num1;
    num1 = num2;
    num2 = temp;
} // Call-by-value

void cbr(int* num1, int* num2){
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
} // Call-by-reference 1

void cbrByref(int &ref1, int &ref2){
    int temp = ref1;
    ref1 = ref2;
    ref2 = temp;
} // Call-by-reference 2
/* 참조자를 이용해 값수정을 원치 않을 경우 const 사용
* cbrByref(const int &ref1, const int &ref2)
*/

int main(){
    int num1 = 10;
    int num2 = 50;
    int num3 = 20;
    int num4 = 30;

    cout << "Orgin num1: " << num1 << "  " << "Orgin num2: " << num2 << endl;

    cby(num1, num2);
    cout << "cby num1: " << num1 << "  " << "cby num2: " << num2 << endl;
    
    cbr(&num1, &num2);
    cout << "cbr num1: " << num1 << "  " << "cbr num2: " << num2 << endl;

    cout << "Orgin num3: " << num3 << "  " << "Orgin num4: " << num4 << endl;

    cbrByref(num3, num4);
    cout << "cbrByref num3: " << num3 << "  " << "cbrByref num4: " << num4 << endl;

    return 0;
}