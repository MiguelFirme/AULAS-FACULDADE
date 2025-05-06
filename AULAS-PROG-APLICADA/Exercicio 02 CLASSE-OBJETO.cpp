#include <iostream>
using namespace std;

class Retangulo {
private:
    float altura;
    float largura;

public:

    Retangulo(float a, float l) : altura(a), largura(l) {}

 
    float area() {
        return altura * largura;
    }

 
    float perimetro() {
        return 2 * (altura + largura);
    }

   
    void exibirArea() {
        cout << "A �rea do ret�ngulo �: " << area() << endl;
    }

 
    void exibirPerimetro() {
        cout << "O per�metro do ret�ngulo �: " << perimetro() << endl;
    }
};

int main() {
    int op;
    float n1, n2;

    cout << "Digite a altura: " << endl;
    cin >> n1;
    cout << "Digite a largura: " << endl;
    cin >> n2;
    cout << "Escolha a opera��o 1- �rea 2- Per�metro: " << endl;
    cin >> op;

    Retangulo retangulo01(n1, n2);

    switch(op) {
        case 1:
            retangulo01.exibirArea();
            break;
        case 2:
            retangulo01.exibirPerimetro();
            break;
        default:
            cout << "Op��o inv�lida!" << endl;
            break;
    }

    return 0;
}

