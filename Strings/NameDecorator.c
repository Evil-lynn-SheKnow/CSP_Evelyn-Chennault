// Evelyn Chennault, Name Decorator C
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){
    char name[50];
    printf("This is the name decorator.\n");
    printf("Please type in your name:\n");
    scanf("%s", toupper(name));
    printf(">>-%s-->\n", name);
   
    return 0;
}