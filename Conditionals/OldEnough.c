//Evelyn Chennault, Old Enough C
#include <stdio.h>

int num[20];

int main(void){
    printf("Hello! I will determine if you can drive!");
    printf("Please type your age here:\n");
    scanf("%d", &num);
    if(num <= 14){
        printf("Being %d years old makes you too young to drive.\n", num);
    }else if(num == 15 || num == 16 || num == 17){
        printf("You are %d. That is old enough to drive! Yay!\n", num);
    }else if(num >= 18){
        printf("You are %d. You should be able to drive. If you don't have a license, take the test!\n", num);
    }
        return 0;
    }