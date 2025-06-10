![image](https://github.com/user-attachments/assets/641c828b-a55f-4995-9bc8-820f9ac11441)

🗺️ Mapa Interativo de Setores Próximos - Goiânia
Este é um aplicativo web interativo desenvolvido com Dash, Folium, e GeoPandas, que permite ao usuário visualizar setores geográficos de Goiânia e identificar quais estão dentro de um raio de distância definido a partir de um setor selecionado.

✨ Funcionalidades
Seleção de um setor urbano de Goiânia.
Definição de uma distância máxima (em metros).
Visualização em mapa dos setores vizinhos dentro do raio especificado.
Mapa interativo com destaque dos setores e marcadores com seus nomes.
🛠️ Tecnologias Utilizadas
Dash + Dash Bootstrap Components
Folium
GeoPandas
Shapely
Python 3.8+
📦 Estrutura do Projeto
├── app.py
├── base_goiania.geojson
├── requirements.txt
└── README.md
📍 Fonte dos Dados
O arquivo base_goiania.geojson contém os dados geoespaciais dos setores urbanos de Goiânia. Ele pode ser obtido de fontes públicas como o portal de dados abertos da prefeitura.

🚀 Como Executar
Clone o repositório:

Crie e ative um ambiente virtual:

Instale as dependências:

Execute o aplicativo:

Acesse no navegador:
http://127.0.0.1:8050/
🧠 Como Funciona
O usuário seleciona um setor e define uma distância.
O app calcula a distância entre o setor selecionado e os demais usando projeção métrica (EPSG:31982).
Os setores dentro do raio são exibidos em um mapa interativo com destaque e marcadores.
📄 Licença
Este projeto está licenciado sob a MIT License.
