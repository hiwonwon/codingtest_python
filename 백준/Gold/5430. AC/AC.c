#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define FUNCTION_COUNT_MAX 100001
#define ARRAY_NUMBER_MAX 300000	

int startPointer;
int endPointer;

int* inputData(int *n, char *p, char *xi){
	scanf("%s", p);
	scanf("%d", n);
	scanf("%s", xi);
	
	int *returnData = (int*)malloc(sizeof(int) * (*n));
	int dataPointer = 0;
	char *token = strtok(xi, ",");
	
	while(token != NULL){
		int i, digits = 1;
		returnData[dataPointer] = 0;
		
		for(i = strlen(token) - 1; i >= 0; i--){
			if(token[i] == '[' || token[i] == ']') continue;
			returnData[dataPointer] += digits * (token[i] - '0');
			digits *= 10;
		}
		
		dataPointer++;
		token = strtok(NULL, ",");
	}
	
	return returnData;
}

int executionFunction(int n, char *p, int *dataArray){
	startPointer = 0;
	endPointer = n - 1;
	bool isForward = true;
	
	int i;
	
	for(i = 0; p[i] != '\0'; i++){
		
		switch(p[i]){
			case 'R':
				isForward = !isForward;
				break;
			case 'D':
				if(endPointer < startPointer) return -1;
				if(isForward) startPointer++;
				else endPointer--;
				break;
		}
	}
	
	return isForward;
}

void print(int mod, int *dataArray){
	
	if(mod == -1) printf("error\n");	
	else if(startPointer > endPointer) printf("[]\n");	
	else{
		int i;
		printf("[");
		
		if(mod) for(i = startPointer; i < endPointer; i++) printf("%d,",dataArray[i]);
		else for(i = endPointer; i > startPointer; i--) printf("%d,",dataArray[i]);
		
		printf("%d]\n",dataArray[i]);
	} 
}

int main(void){
	int T, n;
	char p[FUNCTION_COUNT_MAX];
	char xi[ARRAY_NUMBER_MAX];
	
	scanf("%d", &T);
	
	while(T > 0){
		int *dataArray = inputData(&n, p, xi);
		int mod = executionFunction(n, p, dataArray);
		print(mod, dataArray);
		
		free(dataArray);
		T--;
	}
	
	return 0;
}