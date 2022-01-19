/*Coded in text-only mode in vi*/
#include<stdio.h> /* include the main library that includes printf, scanf, etc */

int main() /* Begin the program's code */
{
	int taffy; /* Declares an integer with the name taffy */
	printf("\n\n\n\n\n\nPlease select a number for me to\nstore into a variable named Taffy.\n\n\nKindly enter your number:"); /* Prints message to user */
	scanf("%d" , &taffy );/* uses scanf to search for an integer and store it to taffy */
	printf("\n\n\nTaffy reads %d!\n\n\n\n\n\n", taffy); /* declare to the user their integer by using printf to declare an integer based on what is stored in taffy */
	return 0; /* Report the all-clear */
}
