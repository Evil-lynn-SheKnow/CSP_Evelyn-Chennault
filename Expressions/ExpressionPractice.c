//Evelyn Chennault, Expressions Practice C
#include <stdio.h>
#include <math.h>

double a = 2;
double b = 3;
double c = 4;
double d = 5;

int main(void){

    // 7-24/8*4+6
    printf(7-24/8*4+6);
    // 18/3-7+2*5
    printf(18/3-7+2*5);
    // 6*4/12+72/8-9
    printf(6*4/12+72/8-9);
    // (17-6/2)+4*3
    printf((17-6/2)+4*3);
    // 2*(1*4-2/2)+(6+2-3)
    printf(-2*(1*4-2/2)+(6+2-3));
    // 1*((3-4*7)/5)-2*24/6
    prinf(-1*((3-4*7)/5)-2*24/6);
    // (3*5**2/15)-(5-2**2)
    printf((3*pow(a,5)/15)-(5-pow(a,2)));
    // (1**4*2**2+3**3)-2**5/4
    printf((pow(c,1)*pow(a,2)+pow(b,3))*pow(d,-2)/4);
    // (22/2-2*5)**2+(4-6/6)**2
    printf((22/2-2*5), pow(a,22/2-2*5)+(4-6/6), pow(a, 4-6/6));

    return 0;
}