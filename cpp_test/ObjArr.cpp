/*
* 배열선언 이후에 각각의 요소를 원하는 값으로 초기화시키려면 일일이 초기화의 과정을 별도로 거쳐야 함
*
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
    Person parr[3];
    char namestr[100];
    char * strptr;
    int age;
    int len;

    for(int i = 0; i < 3; i++) {
        cout << "Name: ";
        cin >> namestr;
        cout << "Age: ";
        cin >> age;
        len = strlen(namestr)+1;
        strptr = new char[len];
        strcpy(strptr, namestr);
        parr[i].SetPersonInfo(strptr, age);
    }

    parr[0].ShowPersonInfo();
    parr[1].ShowPersonInfo();
    parr[2].ShowPersonInfo();

    return 0;
}