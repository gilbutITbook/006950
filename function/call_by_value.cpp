#include <iostream>
using namespace std;

void change_value(int x, int value)//#1
{
	x = value; //#2
	cout << "x : " << x << " in change_value" << endl;
}

int main(void)
{
	int x = 10;//#3
	change_value(x, 20);//#4
	cout << "x : " << x << " in main" << endl;

	return 0;
}
