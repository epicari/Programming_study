#include <iostream>
#include "Rectangle.h"
using namespace std;

bool Rectangle::InitMembers(const Point &ul, const Point &lr){
    if(ul.GetX() > lr.GetX() || ul.GetY() > lr.GetY()){
        cout << "Out of bounds" << endl;
        return false;
    }
    upLeft = ul;
    lowRight = lr;
    return true;
}

void Rectangle::ShowRecInfo() const{
    cout << "Left TOP: " << "[" << upLeft.GetX() << ", ";
    cout << upLeft.GetY() << "]" << endl;
    cout << "Right BOUTTON" << "[" << lowRight.GetX() << ", ";
    cout << lowRight.GetY() << "]" << endl;
}