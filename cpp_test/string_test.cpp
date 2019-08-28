#include <iostream>
#include <string>
#include <sstream>

using namespace std;

struct profile_t {
    string name;
    string address;
    uint8_t age;
} profile_l[2];

void print_prf (profile_t prf);

int main () {
    string empty_str;
    
    for (int n = 0; n < 2; n++) {
        cout << "what your name ? ";
        getline (cin, profile_l[n].name);
        cout << "how old are you ? ";
        getline (cin, empty_str);
        stringstream(empty_str) >> profile_l[n].age;
        cout << "what your home address ? ";
        getline (cin, profile_l[n].address);
    }

    cout << "\n your profile is \n";
    for (int n = 0; n < 2; n++) {
        print_prf (profile_l[n]);
    }

    return 0;
}

void print_prf (profile_t prf) {
    cout << "your name is " << prf.name;
    cout << "\n" << prf.age;
    cout << "\n and your home is" << prf.address;
}


