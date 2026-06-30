# Bot de Automação para Cadastro de Peças

Este projeto é um **bot de automação** desenvolvido em Python para auxiliar no cadastro de peças em um sistema da metalúrgica.  
Ele utiliza a biblioteca **PyAutoGUI** para simular interações com o computador (cliques, teclas e digitação) e a biblioteca **Pandas** para leitura dos dados de uma planilha Excel.

---

## 🚀 Funcionalidades
- Abre automaticamente o navegador Chrome.
- Acessa o sistema da metalúrgica via URL.
- Lê os dados da planilha `planilha_pecas_metalurgica.xlsx`.
- Preenche os campos do sistema com:
  - Código da peça  
  - Nome da peça  
  - Categoria  
  - Material  
  - Quantidade  
  - Preço unitário  
  - Fornecedor  
- Salva cada peça no sistema e repete o processo até o fim da planilha.

---

## 🛠️ Tecnologias utilizadas
- **[Python](ca://s?q=Python_programming_language)**  
- **[PyAutoGUI](ca://s?q=PyAutoGUI_library)** → Automação de cliques e digitação.  
- **[Pandas](ca://s?q=Pandas_library_in_Python)** → Manipulação e leitura da planilha Excel.  
- **[Excel](ca://s?q=Excel_spreadsheet)** → Fonte dos dados das peças.  

---

## 📂 Estrutura do projeto


Automação/
│
├── bot_automacao.py              # Script principal
├── planilha_pecas_metalurgica.xlsx # Planilha com os dados
└── README.md                     # Documentação do projeto