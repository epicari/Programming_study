#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int x,y,z;

    string a[11] = {"even", "odd", "one", "two", "three", "four", "five",
                    "six", "seven", "eight", "nine"};    
    
    cin >> x >> y;

    for (z = x; z <= y; z++) {
        if((z > 9) && (z%2 == 0)) {
            cout << a[0] << endl;
        }
        else if((z > 9) && (z&2 != 0)) {
            cout << a[1] << endl;
        }
        else {
            cout << a[z+1] << endl;
        }
    }
    return 0;
}