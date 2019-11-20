/*
* 복사 생성자
* 디폴트 복사 생성자가 자동으로 삽입되어 특별한 상황이 아닌 이상은 정의 안 해도 됨
* 특별한 상황 = 포인터를 사용하여 메모리 주소를 참고했을 때, 복사와 원본 모두 주소가 같음!
*/

#include <iostream>
using namespace std;

class SoSimple {

private:
    int num1;
    int num2;

public:
    SoSimple(int n1, int n2) : num1(n1), num2(n2) {}

    SoSimple(const SoSimple &copy) : num1(copy.num1), num2(copy.num2) { //복사만 하는 것이므로 원본손상 방지를 위해 const 삽입
        cout << "Called SoSimple(SoSimple &copy)" << endl;
    }

    /*
    * explicit SoSimple(const SoSimple &copy) : num1(copy.num1), num2(copy.num2) {}
    * explicit를 사용함으로써 sim2=sim1은 사용할 수 없고 sim2(sim1)만 사용 가능함
    * 
    * 
    */
    void ShowSimpleData() {
        cout << num1 << endl;
        cout << num2 << endl;
    }
};

int main() {
    SoSimple sim1(15, 30);
    cout << "Init" << endl;
    SoSimple sim2 = sim1; // SoSimple sim2(sim1)로 자동변환
    cout << "End" << endl;
    sim2.ShowSimpleData();

    return 0;
}