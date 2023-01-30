#include<stdio.h>
int main(void){
	int N;
	scanf("%d", &N);

	int remainder = N % 2;
	if (remainder == 0){ //if its even
		printf("Bob");
	}
	else{ //if its odd 
		printf("Alice");
	}
	//printf(" 1 mod 2 is %d", 1%2);
}