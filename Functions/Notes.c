//Evelyn Chennault, Functions Notes C
#include <stdio.h>

//int num;
//char name[50], place[50], verb[50];

//void add(int numOne, int numTwo){
    //return numOne+numTwo;
//}

void due(char assignment[50], char day[20]){
    printf("The %s assignment is due %s.", assignment, day);
}


int main(void){
    //printf("Please tell me a number:\n");
    //scanf("%d", num);
    //add(num,10);
    //add(1,8);
    //printf (add(72,5));
    due("Functions Notes", "Today");
    due("Hello World Update", "Tomorrow");
    due("Functions Notes", "Friday");
    return 0;
}