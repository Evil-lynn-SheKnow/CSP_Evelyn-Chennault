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

float question(char subject){
    float amount;
    printf("What is your", subject);
    scanf("%f", &amount);
    return amount;
}

void calculations(float amount, float income, char subject){
    int percent = amount/income*100;
    printf("Your %s is $%.2f, which is %d percent of your income.", subject, amount, percent);
}

int main(void){

    //tells user what the program does
    printf("Hello! I am a financial calculator. Let's begin! ");
    printf("I will ask you several questions. Please answer them in terms of US dollars. ");

    //user will fill out in order for the calculator to get the variables
    income = question("income?");
    rent = question("rent?");
    utilities = question("utilities?");
    groceries = question("groceries?");
    transportation = question("transportation?");

    float incomePercent = income*.1;

    calculations(rent, income, "income");
    calculations(utilities, income, "income");
    calculations(groceries, income, "income");
    calculations(transportation, income, "income");
    
    float incomePercent = income*.1;
    float spendings = income-rent-utilities-groceries-transportation-incomePercent;


    printf("%f is 10 percent of your income.", incomePercent);
    printf("Your savings are 10 percent of your income is $%f.", incomePercent);
    printf("You have $%f left.", spendings);

    //ending
    printf("Thank you and have a good day! I hope we meet again.");
    return 0;
}
