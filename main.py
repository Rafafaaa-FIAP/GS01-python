
# Cria duas variáveis do tipo array para serem utilizadas por todo código
menuOptions = []
networks = []

# Cria dois tipos de classes para serem utilizadas por todo código
# A função __init__ serve para criar uma variável do tipo da classe
class option:
  def __init__(self, id, name):
      self.id = id
      self.name = name

class network:
  def __init__(self, id, name, description, address, contact):
      self.id = id
      self.name = name
      self.description = description
      self.address = address
      self.contact = contact
      self.isDisqualified = False



# Função para inicializar o sistema.
def initializeSystem():
  # Roda a função loadLists
  loadLists()

  # Mostra a mensagem de boas-vindas ao sistema
  print('\nBem-vindo à área da Rede Credenciada da Hapvida NotreDame Intermédica!\n')

  # Cria uma variável que recebe o que retornar na função choiceMenuOption
  option = choiceMenuOption()
  # Enquanto o id da opção selecionada for diferente de 0
  while (option.id != 0):
    # Mostra o nome da opção selecionada
    print(f'\n--------------- {option.name} ---------------\n')
    # Utilizando if e elif, verifica qual o id da opção selecionada para rodar a respectiva função necessária
    if (option.id == 1):
      listNetworks()
    elif (option.id == 2):
      createNetwork()
    elif (option.id == 3):
      updateNetwork()
    elif (option.id == 4):
      decertifyNetwork()
    elif (option.id == 5):
      searchNetworks()
    print()
    option = choiceMenuOption()

  # Mostra uma mensagem de agradecimento por utilizar o sistema
  print('\nObrigado por utilizar nosso sistema!\n')

# Função para carregar as variáveis do tipo array necessárias
def loadLists():
  # Insere no array menuOptions um item que é do tipo option
  # Cria o item utilizando a função option que chama a função __init__ criada no início do código
  menuOptions.append(option(1, 'Listar Redes Credenciadas'))
  menuOptions.append(option(2, 'Cadastrar Rede Credenciada'))
  menuOptions.append(option(3, 'Alterar Rede Credenciada'))
  menuOptions.append(option(4, 'Descredenciar Rede'))
  menuOptions.append(option(5, 'Pesquisar Rede'))
  menuOptions.append(option(0, 'Sair'))

# Função para mostrar as opções disponíveis para o usuário escolher
def choiceMenuOption():
  # Mostra uma mensagem de título do menu
  print('--------------- Menu ---------------')
  # Percorre o array menuOptions para mostrar as opções disponíveis
  for o in menuOptions:
    print(f'{o.id} - {o.name}')

  # Cria uma variável par utilizar nos inputs seguintes
  inputText = 'Digite o código de uma opção: '
  # Cria uma variável que recebe o que retornar da função inputWithValidation
  option_id = inputWithValidation(inputText, 'int')
  # Enquanto o inverso do bool que retornar da função checkExistingItemInList for true
  while (not checkExistingItemInList(menuOptions, option_id, 'id')):
    # Mostra a mensagem de erro
    print('Opção digitada inválida!')
    # Chama novamente a função inputWithValidation
    option_id = inputWithValidation(inputText, 'int')

  # Cria uma variável que irá retornar na função
  ret = menuOptions[0]
  # Percorre a lista de opções disponíveis
  for o in menuOptions:
    # Verifica se o id da opção atual é igual ao que o usuário selecionou para setar na variável ret e para o for utilizando break
    if (o.id == option_id):
      ret = o
      break

  # Retorna a variável ret
  return ret



# Função para listar as redes cadastradas
def listNetworks():
  # Verifica se a quantidade de itens no array network é igual a 0
  if (len(networks) == 0):
    # Mostra uma mensagem
    print('Não há redes cadastradas')
  else:
    # Percorre o array networks
    for n in networks:
      # Cria uma variável vazia se receberá um texto apenas se a rede atual estiver descredenciada
      disqualifiedText = ''
      if (n.isDisqualified):
        disqualifiedText = '(descredenciada)'
      # Mostra uma mensagem com todos os dados da rede atual
      print (f'{n.id} {disqualifiedText} - {n.name} - {n.description} - {n.address} - {n.contact}')

# Função para cadastrar uma rede
def createNetwork():
  # Cria uma variável e percorre a lista de redes cadastradas para pegar o último id cadastrado e soma 1
  last_network_id = 0
  for n in networks:
    last_network_id = n.id
  last_network_id += 1

  # Cria uma variável que recebe o que retornar da função returnNewNetwork
  network = returnNewNetwork()
  network.id = last_network_id

  # Adiciona a variável criada no array networks
  networks.append(network)

  # Mostra uma mensagem
  print('Rede cadastrada com sucesso')

