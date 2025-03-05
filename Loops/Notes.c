//Evelyn Chennault, Loops Notes C
#include <stdio.h>


int main(void){
    //1. What is a loop? 
        //a section of code repeated multiple times


    //2. What are the two types of loops?
        //while loops
    int start = 0;
    while(start < 5){
        printf("Hello!\n");
        start++;
    }
        //for loops
    int q;
    for(q=0; q<5; q++){
        printf("%d\n", q);
    }


    //3. What is iteration
        //reapeating something with minor changes each time


    //4. What are arrays (lists)?
        //a varible holding multiple values


    //8. How do you make arrays in C?
        //arrays all need to be the same data type
        //1. set the data type
        //2. AFTER naming, put brackets and write the length of the array
        //3. array is surrounded by culry brackets
        //4. commas "," between each item
    int grades[] = {88, 97, 100, 70, 72, 99, 61};
        //print a single int, char, or float
    printf("CSP Grade: %d\n", grades[2]);
        //change item in the array
    grades[2] = 95;
    printf("CSP Grade: %d\n", grades[2]);
        //size of array in bytes
    int size = sizeof(grades);
        //length in items
    int length = sizeof(grades)/sizeof(grades[0]);
    printf("The array is %d items long.\n", length);
        //array of strings
        //forst brackets sets the length of the array
        //second brackets sets length of each string
    char movies[][20] = {"Car", "Treasure Pleanet", "An American Tale", "Marley & Me", "The Avengers"};
    printf("The movie is %s!\n", movies[1]);
    int mlength = sizeof(movies)/sizeof(movies[0]);


    //9. How do you make for loops in C?
        //set the iterator, keeps track of time going through the loop (best practice: use "i" or "x")
    int x;
        //"(starting point; ending point, count by)"
    for(x = 0; x <= 10;x+=2){
        printf("%d\n", x);
    }
    int m;
    for(m = 0;m < mlength; m++){
        printf("%s\n", movies[m]);
    }


    //10. How do you make while loops in C?
    int w = 100; //start

    while(w >= 0){ //stop
        printf("%d\n", w); //count by
        w -= 10;
    }


    return 0;
}