#include <stdio.h>

char name[] = "Evelyn";
int age = 15;
float pi = 15.25;

int main(void){
    printf("Hello I am %s. I am %d years old. I am exactly %f years old.\n", name, age, pi);
    printf("%d\n", age);
    printf("%f\n", pi);
    return 0;
}