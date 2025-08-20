#include <iostream>

using namespace std;

void imprimirMensagem(string mensagem = "Ola mundo!", int repeticoes = 1) {
	for(int i = 0; i < repeticoes; ++i) {
		cout << mensagem << endl;
	}
}

int main() {
	
	imprimirMensagem();
	
	imprimirMensagem("Bem vindo ao c++");
	
	imprimirMensagem("C++ é poderoso!", 3);
	
	return 0;
}
