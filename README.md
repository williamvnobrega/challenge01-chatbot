# Challenge 01 - Chatbot

<p align="left">
  <img src="https://img.shields.io/badge/python-3.8+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Telegram-Bot-2CA5E0?logo=telegram" alt="Telegram Bot">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Status">
</p>

Um bot de Telegram para acompanhar estatísticas e agenda da FURIA no Counter-Strike 2.

---

## ✨ Funcionalidades

### 🗓 Agenda de Partidas
- Mostra a **próxima partida** do time
- Exibe detalhes completos:
  - 🆚 Adversário
  - 📅 Data e horário
  - 🏆 Torneio
- Atualização automática dos jogos

### 📊 Estatísticas do Time
- ⚡ **Win Streak**: Sequência atual de vitórias
- 📈 **Win Rate**: Porcentagem geral de vitórias
- 🏆 **Ranking**: Posição no ranking HLTV
- 📅 **Últimos 5 resultados**: Visualização intuitiva com ícones (🟢/🔴)
- 🗺️ **Win Rate por Mapa**:
  - Dust2: 44.4%
  - Mirage: 42.9%
  - Inferno: 40.0%
  - Train: 40.0%
  - Nuke: 25.0%

---

## 🚀 Como Usar

1. Busque por `@Challenge01FBot` no Telegram
2. Envie o comando `/start`


## 🛠 Desenvolvimento

### 📋 Pré-requisitos
- Python 3.8+
- Conta no Telegram com [@BotFather](https://t.me/BotFather)
- Token API do Telegram

### ⚙️ Instalação
```
git clone https://github.com/williamvnobrega/challenge01-chatbot.git
cd challenge01-chatbot
pip install -r requirements.txt
```
## 🔧 Configuração

1. Crie um arquivo `.env` na raiz do projeto:
   ```
   TELEGRAM_TOKEN=seu_token_aqui
   ```
2. Execute o bot:
   ```
   python bot.py
   ```

### 📌 Exemplo de Saída
- Próxima Partida:
```
🆚 The MongolZ  
📅 10/05 às 05:00  
🏆 PGL Astana 2025 
```

- Estatísticas: 
```
⚡ Win Streak: 0  
📈 Win Rate: 33.3%  
🏆 Ranking: #17  
📅 Últimos 5 jogos:  
🟢 🔴 🟢 🔴 🔴  
🗺️ Win Rate Mapas:  
• Dust2: 44.4%  
• Mirage: 42.9%  
• Inferno: 40.0%
```

### 🤝 Como Contribuir
1. Faça um Fork do projeto

2. Crie uma Branch (git checkout -b feature/nova-funcionalidade)

3. Commit suas mudanças (git commit -m 'Adiciona funcionalidade X')

4. Push para a Branch (git push origin feature/nova-funcionalidade)

5. Abra um Pull Request

### 📄 Licença
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](/LICENSE) para detalhes completos.
