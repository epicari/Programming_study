#include <iostream>
 
using namespace std;
 
class parent {
public :
    virtual void v_print() {
        cout << "parent" << "\n";
    }
    void print() {
        cout << "parent" << "\n";
    }
};
 
class child : public parent {
public :
    void v_print() {
        cout << "child" << "\n";
    }
    void print() {
        cout << "child" << "\n";
    }
};
 
int main() {
    parent* p;
    child c;
    p = &c;
 
    p->v_print(); //포인터가 가르키고 있는 객체에 대한 함수 호출
    p->print();
 
    return 0;
}