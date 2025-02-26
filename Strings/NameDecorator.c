// Evelyn Chennault, Name Decorator C
#include <stdio.h>
#include <string.h>

char one[15] = ">>-";
char two[15] = "-->";
char three[15] = " ";
char name[50];


int main(void){
    printf("This is the name decorator.\n");
    printf("Please type in your name:\n");
    scanf("%s", (name));
    printf("%s", strcat(one, name));
    printf("%s", strcat(two, three));

    return 0;
}