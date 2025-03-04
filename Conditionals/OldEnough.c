//Evelyn Chennault, Old Enough C
#include <stdio.h>
#include <string.h>

int main(void){
    int num;
    printf("This prgram will tell you if you can vote, get a permit, dirve, and go to school.");
    printf("Please type your age here:\n");
    scanf("%d", &num);
    if(num <= 5 && num >= 11){
        printf("You can not vote, get a learners permit, or drive, but you can go to school.");
    }else if(num >= 12 && num <= 14){
        printf("You can not vote or drive, but you can get a learners permit and go to school.");
    }else if (num >= 15 && num <= 17){
        printf("You can not vote, but you can get a learners permit, drive and go to school.");
    }else if(num >= 18){
        printf("You can  vote, get a learners permit, drive and go to school.");
    }
}