#include <stdio.h>

int main ( void )
{
    int number;
    int number2;

    puts("This program multiplies a number by itself the minimum");
    printf("%s","amount of time to get a larger-than-four digit number.\nType Here: ");

    scanf("%d", &number);
    
    if (number == 1 ) {
	puts("Invalid Input.");
        }

    else if (number != 1) {
           while (number < 1000 ) { 
		number = number  * number;
    		}
	   printf( "The first non-quad-digit self multiplied product of your number is %d.\n", number);
    }
}
