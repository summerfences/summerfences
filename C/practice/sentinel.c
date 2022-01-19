/* Test to assess my comprehension of using sentinel-controlled iteration 
 * Frank T Passantino, 2018 AD */
#include <stdio.h>

int main ( void ) // Main begins program execution
{
    int sentinel; // Initialize the sentinel
    puts("I can add as many float numbers as you'd like!");
    puts("Enter your first number, or enter -1 to end input.");
 
    float number; // initialize the float variable number
    scanf("%f", &number);

    float total = 0; // initialize the total, and assign 0 to it
    while (number != -1) { // while the sentinel is not entered
	total = total + number;
	puts("Enter another number, or enter -1 to end input.");
	scanf("%f", &number);
    }
    if (number = -1) {
	sentinel = -1;
    }

    if (sentinel = -1) {
	printf("Your added total was %f!\n", total);
    }
}

