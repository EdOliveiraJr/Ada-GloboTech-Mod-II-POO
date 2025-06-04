from datetime import datetime

class Titular:
  def __init__(self, nome: str, data_nascimento: datetime, cpf: str):
    self._nome : str = nome
    self._data_nascimento : datetime = data_nascimento
    self._cpf : str = cpf

  def __str__(self):
    return f'Nome: {self._nome}, Data de Nascimento: {self._data_nascimento}, CPF: {self._cpf}'

  @property
  def nome(self) -> str:
    return self._nome
  
  @nome.setter
  def nome(self, nome: str) -> None:
    self._nome = nome

  @property
  def data_nascimento(self) -> datetime:
    return self._data_nascimento

  @property
  def cpf(self) -> str:
    return self._cpf

class ContaBancaria :
  def __init__(self, agencia: str, conta: str, titular: Titular):
    self._agencia : str = agencia
    self._conta : str = conta
    self._saldo : float = 0.0
    self._titular : Titular = titular
    self._movimentacao : list = []

  @property
  def agencia(self) -> str:
    return self._agencia
  
  @agencia.setter
  def agencia(self, agencia: str) -> None :
    self._agencia = agencia

  @property
  def conta(self) -> str:
    return self._conta
  
  @conta.setter
  def conta(self, conta: str) -> None:
    self._conta = conta
  
  @property
  def titular(self) -> Titular:
    return self._titular
  
  @titular.setter
  def titular(self, titular: Titular) -> None:
    self._titular = titular
  
  @property
  def saldo(self) -> float:
    return self._saldo
  
  @saldo.setter
  def saldo(self, saldo: float) -> None:
    if saldo >= 0:
      self._saldo = saldo
    else:
      print('Saldo não pode ser negativo.')
  
  def depositar(self, valor: float) -> None:
    if valor > 0:
      self._saldo += valor
      self._movimentacao.append(valor)
      print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
      print('Valor de depósito inválido.')

  def sacar(self, valor: float) -> None:
    if valor > 0 and valor <= self._saldo:
      self._saldo -= valor
      self._movimentacao.append(-valor)
      print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    else:
      print('Valor de saque inválido ou saldo insuficiente.')
  
  def pagar(self, valor: float) -> None:
    if valor > 0 and valor <= self._saldo:
      self._saldo -= valor
      self._movimentacao.append(-valor)
      print(f'Pagamento de R$ {valor:.2f} realizado com sucesso.')
    else:
      print('Valor de pagamento inválido ou saldo insuficiente.')
  
  def transferir(self, valor: float, conta_destino) -> None:
    if valor > 0 and valor <= self._saldo:
      self._saldo -= valor
      conta_destino.depositar(valor)
      self._movimentacao.append(-valor)
      print(f'Transferência de R$ {valor:.2f} realizada com sucesso para a conta {conta_destino.conta}.')
    else:
      print('Valor de transferência inválido ou saldo insuficiente.')
  
  def  imprimir_extrato(self) -> None:
    print(f'Agência: {self._agencia}')
    print(f'Conta: {self._conta}')
    print(f'Titular:\n {self._titular.__str__()}')
    print(f'Saldo: R$ {self._saldo:.2f}')
    print('Movimentações:')
    for mov in self._movimentacao:
      if mov >= 0:
        print(f'E: R$ {mov:.2f}')
      else:
        print(f'S: R$ {-mov:.2f}')

continuar = True
while continuar:
  cpf = input('Digite o CPF do titular: ') 
  nome_do_titular = input('Digite o nome do titular: ')
  data_nascimento_input = input('Digite a data de nascimento do titular (dd/mm/yyyy): ')
  while True:
    try:
      data_nascimento = datetime.strptime(data_nascimento_input, '%d/%m/%Y').date()
      break
    except ValueError:
      print('Data inválida. Por favor, insira a data no formato dd/mm/yyyy.')
      data_nascimento_input = input('Digite a data de nascimento do titular (dd/mm/yyyy): ')
  agencia = input('Digite o número da agência: ')
  conta = input('Digite o número da conta: ')  

  conta_bancaria = ContaBancaria(agencia, conta, Titular(nome_do_titular, data_nascimento, cpf))
  
  while True:
    print('\nMenu:')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Pagar')
    print('4. Transferir')
    print('5. Imprimir Extrato')
    print('6. Sair')

    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
      valor = float(input('Digite o valor a ser depositado: '))
      conta_bancaria.depositar(valor)
    elif opcao == '2':
      valor = float(input('Digite o valor a ser sacado: '))
      conta_bancaria.sacar(valor)
    elif opcao == '3':
      valor = float(input('Digite o valor a ser pago: '))
      conta_bancaria.pagar(valor)
    elif opcao == '4':
      valor = float(input('Digite o valor a ser transferido: '))
      conta_destino_numero = input('Digite o número da conta destino: ')
      conta_destino = ContaBancaria('', conta_destino_numero, '', '', '')
      conta_bancaria.transferir(valor, conta_destino)
    elif opcao == '5':
      conta_bancaria.imprimir_extrato()
    elif opcao == '6':
      break
    else:
      print('Opção inválida. Tente novamente.')
  
  continuar_input = input('Deseja criar outra conta? (s/n): ')
  continuar = continuar_input.lower() == 's'