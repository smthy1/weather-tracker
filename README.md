# 🌍 Weather Tracker

A simple Python application to check the weather forecast using the **OpenWeatherMap API** and store the data in a **SQLite** database.

> **Note**: The code and user interface are in Portuguese, but this documentation includes both English and Portuguese versions for accessibility.

## ✨ Features:
 - Check the current weather forecast for any city.
 - Display:
    - Temperature (°C)
    - Weather description
    - Relative humidity (%)

 - Option to save the weather data in a local SQLite database.
 - View previously saved records.
 - Interactive menu for navigation.

# 🛠 Technologies used:

- **Python 3.8+** (tested on Python 3.13)
- **SQLite3** (built-in)
- **OpenWeatherMap API**
- Python libraries:
  - `requests`: For HTTP requests
  - `python-dotenv`: For managing API keys

## 📋 Prerequisites:
 - Python 3.8 or higher (recommended: Python 3.13 for optimal compatibility)
 - An API key from [OpenWeatherMap](https://openweathermap.org/api)

## 🚀 How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/LuizSmith/weather-tracker.git
   cd weather-tracker

2. Create and activate a virtual enviroment:
    python -m venv venv
    
    source venv/bin/activate  # Linux/Mac
    
    venv\Scripts\activate     # Windows

3. Install dependencies:
    pip install -r requirements.txt

4. Create a .env file in the project root and add your Key:
    OPENWEATHERMAP_API_KEY=your_api_key_here

5. Run te application: python main.py

# Notes:
 - The SQLite database (clima.db) is created automatically on first run.

 - The application uses Portuguese for the user interface and API responses (language set to pt).

 - The interactive menu allows you to check the weather, view saved records, or exit.

# Contributing:
 - Feel free to open issues or submit pull requests with suggestions or improvements!

# Contact:
 - Developed by Luiz Smith. Reach out via email [luiz.smith.br@gmail.com]


# 🇧🇷 Weather Tracker

Um aplicativo simples em Python para consultar a previsão do tempo atual usando a **API OpenWeatherMap** e salvar os dados em um banco de dados **SQLite**.

## ✨ Funcionalidades:
- Consultar a previsão do tempo para qualquer cidade.
- Exibir:
  - Temperatura (°C)
  - Descrição do clima
  - Umidade relativa (%)
- Opção para salvar os dados do clima em um banco SQLite.
- Visualizar registros salvos anteriormente.
- Menu interativo para fácil navegação.

## 🛠 Tecnologias Utilizadas:
- **Python 3.8+** (testado no Python 3.13)
- **SQLite3** (nativo no Python)
- **API OpenWeatherMap**
- Bibliotecas Python:
  - `requests`: Para requisições HTTP
  - `python-dotenv`: Para gerenciar chaves de API

## 📋 Pré-requisitos:
- Python 3.8 ou superior (recomendado: Python 3.13 para compatibilidade ideal)
- Uma chave de API do [OpenWeatherMap](https://openweathermap.org/api)

## 🚀 Como Executar:
1. Clone o repositório:
   ```bash
   git clone https://github.com/LuizSmith/weather-tracker.git
   cd weather-tracker

2. Crie e ative um ambiente virtual: 
    python -m venv venv
    
    source venv/bin/activate  # Linux/Mac
    
    venv\Scripts\activate     # Windows

3. Instale as dependências:
    pip install -r requirements.txt

4. Crie um arquivo .env na raiz do projeto e adicione sua chave de API:
    OPENWEATHERMAP_API_KEY=sua_chave_aqui

5. Execute o aplicativo: python main.py

# Observações:
 - O banco de dados SQLite (clima.db) é criado automaticamente na primeira execução.

 - O aplicativo usa português para a interface do usuário e respostas da API (idioma configurado como pt).

 - O menu interativo permite consultar o clima, visualizar registros salvos ou sair.

# Contribuições:
 - Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões ou melhorias!

# Contato
 - Desenvolvido por Luiz Smith. Entre em contato via email [luiz.smith.br@gmail.com]