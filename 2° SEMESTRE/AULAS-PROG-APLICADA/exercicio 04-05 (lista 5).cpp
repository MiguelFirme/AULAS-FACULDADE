#include <iostream>
using namespace std;


bool validarSaque(double a, double b, double c){
	return (c <= a + b);
}

double sacar ( double a, double b, double s){
	return (a + b - s);
}

int main(){
	
	double num1, num2, num3;
	
	num1 = 1500;
	num2 = 2000;
	cout << "Seu limite: " << num2 << endl;
	cout << "Seu Saldo: " << num1 << endl;
	
	cout << "Digite o valor que deseja sacar: ";
	cin >> num3;
	
	double saldoFinal = sacar(num1, num2, num3);
	bool permitir = validarSaque(num1, num2, num3);
	
	if (permitir) {
		cout << "Seu saldo ficou em: " << saldoFinal << " Reais" << endl;
	}
	else{ cout << "Saldo insuficiente para realizar a operacao!" << endl;
	return 0;
	}
	
	return 0;
}
