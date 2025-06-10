🇧🇷 Verificador de Próximo Feriado no Brasil
Este é um aplicativo web simples desenvolvido com Flask que exibe o próximo feriado público no Brasil, utilizando a API pública Nager.Date.

✨ Funcionalidades
Consulta automática do próximo feriado nacional ou regional no Brasil.
Exibição do nome do feriado, data, local e quantos dias faltam.
Interface web básica com index.html.
API RESTful com resposta em JSON.
🛠️ Tecnologias Utilizadas
Python 3
Flask
Requests
Nager.Date API
Jinja2 (via Flask)
pytz para manipulação de fuso horário
🚀 Como Executar Localmente
Clone o repositório:

Crie um ambiente virtual e ative-o:

Instale as dependências:

Execute o servidor Flask:

Acesse no navegador:
http://127.0.0.1:5000/
📦 Estrutura do Projeto
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
🔄 Endpoints
/ — Página inicial (HTML)
/proximo_feriado — Retorna os dados do próximo feriado em formato JSON:

📄 Licença
Este projeto está licenciado sob a MIT License.
