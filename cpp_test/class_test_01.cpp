/*
* 클래스 테스트
*/
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>

using namespace std;

class profileClass {
    string name;
    uint16_t age;
public:
    ostringstream oss;
    void set_value (string, uint16_t);
    string print_prf() {return oss << name << " " << age << endl;}


};

int main() {
    
    system("pause");
    return 0;
}   