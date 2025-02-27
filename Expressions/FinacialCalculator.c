//Evelyn Chennault, Finacial Calculator C
#include <stdio.h>

int main(void){
    //tells user what the program does
    printf("Hello! I am a finacial calculator. Let's begin! ");
    printf("I will ask you several questions. Please answer them in terms of US dollars. ");

    //questions for the user to fill out in order for the calculator to get the varibles
    float round(income);
    printf("What is your income?\n");
    scanf("%f", &income);
    float round(rent);
    printf("What is your rent?\n");
    scanf("%f", &rent);
    float utilities;
    printf("How much do you spend on utilities?\n");
    scanf("%f", &utilities);
    float groceries;
    printf("How much do you spend on groceries?\n");
    scanf("%f", &groceries);
    float transportation;
    printf("How much do you spend on transportation?\n");
    scanf("%f", &transportation);
    float savings;
    printf("How much is in your savings account?\n");
    scanf("%f", &savings);
    
    //ten percent of income
    float incomePercent = income*.1;
    //money left over after spendings and current savings
    float spendings = income-rent-utilities-groceries-transportation-savings;
    //math equations that are needed to calculate the percentages
    float rentPercent = rent/income*100;
    //calculate percent income of utilites (utilites/income*100) (varible)
    float utilitesPercent = utilities/income*100;
    //calculate percent income of groceries (groceries/income*100) (varible)
    float groceriesPercent = groceries/income*100;
    //calculate percent income of transportation (transportation/income*100) (varible)
    float transportationPercent = transportation/income*100;
    //calculate percent income of spending (savings/income*100) (varible)
    float savingsPercent = savings/income*100;
    //calculate percent income of spending (spendings/income*100) (varible)
    float spendingsPercent = spendings/income*100;

    //all final calculations
    printf("%f is 10 percent of your income.", incomePercent);
    printf("Your rent is %f, which is %f of your income.", income, rentPercent);
    printf("Your spendings on utilities is %f, which is %f of your income.", utilities, utilitesPercent);
    printf("Your spendings on groceries is %f, which is %f of your income.", groceries, groceriesPercent);
    printf("Your spendings on transportation is %f, which is %f of your income.", transportation, transportationPercent);
    printf("You spend %f dollars monthly.", spendings);
    
    //ending
    printf("Thank you and have a good day! I hope we meet again.");
    return 0;
}
