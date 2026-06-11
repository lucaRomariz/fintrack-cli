from unittest.mock import patch, Mock
from fintrack.cotacao_service import obter_cotacao_dolar


@patch("fintrack.cotacao_service.requests.get")
def test_obter_cotacao_dolar(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "USDBRL": {
            "bid": "5.50"
        }
    }

    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    cotacao = obter_cotacao_dolar()

    assert cotacao == 5.50