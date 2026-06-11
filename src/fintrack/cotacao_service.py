import requests


def obter_cotacao_dolar():
    """
    Consulta a cotação atual do dólar usando a AwesomeAPI.
    """

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    try:
        response = requests.get(url, timeout=5)

        # Verifica se a requisição deu certo
        response.raise_for_status()

        dados = response.json()

        cotacao = dados["USDBRL"]["bid"]

        return float(cotacao)

    except requests.RequestException as erro:
        print(f"Erro ao consultar API: {erro}")
        return None