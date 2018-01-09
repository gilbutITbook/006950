#include <iostream>
using namespace std;

int test(int a, int b);

int main(void)
{
	int a = 10, b = 5;//#4
	int res = test(a, b);//#5
	cout << "result of test : " << res << endl;
	return 0;
}

int test(int a, int b)//#1
{
	int c = a + b;//#2
	int d = a - b;//#3
	return c + d;
}
