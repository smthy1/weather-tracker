import requests
from database import adicionar_registro, conectar, listar_registros
from dotenv import load_dotenv
import os

load_dotenv()

def previsao_tempo(cidade, idioma="pt"):
    city = cidade
    key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not key:
        print('Erro: Chave não configurada. Adicione ao arquivo .env')
        exit(1)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric&lang={idioma}"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print('Cidade não encontrada ou erro na requisição.')
            return
        
        dados = response.json()
                
        descricao = dados["weather"][0]['description']
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        
        print("\n=== Weather Tracker ===")
        print(f'Cidade: {cidade.capitalize()}')
        print('-'*50)
        print(f'Temperatura: {temperatura}°C')
        print(f'Clima: {descricao.capitalize()}')
        print(f'Humidade: {umidade}%')
        print('-'*50)
        
        escolha = str(input('Deseja adicionar aos registros [S/N]?\nDigite: ')).strip().lower()
        
        while escolha not in 'sn':
            print('Resposta inválida, tente novamente.')
            escolha = str(input('Deseja adicionar aos registros [S/N]?\nDigite: ')).strip().lower()
        
        if escolha == 's':
            adicionar_registro(city, temperatura, descricao, umidade)
            print('Registrando...')
        
        else:
            print('Resgistro não salvo.')

    
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    
    while True:
        print("\n=== Weather Tracker ===")
        print("1. Consultar previsão do tempo")
        print("2. Listar registros salvos")
        print("3. Sair")
        opcao = input('Escolha uma das opções acima: ').strip()
        
        while opcao not in '123':
            print('Opção inválida, tente novamente.')
            opcao = input('Escolha uma das opções acima: ').strip()
        
        if opcao == '1':
            if cidade:
                print(previsao_tempo(cidade))
            else:
                print('Erro: O nome da cidade não pode ficar vazio.')
        
        elif opcao == '2':
            listar_registros()
        
        elif opcao == '3':
            print('Finalizando...')
            break
        

cidade = input('Digite o nome de uma cidade: ').strip()
previsao_tempo(cidade)
