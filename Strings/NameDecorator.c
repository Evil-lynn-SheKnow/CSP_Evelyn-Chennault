// Evelyn Chennault, Name Decorator C
#include <stdio.h>
#include <string.h>

char one[3] = ">>-";
char two[3] = "-->";
char name[50];


int main(void){
    printf("This is the name decorator.\n");
    printf("Please type in your name:\n");
    scanf("%s", (name));
    strcat(one, name);
    strcat(two)

    return 0;
}