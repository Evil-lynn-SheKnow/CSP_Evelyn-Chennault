#include <stdio.h>

char name[] = "Evelyn";
int age;
float pi;

int main(void){
    printf("Welcome, what ius your name: \n");
    scanf("%s");
    printf("How old ar you: \n")
    scanf("%d", &age);
    printf("Write as much of pi as you know: \n");
    scanf("%f", &pi)
    printf("Hello I am %s. I am %d years old. I am exactly %f years old.\n", name, age, pi);
   //
   
    return 0;
}