/* C Test 
*
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
