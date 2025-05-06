#include <iostream>
using namespace std;


class cidade{

public:
	string nome;
	string dataFundacao;
	int numeroHabit;
	int numeroEleit;
	
	void exibirInfo(){
		cout << "Nome da cidade: " << nome << endl;
		cout << "Data de fundação: " << dataFundacao << endl;
		cout << "Numero de Habitantes: " << numeroHabit << endl;
		cout << "Numero de eleitores: " << numeroEleit << endl;
	}
};
	
	
	int main(){
		string n1, n2;
		int n3, n4;
		
		cout << "Digite o nome da cidade: ";
		cin >> n1;
		cout <<"Digite a data de fundação: ";
		cin >> n2;
		cout << "Digite a quantidade de habitantes: ";
		cin >> n3;
		cout << "Digite a quantidade de eleitores: ";
		cin >> n4;
		
		class cidade minhaCidade;
		 minhaCidade.nome = n1;
		 minhaCidade.dataFundacao = n2;
		 minhaCidade.numeroHabit = n3;
		 minhaCidade.numeroEleit = n4;
		 
		 minhaCidade.exibirInfo();
		
	}
	
	
