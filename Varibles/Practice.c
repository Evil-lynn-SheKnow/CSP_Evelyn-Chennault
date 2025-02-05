// Evelyn Chennault, Practice C
#include <stdio.h>

char name;
int age;
char school;
char subject;
int periods;
int year;
int days;
char eyes;
char color;
char food;

int main(void){
    printf("Welcome, what is your name: \n");
    scanf("%s", &name);

    printf("How old are you: \n");
    scanf("%d", &age);

    printf("What school do you attend: \n");
    scanf("%s", &school);

    printf("What is your favorite class: \n");
    scanf("%s", &subject);

    printf("How many classes do you have: \n");
    scanf("%d", &periods);

    printf("The year is: \n");
    scanf("%d", &year);

    printf("How many days are in a year: \n");
    scanf("%d", &days);

    printf("What color are your eyes: \n");
    scanf("%s", &eyes);

    printf("What is your favorite color: \n");
    scanf("%s", &color);

    printf("What did you eat for breakfast: \n");
    scanf("%s", &food);


    printf("Hello I am %s. I am %d years old.\n", name, age);
    printf("I go to %s. My favorite class is %s. I have %d class periods.\n", school, subject, periods);
    printf("The year is %d. There are %d days in a year.\n", year, days);
    printf("My eyes are %s. My favorite color is %s.\n", eyes, color);
    printf("I ate %s.\n", food);
   //
   
    return 0;
}