from fintrack.cotacao_service import obter_cotacao_dolar

def test_obter_cotacao_dolar():
    cotacao = obter_cotacao_dolar()
    assert cotacao is not None
    assert cotacao > 0
