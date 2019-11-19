/*
* 멤버변수를 private으로 선언하고, 해당 변수에 접근하는 함수를 별도로 정의해서, 안전한 형태로 멤버 변수의 접근을
* 유도하는 것이 바로 '정보은닉'
*/

#ifndef __POINT_H_
#define __POINT_H_

class Point{
    private:
        int x, y;

    public:
    //bool InitMembers(int xpos, int ypos);
    Point(const int &xpos, const int &ypos); //생성자
    int GetX() const;
    int GetY() const;
    bool SetX(int xpos);
    bool SetY(int ypos);
};

#endif