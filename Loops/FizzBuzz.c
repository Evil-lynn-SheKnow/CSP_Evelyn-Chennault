//Evelyn Chennault, FizzBuzz C
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void){
    int num;
    for(num){
        if(num % 3){
            printf("Fizz");
        }else if(num % 5){
            printf("Buzz");
        }else if (num % 3 && num % 5){
            printf("FizzBuzz");
        }else{
            printf(num);
        }
    return 0;
}