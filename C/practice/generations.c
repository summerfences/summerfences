/* Program for determining the generation of the user. v1.0. Copyleft Frank T Passantino, 2018 AD */
#include<stdio.h>

int main( void )
{
	int year; /* Declares an integer variable named "year" */
	printf("\nThis program will determine what generation you belong to.\nPlease enter your birth year: "); /* Prints out question to user */
	scanf ("%d", &year); /* Uses scanf to look for an integer as input, then assigns it to the variable "year" */
	
	/* Boolean logic follows.*/

	if ( year >= 1995 && year <= 2012) { /* Checks to see if 'year' has a value greater than or equal to 1995 and less than or equal to 2012 */
	printf("\nYou are a member of Gen Z.\n");
	}

	else if ( year >= 2013 && year < 2025 ) { /* Checks to see if 'year' has a value greater than or equal to 2013 and less than or equal to 2025 */
	printf("\nYou are a member of Gen Alpha.\n");
	}
	
	else if ( year >= 1985 && year < 1995 ) { /* Checks to see if 'year' has a value greater than or equal to 1985 and less than 1995 */
	printf("\nYou are a member of the Millennials.\n");
	}

	else if ( year >= 1975 && year < 1985 ) { /* Checks to see if 'year' has a value greater than or equal to 1975 and less than 1985 */
	printf("\nYou are a member of the Xennials.\n");
	}

	else if ( year >= 1965 && year < 1975) { /* Checks to see if 'year' has a value greater than or equal to 1965 and less than 1975 */
	printf("\nYou are member of Generation X.\n");
	}

	else if ( year >= 1946 && year < 1965) { /* Checks to see if 'year' has a value greater than or equal to 1946 and less than 1965 */
	printf("\nYou are a Baby Boomer.\n");
	}
	 
	else if ( year >= 1925 && year < 1946) { /* Checks to see if 'year' has a value greater than or equal to 1925 and less than 1946 */
	printf("\nYou are a member of the Silent Generation.\n");
	}

	else if ( year >= 1901 && year < 1925 ) { /* Checks to see if 'year' has a value greater than or equal to 1901 and less than 1925 */
	printf("\nYou are a member of the G.I. Generation.\n");
	}

	else if ( year >= 1883 && year <= 1900 ) { /* Checks to see if 'year' has a value greater than or equal to 1883 and less than or equal to 1900 */
	printf("\nYou would have been a member of the Lost Generation.\nMay you rest in peace.\n"); /* Although the Lost Generation is gone, I felt it respectful to include them, and a message directed towards them. */
	}
	 
	else {	/* Input validation. Every value not applied to a generation returns this. */
	printf("\nOut of range.\n");
	}
	
	printf("Press ENTER to terminate...\n"); /* Uses getchar to accept ENTER as input to terminate program */
	getchar();
	getchar();

	return 0; /* Return the success of program execution. */
}
