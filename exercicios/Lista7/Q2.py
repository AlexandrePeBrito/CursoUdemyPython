""" 2. Crie uma classe Agenda que pode armazenar 10 pessoas e seja capas de realizar as
seguintes operações:
    * void armazenaPessoa(String nome, int idade, float altura);
    * void removePessoa(String nome);
    * int buscaPessoa(String nome);  informa em que posição da agenda está a
pessoa
    * void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
    * void imprimePessoa(int index); // imprime os dados da pessoa que está na
posição “i” da agenda. """

class Agenda():
    contador=0
    __nome=[]
    __altura=[]
    __idade=[]
     
    def armazenaPessoa(self,nome,idade,altura):
        if Agenda.contador<=10:
            Agenda.__nome.append(nome)
            Agenda.__idade.append(idade)
            Agenda.__altura.append(altura)
            Agenda.contador+=1
        else:
            print("Agenda Lotada")

    def removePessoa(self,nome):
        if Agenda.contador>0:
            for c in range(0,Agenda.contador):
                if Agenda.__nome[c] == nome:
                    Agenda.__nome.pop(c)
                    Agenda.__idade.pop(c)
                    Agenda.__altura.pop(c)
                    Agenda.contador-=1
                    break
        else:
            print("Agenda Vazia!")

    def buscaPessoa(self,nome):
        if Agenda.contador>0:
            for c in range(0,Agenda.contador):
                if Agenda.__nome[c] == nome:
                    return c
        else:
            print("Agenda Vazia!")

    def imprimeAgenda(self):
        if Agenda.contador>0:
            for c in range(0,Agenda.contador):
                print(f"Nome: {Agenda.__nome[c]}\nIdade: {Agenda.__idade[c]}\nAltura: {Agenda.__altura[c]}\n")
        else:
            print("Agenda Vazia!")

    def imprimiPessoa(self,posicao):
        print(f"Na {posicao} posição temnos\nNome: {Agenda.__nome[posicao-1]}\nIdade: {Agenda.__idade[posicao-1]}\nAltura: {Agenda.__altura[posicao-1]}")


agenda=Agenda()
agenda.armazenaPessoa('Alexandre',28,1.74)
agenda.armazenaPessoa('Maiure',21,1.60)
agenda.armazenaPessoa('Joao',15,1.87)
agenda.imprimeAgenda()
print(agenda.buscaPessoa('Maiure')+1)