//Evelyn Chennault, Old Enough C
#include <stdio.h>

int main(void){
    int num;
    printf("Please type your age here:\n");
    scanf("%d", &num);
    printf("Can you legally vote in the USA?"); //Can you vote?
    if(num <= 5){
        printf("Being %d years old makes you too young to vote.\n", num);
    }else if(num == 6 || num == 7 || num == 8 || num == 9 || num == 10 || num == 11 || num == 12 || num == 13 || num == 14 || num == 15 || num == 16 || num == 17){
        printf("You are %d. That is still too young to vote...sorry...\n", num);
    }else if(num >= 18){
        printf("You are %d. You can vote! Just know to be smart about it!\n", num);
    }
    printf("Can you drive?"); //Can you get a learner's permit?
    if(num <= 14){
        printf("Being %d years old makes you too young to even touch the steering wheel.\n", num);
    }else if(num == 15 || num == 16 || num == 17){
        printf("You are %d. You can get your permit!\n", num);
    }else if(num >= 18){
        printf("You are %d. You should've exceeded the time and you should have your license!\n", num);
    }
    printf("Can you drive?"); //Can you drive?
    if(num <= 14){
        printf("Being %d years old makes you too young to drive.\n", num);
    }else if(num == 15 || num == 16 || num == 17){
        printf("You are %d. That is old enough to drive! Yay!\n", num);
    }else if(num >= 18){
        printf("You are %d. You should be able to drive. If you don't have a license, take the test!\n", num);
    }
    printf("Can you go to school?"); //Can you attend school?
    if(num <= 5){
        printf("Being %d years old makes you too young to go to school.\n", num);
    }else if(num == 6 || num == 7 || num == 8 || num == 9 || num == 10 || num == 11 || num == 12 || num == 13 || num == 14 || num == 15 || num == 16 || num == 17){
        printf("You are %d. That is old enough to attend school! Yay!\n", num);
    }else if(num >= 18){
        printf("You are %d. You should have gradutated from high school and had at least one degree from college. Make sure you have a job, too!\n", num);
    }
    
        return 0;
    }