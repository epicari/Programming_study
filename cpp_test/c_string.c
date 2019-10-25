#include <stdio.h>

#define DUBAE(a) a+a //매크로 함수
#define JEGOP(a) ((a)*(a)) //기계적으로 치환하므로 괄호로 감싸야 함

void countTest(){
    static int countNum = 0; //countNum 값이 프로그램 종료 시 까지 살아있음
    countNum++;
    printf("The count: %d\n", countNum);
}

int main(){
    int i;
    int price[] = {100, 500, 300, 200, 700};

    printf("Dubae %d\n", DUBAE(3));
    printf("Jegop %d\n", JEGOP(2+3));
    
    for(i=0; i<2; i++) {
        countTest();
    }

    for(i=0; i<sizeof(price)/sizeof(price[0]);i++){ //배열의 크기가 달라져도 루프의 범위 자동적용
        printf("Price: %d\n", price[i]);
    }
    return 0;
}