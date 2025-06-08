from flask import Flask, render_template, jsonify
import requests
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/proximo_feriado')
def proximo_feriado():
    url = "https://date.nager.at/api/v3/NextPublicHolidays/BR"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        feriados = response.json()

        # Encontrar o próximo feriado a partir de hoje
        hoje = datetime.now(pytz.timezone('America/Sao_Paulo')).date()
        for feriado in feriados:
            data_feriado = datetime.strptime(feriado['date'], "%Y-%m-%d").date()
            if data_feriado >= hoje:
                # Calcular dias restantes
                dias_restantes = (data_feriado - hoje).days

                # Tratar local (correção do erro)
                local = "Brasil"  # Valor padrão

                # Verificar se 'counties' existe e tem conteúdo
                if 'counties' in feriado and feriado['counties']:
                    # Pega o primeiro município e extrai o nome
                    local = feriado['counties'][0].split("-")[-1]

                return jsonify({
                    'nome': feriado['name'],
                    'data': data_feriado.strftime("%d/%m/%Y"),
                    'dias_restantes': dias_restantes,
                    'local': local
                })

        return jsonify({'erro': 'Nenhum feriado futuro encontrado'}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)