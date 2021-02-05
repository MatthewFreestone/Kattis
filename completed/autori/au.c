#include<stdio.h>
#include<string.h>
int main(int argc, char const *argv[])
{
	char name[128];
	scanf("%s", name);
	for(int i = 0; i < strlen(name); i++){
		if (name[i] >= 'A' && name[i] <= 'Z'){
			printf("%c", name[i]);
		}
	}

}
