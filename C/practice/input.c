#include<stdio.h>

int main()
{	
	int character; /* declares an integer named character */
	printf("\n\n\n\n\nI'm here to test if the programmer understands variables!\nInput a number, and, if I've had a competent coder,\nI'll display your number!\nPut your number here: ");
	scanf ("%d", &character ); /* Tells scanf to scan for an integer (%d), then store this integer in the character variable (&character)*/
	printf( "Your number was %d!\n\n\n\n", character ); /* %d declares the integer, and character scans the contents of the variable, giving the integer previously declared. */
	getchar();
	return 0;
}
