# main.py

from datetime import date

# # Funciona direto desde que o modulosepacotes esteja na mesma
# # pasta que o script
# from modulosepacotes.bibliotecacontas.titulares.titular import Titular

# Se não tiver, é necessário o import e adição do sys.path
import sys
import os

module_path = os.path.abspath('modulosepacotes')
sys.path.append(module_path) # append no final da lista
# sys.path.insert(0, module_path) # insere na posição 0

from modulosepacotes.bibliotecacontas.titulares.titular import Titular
from modulosepacotes.bibliotecacontas.contas.contacorrente import ContaCorrente

def run():
    dt_nasc = date(year=1991, month=8, day=6)
    t1 = Titular('Pedro', 'Engenheiro de dados', dt_nasc)
    print(t1.nome_titular)
    print(t1.cpf)
    print(t1.data_nascimento)
    
    print(t1._nome)
    print(t1._cpf)
    print(t1._dt_nasc)
    
    t1.nome_titular = 'Marcos'
    print(t1.nome_titular)
    print(t1._nome)

    cc1 = ContaCorrente(t1, '001', 'c101')
    cc1.deposito(180.50) # nesse ponto eu estou informando que o depósito vai ser feito para a cc1
    print(cc1.saldo)
    cc1.saque(100)
    print(cc1.saldo)
    cc1.pagamento(80.0)
    print(cc1.saldo)

    cc1.extrato()

    dt_nasc = date(year=1991, month=8, day=6)
    t2 = Titular('Luana', 'Engenheira de dados', dt_nasc)
    print(t2.nome_titular)
    print(t2.cpf)
    print(t2.data_nascimento)

    cc2 = ContaCorrente(t2, '001', 'c202')
    print(cc2.agencia)
    print(cc2.conta)
    print(cc2.saldo)
    print(cc2.titular.nome_titular)
    print(cc2.titular.cpf)
    print(cc2.titular.data_nascimento)

    cc1.saque(100)
    cc1.pagamento(100)
    cc1.transferencia(100, cc2)
    cc1.deposito(100)
    print(cc1.saldo)
    cc1.transferencia(100, cc2)
    print(cc1.saldo)
    print(cc2.saldo)

    print()

    cc1.extrato()

    print()

    cc2.extrato()

if __name__ == "__main__":
    run()