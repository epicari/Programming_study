#ifndef __CAR_H_
#define __CAR_H_

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

#endif