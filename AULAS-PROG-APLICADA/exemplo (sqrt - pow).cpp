#include <iostream>
#include <cmath> 

using namespace std;


int main(){
	double num1, num2;
	
	cout << "Digite o primeiro numero: ";
	cin >> num1;
	
	cout << "Digite o segundo numero; ";
	cin >> num2;
	
	double raiz1 = sqrt(num1);
	double raiz2 = sqrt(num2);
	
	double potencia = pow(num1, num2);
	
	cout << "A raiz quadrada de " << num1 << " é: " << raiz1 << endl;
	cout << "A raiz quadrada de " << num2 << " é: " << raiz2 << endl;
	cout << num1 << " elevado a " << num2 << " é: " << potencia << endl;
}
	

