#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int* p;

    if (find(begin(arr), end(arr), 1) != end(arr)) {
        cout << "It exists" << endl;
    } else {
        cout << "It does`t exist" << endl;
    }

    p = find(arr, arr + 4, 4);
    if (p != arr + 4){
        cout << "found in arr: " << *p << endl;
    } else {
        cout << "not found in arr" << endl;
    }

    return 0;
}