/*
* 할당 이후, 복사 생성자를 통한 초기화
*
*/

#include <iostream>
using namespace std;

class SoSimple {

private:
    int num;

public:
    SoSimple(int n) : num(n) {}

    SoSimple(const SoSimple& copy) : num(copy.num) {
        cout << "Called COPY SoSimple" << endl;
    }
    SoSimple& AddNum(int n) {
        cout << "Called AddNum" << endl;
        num += n;
        return *this; //이 함수를 사용한 객체 자신을 반환함, 하지만 반환형이 참조형이니, 참조 값이 반환 됨
    }

    void ShowData() {
        cout << "num: " << num << endl;
    }
};

/*
* void SimpleFuncObj(SoSimple ob) {
*   ob.ShowData();
* }
*/

SoSimple SimpleFuncObj(SoSimple ob) {
    cout << "Before The return" << endl;
    return ob; //리턴도 임시 메모리공간 할당받고 데이터 저장함 데이터는 ob, 따라서 임시객체(return)의 복사 생성자 호출
}

int main() {
    SoSimple obj(7);
    //cout << "Before The call" << endl;
    //SimpleFuncObj(obj); //객체 obj를 인자로 전달하므로 void SimpleFunObj(SoSimple ob)에서 선언된 매게변수 ob의 복사 생성자가 호출됨
    //cout << "After The call" << endl;
    SimpleFuncObj(obj).AddNum(30).ShowData(); //SimpleFunObj 함수가 반환한 객체(임시객체)를 대상으로 AddNum 함수를 호출하고, AddNum 함수가 반환하는 참조 값을 대상으로 ShowData 함수를 호출함
    obj.ShowData();

    return 0;
}