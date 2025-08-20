#include <iostream>
using namespace std;

// Função que retorna "N" se o número for menor que 0 e "P" caso 
char verificarNumero(int numero) {
    if (numero < 0) {
        return 'N';  // Retorna 'N' se o número for menor que 0
    } else {
        return 'P';  // Retorna 'P' se o número for maior ou igual a 0
    }
}

int main() {
    int numero;
    
    cout << "Digite um numero: ";
    cin >> numero;
    
    // Chama a função e armazena o resultado
    char resultado = verificarNumero(numero);
    
    // Imprime o resultado retornado pela função
    cout << resultado << endl;
    
    return 0;
}

