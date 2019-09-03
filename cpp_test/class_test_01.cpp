/*
* 클래스 테스트
*/
#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

class profileClass {
    string name;
    uint16_t age;
public:
    void set_value (string, uint16_t);
    string print_prf() {return cout << name << " " << age << endl;}


}

int main() {
    
    system("pause");
    return 0;
}   