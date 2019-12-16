/* C Test 
* 포인터를 참조 호출로 전달하여 함수가 포인터를 변경할 수 있도록 함
* 이름의 길이가 DB나 사용자로부터 입력되기 전까지 얼만지 모름
* 따라서 함수가 필요한만큼 메모리를 할당해서 할당한 번지를 리턴
* 함수는 동적으로 메모리를 할당하여 할당된 번지를 *pName에 대입
* *pName == *Name 이므로 Name에 메모리를 할당 후 값을 넣고 반환
* 2중 포인터를 안 쓸 경우, pName는 지역변수가 되므로 Name와 무관해짐
* int inputName(char *pName) { pName = (char *)malloc(12) }
* 함수에서 char *형의 인수 Name을 변경할 수 있도록 하려면 char *의 포인터인
* char **형을 넘겨야 하고 함수 내에선 *pName으로 실인수를 참조해야 하는 것
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int inputName(char **pName){
    *pName = (char *)malloc(12);
    strcpy(*pName, "Cabin");
}

int main() {

    char* Name;

    inputName(&Name);
    printf("이름은 %s입니다.\n", Name);
    free(Name);
    system("pause");
    
    return 0;
}
