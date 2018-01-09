#include <iostream>

//CODE
int add(int a, int b){//#1
	return a + b;
}

int subtract(int a, int b){
	return a - b;
}

//DATA
int global_x = 10;//#2

int main(void) {
	//STACK
	int local_x = 20;//#3

	//HEAP
	int * heap_x = (int*)malloc(sizeof(int));//#4
	*heap_x = 30;
	free(heap_x);//#5

	return 0;
}