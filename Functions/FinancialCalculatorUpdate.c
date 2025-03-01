//Evelyn Chennault, Financial Calculator C
#include <stdio.h>
#include <math.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float rentPercent;
float utilitiesPercent;
float groceriesPercent;
float transportationPercent;

void question(char subject){
    printf("What is your", subject);
}

void calculations(float subject){
    printf(subject/income*100);
}

void results(char subject, char percent){
    printf("Your %s is %s percent of your income.", subject, percent);
}

int main(void){

    //tells user what the program does
    printf("Hello! I am a financial calculator. Let's begin! ");
    printf("I will ask you several questions. Please answer them in terms of US dollars. ");

    //user will fill out in order for the calculator to get the variables
    printf("What is your income?\n");
    scanf("%f", &income);
    printf("What is your rent?\n");
    scanf("%f", &rent);
    printf("How much do you spend on utilities?\n");
    scanf("%f", &utilities);
    printf("How much do you spend on groceries?\n");
    scanf("%f", &groceries);
    printf("How much do you spend on transportation?\n");
    scanf("%f", &transportation);

    float incomePercent = income*.1;

    calculations(rentPercent subject);
    calculations(utilitiesPercent);
    calculations(groceriesPercent);
    calculations(transportationPercent);

    float savings = income*.1;
    float spendings = income-rent-utilities-groceries-transportation-savings;


    //all final calculations
    results(rent, rentPercent);
    results(utilities, utilitiesPercent);
    results(groceries, groceriesPercent);
    results(transportation, transportationPercent);
    results(utilities, utilitiesPercent);


    printf("%f is 10 percent of your income.", incomePercent);
    printf("You spend %f dollars monthly.", spendings);
    printf("Your savings are 10 percent of your income, which is %f dollars.", savings);
    
    //ending
    printf("Thank you and have a good day! I hope we meet again.");
    return 0;
}
