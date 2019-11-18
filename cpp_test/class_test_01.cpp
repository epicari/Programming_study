/*
* 클래스 테스트
*/
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>

using namespace std;

class proFileClass {

private:
    string name;
    int age;

public:
    proFileClass(string n, int i) { //생성자
        name = n;
        age = i;
    }
    void printProfile() {
        cout << "name: " << name << endl;
        cout << "age: " << age << endl;
    }
};

void main() {
    proFileClass aProfile('CHOI', 30);
    aProfile.printProfile();
    system("pause");
}   