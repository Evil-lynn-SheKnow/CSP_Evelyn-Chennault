//Evelyn Chennault, Time Notes C
#include <stdio.h>
#include <time.h>

int main(void){
    time_t seconds;
    seconds = time(NULL);
    printf("Seocnds since January 1, 1970 = %d\n", seconds);

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
    printf("%d\n", hour);

    return 0;
}