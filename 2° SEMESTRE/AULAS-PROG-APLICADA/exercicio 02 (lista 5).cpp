#include <iostream>
using namespace std;

// Fun��o que retorna "N" se o n�mero for menor que 0 e "P" caso 
char verificarNumero(int numero) {
    if (numero < 0) {
        return 'N';  // Retorna 'N' se o n�mero for menor que 0
    } else {
        return 'P';  // Retorna 'P' se o n�mero for maior ou igual a 0
    }
}

int main() {
    int numero;
    
    cout << "Digite um numero: ";
    cin >> numero;
    
    // Chama a fun��o e armazena o resultado
    char resultado = verificarNumero(numero);
    
    // Imprime o resultado retornado pela fun��o
    cout << resultado << endl;
    
    return 0;
}

