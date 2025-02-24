// Evelyn Chennault, Silly Sentences C
#include <stdio.h>
#include <string.h>

//empty string varibles for user words (minimum 3)
char noun[];
char nounTwo[];
char verb[];


int main(void){
    //What the program is
    printf("This is a MadLib program.\nTo begin, you just answer the question with a single word. ");
    printf("Please type in a PLACE:\n");
    scanf("%s", noun);
    printf("Type in a verb:\n");
    scanf("%s", verb);
    printf("Type in another noun:\n");
    scanf("%s", nounTwo);
    printf("Type in a object:\n");
    //Print madlib
    printf("I was in my %s when my %s had %s me over to his room.", noun, verb, nounTwo);
    return 0;
}