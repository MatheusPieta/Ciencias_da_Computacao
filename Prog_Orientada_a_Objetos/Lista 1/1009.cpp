#include <iostream>
 
using namespace std;
 
int main() {
    
    char n;
    double s, v, r;

    scanf("%s %lf %lf", &n, &s, &v);

    r = s + (v*0.15);

    printf("TOTAL = R$ %.2f\n", r);
    
 
    return 0;
}