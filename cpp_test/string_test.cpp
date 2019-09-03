/* 
* 구조체 테스트
*/
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>

using namespace std;

struct profile_t {
    string name;
    string address;
    uint16_t age;
} profile_l[2];

void print_prf (profile_t prf);

int main () {
    string empty_str;
    
    for (uint8_t n = 0; n < 2; n++) {
        cout << "what your name ? ";
        getline (cin, profile_l[n].name);
        cout << "how old are you ? ";
        getline (cin, empty_str);
        stringstream(empty_str) >> profile_l[n].age;
        cout << "what your home address ? ";
        getline (cin, profile_l[n].address);
    }

    cout << "profile is ";
    for (uint8_t n = 0; n < 2; n++) {
        print_prf (profile_l[n]);
    }

    system("pause"); // cout이 끝나면 종료되는 것을 막음
    return 0;
}

void print_prf (profile_t prf) {
    cout << "\nyour name is " << prf.name << " and " << prf.age << ", your address is " << prf.address << endl; 
}


