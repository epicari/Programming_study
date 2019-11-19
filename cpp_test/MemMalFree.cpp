#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

char* MakeStrAdr(int len){
    char* str = (char*)malloc(sizeof(char)*len);
    return str;
}
/*
* 할당할 대상의 정보를 무조건 바이트 크기단위로 전달해야 함
* 반환형이 void형 포인터이기 때문에 적절한 형 변환을 거쳐야 함
*/

char* MakeStrAdrCpp(int len){
    char* str2 = new char[len];
    return str2;
} // cpp는 malloc 대신 new, free 대신 delete 사용

int main(){
    char* str = MakeStrAdr(20);
    char* str2 = MakeStrAdrCpp(20);
    strcpy(str, "Hello World! ");
    cout << str << endl;
    strcpy(str2, "I`m so happy~ ");
    cout << str2 << endl;
    free(str);
    delete []str;
    
    return 0;
}