//Evelyn Chennault, Family Loop 
#include <stdio.h>
#include <string.h>


int main(void){
    char family[][50] = {"Russell", "Kristin", "Violet", "Steven"};
    int mlength = sizeof(family)/sizeof(family[0]);
    int i;
    for(i = 0;i < mlength; i++){
        printf("Hello, %s\n", family[i]);
    }
    return 0;
}