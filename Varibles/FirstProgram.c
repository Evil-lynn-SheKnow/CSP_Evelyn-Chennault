// Evelyn Chennault, First Program C
#include <stdio.h>

char name;

int main(void){
    printf("Hello, user.");
    printf("I am the computer program.");
    printf("Welcome, what is your name: \n");
    scanf("%s", &name);

    printf("Hello, %s. I hope you enjoy your time on this computer!\n", name);
    return 0;
}
