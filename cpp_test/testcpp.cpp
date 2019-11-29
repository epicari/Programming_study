#include <iostream>
using namespace std;

class boolclass1 {
public:
    bool voidText(int num) {
        if(num==0)
            return false; // == 0 
        else
            return true;
    }
};

class boolclass2 : public boolclass1 {
public:
    //virtual bool voidText(int num) // 함수이므로 정의 해야 함 ... = 0; 도 안 됨 !

    virtual bool voidText(int num) {
        if(num==0)
            return false; // == 0 
        else
            return true;
    }
};

int main() {
    boolclass2 bc2;
    int num;
    bool testbool;
    cin >> num;
    testbool = bc2.voidText(num);

    cout << testbool << endl;

    return 0;
}