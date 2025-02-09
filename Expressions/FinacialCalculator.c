// Evelyn Chennault, Finacial Calculator C
#include <stdio.h>

// tells user what the program does
printf("Hello! I am a finacial calculator. Let's begin!");
printf("I will ask you several questions. Please answer them in terms of US dollars.");

// questions for the user to fill out in order for the calculator to get the varibles
float income = printf("What is your income? \n");
float rent = printf("What is your rent? \n");
float utilities = printf("How much do you spend on utilities? \n");
float groceries = printf("How much do you spend on groceries? \n");
float transportation = printf("How much do you spend on transportation? \n");
float savings = printf("How much is in your savings account? \n");
float spendings = printf("How much are you usually spending? \n");

// ten percent of income
float incomePercent = (income*.1);
// money left over after spendings and current savings
float leftOverMoney = (income-rent-utilities-groceries-transportation-savings-spendings);

// math equations that are needed to calculate the percentages
float rentPerent = ((rent/income)*100);
// calculate percent income of utilites (utilites/income*100) (varible)
float utilitesPercent = ((utilites/income)*100);
// calculate percent income of groceries (groceries/income*100) (varible)
float groceriesPercent = ((groceries/income)*100);
// calculate percent income of transportation (transportation/income*100) (varible)
float transportationPercent = ((transportation/income)*100);
// calculate percent income of spending (savings/income*100) (varible)
float savingsPercent = ((savings/income)*100);
// calculate percent income of spending (spendings/income*100) (varible)
float spendingsPercent = ((spending/income)*100);

int main(void){
    // all final calculations
    printf("%f is 10 percent of your income.\n", incomePercent);
    printf("Your rent is %f, which is %f of your income.\n", income, rentPercent);
    printf("Your spendings on utilities is %f, which is %f of your income.\n", utilities, utilitesPercent);
    printf("Your spendings on groceries is %f, which is %f of your income.\n", groceries, groceriesPercent);
    printf("Your spendings on transportation is %f, which is %f of your income.\n", transportation, transportationPercent);
    printf("You have %f dollars left for other uses.\n", leftOverMoney);

    return 0;
}

printf("Thank you and have a good day! I hope we meet again.")