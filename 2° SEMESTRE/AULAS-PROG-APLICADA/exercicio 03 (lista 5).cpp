#include <iostream>
using namespace std;

bool cres(int a, int b, int c){
	return ( a <= b && b <= c);
}

int main(){
	
	int num1, num2, num3;
	
	cout << "Digite o primeiro numero: ";
	cin >> num1;
	cout << "Digite o primeiro numero: ";
	cin >> num2;
	cout << "Digite o primeiro numero: ";
	cin >> num3;
	
	bool result = cres(num1, num2, num3);
	
	if (result){
		cout << "Os numeros estao ordenados de forma crescente!" << endl;
	}
	else {
	cout << "Os numeros NAO estao ordenados de forma crescente!" << endl;
}

return 0; }
