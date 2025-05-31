import pytest
from unittest.mock import patch, MagicMock, mock_open
from src.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_connect_success(hh_api):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert hh_api._HhApiAbc__connect() is True


def test_connect_failure(hh_api):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        assert hh_api._HhApiAbc__connect() is False


@patch("requests.get")
def test_load_vacancies_connection_error(mock_get, hh_api):
    mock_get.return_value.status_code = 404

    with pytest.raises(ConnectionError, match="Где-то какая-то ошибочка"):
        hh_api.load_vacancies("python")


@patch("builtins.open", new_callable=mock_open)
@patch("requests.get")
def test_load_vacancies_success(mock_get, mock_file, hh_api):
    mock_connect_response = MagicMock()
    mock_connect_response.status_code = 200

    def side_effect(url, params=None):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"items": [{"id": params['page'], "name": f"Vacancy {params['page']}"}]}
        return mock_resp

    mock_get.side_effect = lambda url, params=None: side_effect(url, params) if params else mock_connect_response

    result = hh_api.load_vacancies("python")

    assert len(result) == 20
    assert result[0]["id"] == 0
    assert result[-1]["id"] == 19
    assert mock_get.call_count == 21

    mock_file.assert_called_with("../data/vacancies.json", "w", encoding="utf-8")
