#include <iostream>
#include "Rectangle.h"
using namespace std;

/*
bool Rectangle::InitMembers(const Point &ul, const Point &lr){
    if(ul.GetX() > lr.GetX() || ul.GetY() > lr.GetY()){
        cout << "Out of bounds" << endl;
        return false;
    }
    upLeft = ul;
    lowRight = lr;
    return true;
}
*/
//멤버 이니셜라이저
//객체 upLeft와 lowRight의 생성과정에서 인자로 전달받은 생성자를 호출
Rectangle::Rectangle(const int &x1, const int &y1, const int &x2, const int &y2)
    :upLeft(x1, y1), lowRight(x2, y2) { /* 비어있음 */ }

void Rectangle::ShowRecInfo() const{
    cout << "Left TOP: " << "[" << upLeft.GetX() << ", ";
    cout << upLeft.GetY() << "]" << endl;
    cout << "Right BOUTTON" << "[" << lowRight.GetX() << ", ";
    cout << lowRight.GetY() << "]" << endl;
}