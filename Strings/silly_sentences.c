// Evelyn Chennault, Silly Sentences C
#include <stdio.h>
#include <string.h>

//empty string varibles for user words (minimum 3)
char place;
char place2;
char person;
char verb;
char verb2;
char object;
char object2;
char emotion;

int main(void){
    //What the program is
    printf("This is a MadLib program.\nTo begin, you just answer the question with a single word. ");
    printf("Please type in a noun:\n");
    scanf("%s", &place);
    printf("Type in another noun:\n");
    scanf("%s", &place2);
    printf("Type in a person's name:\n");
    scanf("%s", &person);
    printf("Type in a verb:\n");
    scanf("%s", &verb);
    printf("Type in a object:\n");
    scanf("%s", &object);
    printf("Type in another object:\n");
    scanf("%s", &object2);
    printf("Type in a emotion:\n");
    scanf("%s", &emotion);
    printf("I was in my %s when my %s had %s me over to his room.", place, person, verb);
    printf("I when into my %s's room and he said to help him %s John, our cousin.", person, verb2);
    printf("Me and my %s got the %s and the %s. We went to the %s next door and %s the room. My brother was not %s.", person, object, object2, place2, emotion);

    return 0;
}