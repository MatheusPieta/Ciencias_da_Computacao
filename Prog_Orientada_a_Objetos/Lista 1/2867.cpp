#include <iostream>
#include <math.h>

using namespace std;

 int main(){
    int cases;
    int base;
    int exponent;
    int helper;
    cin >> cases;
    for (helper = 0; helper < cases; helper++){
        cin >> base;
        cin >> exponent;
        cout << int(exponent * log10(base)) + 1 << endl;
    }
    return 0;
 }