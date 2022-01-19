#include <stdio.h>

int main( void )
{
    printf("%s", "Would you like me to increment or decrement?\n1. ++\n2. --\n");

    unsigned int initSelect;
    scanf("%d", &initSelect);
    int number;

    if (initSelect == 1) {
        puts("Please enter a number.");
        scanf("%d", &number);
        number++;
        printf("Ta-Da! Your number is now %d!\n", number);
    }

    else if (initSelect == 2) {
	    puts("Please enter a number.");
	    scanf("%d", &number);
	    number--;
	    printf("Ta-Da! Your number is now %d!\n", number);
    }

    else {
	puts("Invalid Input. Run the program again.");
    }
}
