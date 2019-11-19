/*
* 클래스 테스트
* public 어디서든 접근허용
* protected 상속관계에 놓여있을 때, 유도 클래스에서의 접근허용
* private 클래스 내서만 접근허용
*/
#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

namespace CAR_CONST{
    enum{
        ID_LEN=20, MAX_SPD=200, FUEL_STEP=2,
        ACC_STEP=10, BRK_STEP=10
    }; //열거형 enum을 통해 구조체 내에서만 유효한 상수 정의
}

class Car{
    private:
        char gamerID[CAR_CONST::ID_LEN];
        int fuelGauge;
        int curSpeed;
    // 함수의 원형선언을 클래스 내부에 미리 선언하여 정보 파악에 도움
    public:
        void InitMembers(char* ID, int fuel);
        void ShowCarState();
        void Accel();
        void Break();
};

void Car::InitMembers(char* ID, int fuel){
    strcpy(gamerID, ID);
    fuelGauge = fuel;
    curSpeed = 0;
}

void Car::ShowCarState(){
    cout << "ID: " << gamerID << endl;
    cout << "Gauge: " << fuelGauge << "%" << endl;
    cout << "Speed: " << curSpeed << "km/s" << endl;
}

void Car::Accel(){
    if(fuelGauge <= 0)
        return;
    else
        fuelGauge -= CAR_CONST::FUEL_STEP;
    
    if((curSpeed + CAR_CONST::ACC_STEP) >= CAR_CONST::MAX_SPD){
        curSpeed = CAR_CONST::MAX_SPD;
        return;
    }
    curSpeed += CAR_CONST::ACC_STEP;
}

void Car::Break(){
    if(curSpeed < CAR_CONST::BRK_STEP){
        curSpeed = 0;
        return;
    }

    curSpeed -= CAR_CONST::BRK_STEP;
}

int main(){
    Car run99;
    run99.InitMembers("run99", 100);
    run99.Accel();
    run99.Accel();
    run99.ShowCarState();
    run99.Break();
    run99.ShowCarState();

    system("pause");
    return 0;
}