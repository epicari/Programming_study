#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    // Complete this function 
    int tmp = *a;
    *a += *b;
    *b = abs(tmp-*b);
}

void update2(int **c) {
    *c += 10;
}

int main() {
    int a, b;
    int *c;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    scanf("%d", &c);
    update2(&c);
    printf("%d", c);

    return 0;
}