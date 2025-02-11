// Evelyn Chennault, Notes C
#include <stdio.h>

char subject[50];

int main(void){
    //printf("What class are you in?\n");
    //scanf("%s", subject);
    fgets(subject, sizeof(subject), stdin);
    printf("You are in %s, that is a cool class.");
    return 0;
}