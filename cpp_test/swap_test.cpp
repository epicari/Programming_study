#include <iostream>

using namespace std;

int main(){
    int arrNum[4] = {3, 4, 6, 5};
    int i, j, temp;
    int N = 4;

    for(i = 0; i < N; i++){
        for (j = 0; j < N - (i+1); j++){
            if (arrNum[j] > arrNum[j+1]){
                temp = arrNum[j+1];
                arrNum[j+1] = arrNum[j];
                arrNum[j] = temp;
            }
        }
        cout << arrNum[i] << endl;
    }

    return 0;
}