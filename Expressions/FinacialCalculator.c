//Evelyn Chennault, Financial Calculator C
#include <stdio.h>

int main(void){
    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;

    //tells user what the program does
    printf("Hello! I am a financial calculator. Let's begin! ");
    printf("I will ask you several questions. Please answer them in terms of US dollars. ");

    //questions for the user to fill out in order for the calculator to get the variables
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
    float rentPercent = rent/income*100;
    float utilitiesPercent = utilities/income*100;
    float groceriesPercent = groceries/income*100;
    float transportationPercent = transportation/income*100;
    float savings = income*.1;
    float spendings = income-rent-utilities-groceries-transportation-savings;


    //all final calculations
    printf("%f is 10 percent of your income.", incomePercent);
    printf("Your rent is %f, which is %f of your income.", income, rentPercent);
    printf("Your spendings on utilities is %f, which is %f of your income.", utilities, utilitiesPercent);
    printf("Your spendings on groceries is %f, which is %f of your income.", groceries, groceriesPercent);
    printf("Your spendings on transportation is %f, which is %f of your income.", transportation, transportationPercent);
    printf("You spend %f dollars monthly.", spendings);
    printf("Your savings are 10% of your income, which is %f dollars.", savings);
    
    //ending
    printf("Thank you and have a good day! I hope we meet again.");
    return 0;
}
