/*
* 참조자
* 새로 선언되는 변수의 이름 앞에 등장하면 이는 참조자의 선언
* num1 이라 네임드된 메모리 공간에 num2라는 이름이 하나 더 붙음
* 지역 참조자는 지역변수와 마찬가지로 동작
* 포인터 변수도 참조자 선언 가능함
*/

#include <iostream>

using namespace std;

int main(){
    int num1 = 5;
    int &num2 = num1;

    int *ptr = &num1;
    int **dptr = &ptr;

    int *(&pref) = ptr;
    int **(&dpref) = dptr;

    cout << "num1: " << num1 << endl;
    cout << "pref: " << *pref << endl;
    cout << "dpref: " << **dpref << endl;

    num2 = 10;
    cout << "num2: " << num2 << endl;
    cout << "num1: " << num1 << endl;
    cout << "pref: " << *pref << endl;
    cout << "dpref: " << **dpref << endl;

    return 0;
}