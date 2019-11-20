/*
* 객체 포인터 배열
* : 객체의 주소 값 저장이 가능한 포인터 변수로 이뤄진 배열
*/

#include<iostream>
#include<cstring>
using namespace std;

class Person {

private:
    char * name;
    int age;

public:
    Person(char * myname, int myage) {
        int len = strlen(myname)+1;
        name = new char[len];
        strcpy(name, myname); //myname 내용을 name으로 복사
        age = myage;
        cout << "called Person constructor" << endl;
    }
    Person() { //배열 생성시 필요한 생성자
        name = NULL;
        age = 0;
        cout << "called Person()" << endl;
    }
    void SetPersonInfo(char * myname, int myage) { //원하는 데이터로의 초기화를 목적
        name = myname;
        age = myage;
    }
    void ShowPersonInfo() const {
        cout <<"Name: " << name << ", ";
        cout << "Age: " << age << endl;
    }
    ~Person() {
        delete []name;
        cout << "called destructor!" << endl;
    }
};

int main() {
    Person * parr[3];
    char namestr[100];
    int age;

    for(int i=0; i<3; i++) {
        cout << "Name: ";
        cin >> namestr;
        cout << "Age: ";
        cin >> age;
        parr[i] = new Person(namestr, age); // 객체를 생성해서, 이 객체의 주소 값을 배열에 저장
    }

    parr[0]->ShowPersonInfo();
    parr[1]->ShowPersonInfo();
    parr[2]->ShowPersonInfo();
    delete parr[0];
    delete parr[1];
    delete parr[2];

    return 0;
}