# Função para alterar uma rede
def updateNetwork():
  # Roda a função listNetworks para mostrar todas as redes cadastradas
  listNetworks()

  # Pede para o usuário digitar o código de uma rede, verificando se é um código válido
  inputText = 'Digite o código da rede que deseja alterar: '
  network_id = inputWithValidation(inputText, 'int')
  while (not checkExistingItemInList(networks, network_id, 'id')):
    print('Rede não encontrada')
    network_id = inputWithValidation(inputText, 'int')

  # Verifica se a rede selecionada está descredenciada ou não
  if (checkNetworkAccreditation(network_id)):
    # Cria a variável com os novos dados da rede
    network = returnNewNetwork()
    network.id = network_id

    # Localiza a rede selecionada no array networks e atualiza a rede e para o for
    for n in networks:
      if (n.id == network_id):
        n.name = network.name
        n.description = network.description
        n.address = network.address
        n.contact = network.contact
        break

    print('Rede alterada com sucesso')
  else:
    print('Não é possível alterar uma rede descredenciada')

# Função para descredenciar uma rede
def decertifyNetwork():
  # Roda a função listNetworks para mostrar todas as redes cadastradas
  listNetworks()

  # Pede para o usuário digitar o código de uma rede, verificando se é um código válido
  inputText = 'Digite o código da rede que deseja descredenciar: '
  network_id = inputWithValidation(inputText, 'int')
  while (not checkExistingItemInList(networks, network_id, 'id')):
    print('Rede não encontrada')
    network_id = inputWithValidation(inputText, 'int')

  # Verifica se a rede selecionada está descredenciada ou não
  if (checkNetworkAccreditation(network_id)):
    # Pede confirmação do usuário
    response = inputWithValidation('Tem certeza que deseja descredenciar essa rede? (sim/não): ', 'boolean')
    
    # Verifica se o usuário confirmou, percorre o array networks, localiza a rede selecionada, a descredencia e para o for
    if (response):
      for n in networks:
        if (n.id == network_id):
          n.isDisqualified = True
          break

      print('Rede descredenciada com sucesso')
  else:
    print('Rede já descredenciada')

# Função para retornar uma variável do tipo network
def returnNewNetwork():
  # Pede para o usuário digitar os dados da rede.
  inputText = 'Digite o nome da rede credenciada: '
  name = inputWithValidation(inputText, 'string')
  # Verificar se há alguma rede cadastrada com o nome que o usuário digitou
  while (checkExistingItemInList(networks, name, 'name')):
    print('Já existe uma rede cadastrada com esse nome')
    name = inputWithValidation(inputText, 'string')

  description = inputWithValidation('Digite uma descrição para o local: ', 'string')
  
  address = inputWithValidation('Digite o endereço do local: ', 'string')
  
  contact = inputWithValidation('Digite o contato do local: ', 'string')

  # Criar a variável do tipo network e a retorna
  return network(0, name, description, address, contact)

# Função para verificar se uma rede está descredenciada
def checkNetworkAccreditation(network_id):
  # Percorre a lista de redes para localizar a rede que tenha o id que foi passado por parâmetro na função, parando o for ao encontrar
  currentNetwork = networks[0]
  for n in networks:
    if (n.id == network_id):
      currentNetwork = n
      break

  # Retorna se o inverso se item está ou não descredenciado
  return not currentNetwork.isDisqualified

# Função para pesquisar uma rede
def searchNetworks():
  # Verifica se a quantidade de itens no array network é igual a 0
  if (len(networks) == 0):
    print('Não há redes cadastradas')
  else:
    # Pede para o usuário digitar o que quer pesquisar
    searchText = input('Pesquisar rede: ')
    
    # Percorre a lista de redes e mostra todos os dados apenas das redes que possuem o que o usuário digitou
    for n in networks:
      disqualifiedText = ''
      if (n.isDisqualified):
        disqualifiedText = '(descredenciada)'
      printText = f'{n.id} {disqualifiedText} - {n.name} - {n.description} - {n.address} - {n.contact}'
      if (searchText in printText):
        print(printText)



# Função para pedir para o usuário digitar, verificando se o que digitou é válido ou não
def inputWithValidation(inputText, typeValue):
  # Cria uma variável para uma mensagem de erro padrão
  errorMessage = 'Valor digitado é inválido'

  # Pede para o usuário digitar até não ser um valor vazio
  ret = input(inputText)
  while (ret == ''):
    print(errorMessage)
    ret = input(inputText)

  # Verifica o tipo que foi passado por parâmetro na função
  if (typeValue == 'int'):
    # Pede para o usuário digitar até não ser um valor não numérico
    while (not ret.isnumeric()):
      print(errorMessage)
      ret = input(inputText)
    ret = int(ret)
  elif (typeValue == 'boolean'):
    # Pede para o usuário digitar até ser sim ou não
    while (ret != 'sim' and ret != 'não'):
      print(errorMessage)
      ret = input(inputText)
    ret = ret == 'sim'

  # Retorna o que o usuário digitou
  return ret

# Função para verificar que um item existe em uma lista
def checkExistingItemInList(items, item_value, check_by):
  ret = False
  # Percorre a lista que foi passado por parâmetro
  for item in items:
    # Cria uma variável que recebe o que será verificado dependendo do tipo que foi passado por parâmetro
    check_value = ''
    if (check_by == 'id'):
      check_value = item.id
    elif (check_by == 'name'):
      check_value = item.name

    # Verifica se a variável é igual ao que foi passado por parâmetro, se for, seta a variável de retorno como verdadeiro e para o for
    if (check_value == item_value):
      ret = True
      break

  return ret



# Roda a função initializeSystem
initializeSystem()
