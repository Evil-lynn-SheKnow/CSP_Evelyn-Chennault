//Evelyn Chennault, Old Enough C
#include <stdio.h>
#include <string.h>

int main(void){
    int num;
    printf("This prgram will tell you if you can vote, get a permit, dirve, and go to school.");
    printf("Please type your age here:\n");
    scanf("%d", &num);
    //Can you vote?
    if(num <= 5){
        printf("No");
    }else if(num <= 6 && num >= 17){
        printf("No");
    }else if(num >= 18){
        printf("Yes");
    }
    //Can you get a learner's permit?
    if(num <= 14){
        printf("No");
    }else if(num <= 15 && num >= 17){
        printf("Yes");
    }else if(num >= 18){
        printf("Yes");
    }
    //Can you drive?
    if(num <= 14){
        printf("No");
    }else if(num <= 15 && num >= 17){
        printf("Yes");
    }else if(num >= 18){
        printf("Yes");
    }

    //Can you attend school?
    if(num <= 5){
        printf("No");
    }else if(num <= 6 && num >= 17){
        printf("Yes");
    }else if(num >= 18){
        printf("Yes");
    }
    
        return 0;
    }