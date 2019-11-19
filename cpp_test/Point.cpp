#include<iostream>
#include "Point.h"
using namespace std;

bool Point::InitMembers(int xpos, int ypos){
    if(xpos < 0 || ypos < 0){
        cout << "Out of bounds" << endl;
        return false;
    }
    x = xpos;
    y = ypos;
    return true;
}
// 엑세스 함수, 멤버변수를 private으로 선언하면서 클래스 외부에서의 멤버변수 접근을 목적으로 정의되는 함수
int Point::GetX() const{ 
    return x;
}

int Point::GetY() const{
    return y;
}

bool Point::SetX(int xpos){
    if(0 > xpos || xpos > 100){
        cout << "Out of bounds" << endl;
        return false;
    }
    x = xpos;
    return true;
}

bool Point::SetY(int ypos){
    if(0 > ypos || ypos > 100){
        cout << "Out of bounds" << endl;
    }
    y = ypos;
    return true;
}
