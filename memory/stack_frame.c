#include <stdio.h>

int adder(int a, int b, int n) {
	int c = a * n;
	int d = b * n;
	int e = c + d;
	return e;
}
 
int main(void) {
	int a = 10;
	int b = 20;
	int n = 2;
	int res = adder(a, b, n);
	return 0;
}

