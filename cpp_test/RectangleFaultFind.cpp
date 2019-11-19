#include<iostream>
#include "Point.h"
#include "Rectangle.h"
using namespace std;

int main(){
/*
    Point pos1;
    if(!pos1.InitMembers(-2, 4))
        cout << "Fail init" << endl;
    if(!pos1.InitMembers(2, 4))
        cout << "Fail init" << endl;

    Point pos2;
    if(!pos2.InitMembers(5, 9))
        cout << "Fail init" << endl;
    
    Rectangle rec;
    if(!rec.InitMembers(pos2, pos1))
        cout << "Fail init" << endl;
    
    if(!rec.InitMembers(pos1, pos2))
        cout << "Fail init" << endl;

    rec.ShowRecInfo();
    return 0;
*/

//생성자 추가로 인한 코드 간결화
    Rectangle rec(1, 1, 5, 5);
    rec.ShowRecInfo();
    return 0;
}