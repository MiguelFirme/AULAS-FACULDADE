#include <iostream>
using namespace std;

class contaBancaria {
private:
    double saldo;
    int senha;

public:
    string nome;

    void depositar() {
        double deposito;
        int Pedisenha;

        cout << "Valor do deposito: " << endl;
        cin >> deposito;
        cout << "Insira sua senha: " << endl;
        cin >> Pedisenha;

        if (Pedisenha == senha) {
            saldo += deposito;
            cout << "Deposito realizado com sucesso. Novo saldo: " << saldo << endl;
        } else {
            cout << "Senha incorreta." << endl;
        }
    }

    void sacar() {
        double saque;
        int Pedisenha;

        cout << "Valor do saque: " << endl;
        cin >> saque;
        cout << "Insira sua senha: " << endl;
        cin >> Pedisenha;

        if (Pedisenha == senha) {
            if (saque <= saldo) {
                saldo -= saque;
                cout << "Saque realizado com sucesso. Novo saldo: " << saldo << endl;
            } else {
                cout << "Saldo insuficiente." << endl;
            }
        } else {
            cout << "Senha incorreta." << endl;
        }
    }

    void exibirSaldo() {
        int Pedisenha;
        cout << "Insira sua senha: " << endl;
        cin >> Pedisenha;

        if (Pedisenha == senha) {
            cout << "Saldo atual: " << saldo << endl;
        } else {
            cout << "Senha incorreta." << endl;
        }
    }

    void setsenha(int senha) {
        this->senha = senha;
    }

    void setsaldo(double saldo) {
        this->saldo = saldo;
    }
};

int main() {
    contaBancaria contaBancaria01;
    contaBancaria01.nome = "Miguel";
    contaBancaria01.setsenha(1234);
    contaBancaria01.setsaldo(2500);

    int op = 0;

    cout << "1-Depositar" << endl;
    cout << "2-Sacar" << endl;
    cout << "3-Exibir saldo" << endl;
    cout << "Qual das operacoes deseja realizar: " << endl;
    cin >> op;

    switch (op) {
    case 1:
        contaBancaria01.depositar();
        break;
    
	case 2:
        contaBancaria01.sacar();
        break;
    
	case 3:
        contaBancaria01.exibirSaldo();
        break;
    
	default:
        cout << "Operacao invalida." << endl;
    }

    return 0;
}
