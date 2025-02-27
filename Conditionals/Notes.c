//Evelyn Chennault, Conditional Notes C
#include <stdio.h>
#include <string.h> //Needed tp compare strings

char name[10] = "Evelyn";
int num[20];

int main(void){
    //10. How do I you write an if statement in C?
    if(strcmp(name, "Evelyn") == 0){ //strcmp means string comparisson whne the outcome is 0, the stings are the same.
        printf("Hello, Evelyn Chennault! Welcome to CSP!");
    //11. How do you write else statements in C?
    }else{
        printf("Hello, %s. Welcome to CSP!\n", name);

        return 0;
    }}


//12. How do you write elif statements in C?
int main(void){
    printf("How many siblings do you have?\n");
    scanf("%d", &num);
    if(num == 0){
        printf("You are an only child.");
    }else if(num <= 2){
        printf("You have a couple siblings.");
    }else if(num <= 5){
        printf("You have a few siblings.");
    }else if(num <= 8){
        printf("You have a TON of siblings. Dang!");
    
    return 0;
}}


//13. What are the three logical operators in C?
// && = and
// || = or
// ! = not
int main(void){
    if(num == 7 || num == 13){
        printf("%d is an unlucky number.\n", num);
    }else if(num < 10 && num > 5){
        printf("%d is a large number.\n", num);
    }else if((!num > 10)){
        printf("You typed in %d.\n", num);
    }else if(num == 12){
        printf("You have a dozen siblings.\n", num);
    }

        return 0;
    }