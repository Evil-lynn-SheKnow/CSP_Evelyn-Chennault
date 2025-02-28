//Evelyn Chennault, Time Notes C
#include <stdio.h>
#include <time.h>

int main(void){
    //Current time  
    time_t rawtime;  
    struct tm * timeinfo;  
    time(&rawtime);  
    timeinfo = localtime(&rawtime);  
    printf("Current time and date is %s\n", asctime(timeinfo));
    //Current hour  
    time_t now = time(NULL);  
    //now = time(NULL); //same thing  
    struct tm * tm_struct = localtime(&now);  
    int hour = tm_struct->tm_hour; //military time  
    printf("In military time, the time is %d.", hour);
    //Greet user based off of hour
    if(hour == 6 || hour == 7 || hour == 8 || hour == 9 || hour == 10 || hour == 11){
        printf("Good morning!");
    }else if(hour == 12 || hour == 13 || hour == 14 || hour == 15 || hour == 16){
        printf("Good afternoon!");
    }else if(hour == 17 || hour == 18 || hour == 19 || hour == 20 || hour == 21 || hour == 22){
        printf("Good evening!");
    }else if(hour == 23 || hour == 0 || hour == 1 || hour == 2 || hour == 3 || hour == 4 || hour == 5){
        printf("Good night!");
    }

return 0;  

}