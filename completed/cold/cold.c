#include<stdio.h>
int main(int argc, char const *argv[])
{
	int n;
	int totalUnderZero = 0;
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		int t;
		scanf("%d", &t);
		if (t < 0){
			totalUnderZero++;
		}
	}
	printf("%d", totalUnderZero);
	return 0;
}