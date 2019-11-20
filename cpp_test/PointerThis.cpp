#include <iostream>
#include <cstring>
using namespace std;

class SoSimple {

private:
    int num;

public:
    SoSimple(int n) : num(n) { //num(n) == num=n 
        cout << "num= " << num << endl;
        cout << "address=" << this << endl;
    }
    void ShowSimpleData() {
        cout << num << endl;
    }
    SoSimple * GetThisPointer() { // 이 함수를 실행하는 객체의 포인터를 반환하라는 의미
        return this; 
    }
};

int main() {
    SoSimple sim1(100);
    SoSimple * ptr1 = sim1.GetThisPointer(); // 포인터를 반환하므로 SoSimple형 포인터 변수에 저장해야 함
    cout << ptr1 << ", "; // ptr1에 저장된 주소 값을 출력
    ptr1->ShowSimpleData(); // ptr1이 가리키는 객체의 함수를 호출함

    SoSimple sim2(200);
    SoSimple * ptr2 = sim2.GetThisPointer();
    cout << ptr2 << ", ";
    ptr2->ShowSimpleData();

    return 0;
}