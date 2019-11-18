/* 
*   a` = a+b, b` = |a-b|
*
*/

#include <iostream>

using namespace std;

void update(int *a, int *b){
    int aDot = *a;
    *a += *b;
    *b = abs(aDot - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}