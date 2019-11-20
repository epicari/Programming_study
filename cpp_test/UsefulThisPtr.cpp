#include <iostream>
using namespace std;

class TwoNumber {

private:
    int num1;
    int num2;

public:
    TwoNumber(int num1, int num2) {
        this->num1 = num1;
        this->num2 = num2;
    }
    void ShowTowNumber() {
        cout << this->num1 << endl; //this포인터를 사용함으로써, 멤버변수에 접근함을 명확히 함
        cout << num2 << endl; //하지만 일반적으로 생략해서 표현함
    }
};

int main() {
    TwoNumber two(2, 4);
    two.ShowTowNumber();
    return 0;
}