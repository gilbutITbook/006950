#include <iostream>
#include <string>
using namespace std;

class Account{
public://#1
	//생성자 : 파이썬 클래스의 __init__()과 같다
	Account(string name, int money){
		user = name;
		balance = money;
	}
	//인스턴스 메서드(멤버 함수)
	int get_balance() {
		return balance;
	}
	//인스턴스 메서드(멤버 함수)
	void set_balance(int money) {
		if (money < 0) {
			return;
		}

		balance = money;
	}

private://#2
	//인스턴스 멤버(멤버 변수)
	string user;
	int balance;//#3
};

int main(void){
	Account my_acnt("greg", 5000);

	//my_acnt.balance;//#4

	my_acnt.set_balance(-3000); // #5

	cout << my_acnt.get_balance() << endl;

	return 0;
}