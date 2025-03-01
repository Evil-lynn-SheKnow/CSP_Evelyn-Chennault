//Evelyn Chennault, Hello World Update C
#include <stdio.h>

void hello(char greet[50], char name[50]){
    printf("%s %s", greet, name);
}

int main(void){
        hello("Here's a shiny,", "Lily!\n");
        hello("Keep on drawing,", "Kate!\n");
        hello("Live, laugh, and love on,", "Emma!\n");
        hello("Enjoy the ducks,", "Quackers!\n");
        hello("Stay the wild card,", "Seraphim!\n");
        hello("Rock that hair,", "Gracie!\n");
        hello("Daydream every day,", "Evelyn!");
        return 0;
}