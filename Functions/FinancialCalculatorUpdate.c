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

float question(char subject[50]){
    float amount;
    printf("What is your %s\n", subject);
    scanf("%f", &amount);
    return amount;
}

void calculations(float amount, float income, char subject[50]){
    int percent = amount/income*100;
    printf("Your %s is $%.2f, which is %d percent of your income.\n", subject, amount, percent);
}

int main(void){

    //tells user what the program does
    printf("Hello! I am a financial calculator. Let's begin! \n");
    printf("I will ask you several questions. Please answer them in terms of US dollars. \n");

    //user will fill out in order for the calculator to get the variables
    income = question("income?");
    rent = question("rent?");
    utilities = question("utilities?");
    groceries = question("groceries?");
    transportation = question("transportation?");


    calculations(rent, income, "income");
    calculations(utilities, income, "income");
    calculations(groceries, income, "income");
    calculations(transportation, income, "income");
    
    float savings = income*.1;
    float spendings = income-rent-utilities-groceries-transportation-savings;

    printf("Your savings are 10 percent of your income is $%f.\n", savings);
    printf("You have $%f left.\n", spendings);

    //ending
    printf("Thank you and have a good day! I hope we meet again.");
    return 0;
}
