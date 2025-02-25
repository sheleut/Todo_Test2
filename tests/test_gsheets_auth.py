import pytest
from unittest.mock import patch, MagicMock
import gsheets_auth  # Dein Modul mit authenticate() und open_sheet()

def test_authenticate_success():
    """
    Testet, dass die Authentifizierung über gspread.service_account korrekt funktioniert.
    """
    # Arrange: Erstelle einen Mock-Client.
    mock_client = MagicMock()
    with patch("gsheets_auth.gspread") as mock_gspread:
        mock_gspread.service_account.return_value = mock_client

        # Act: Rufe die Authentifizierungsfunktion auf.
        client = gsheets_auth.authenticate()

        # Assert: Überprüfe, ob gspread.service_account aufgerufen wurde und der zurückgegebene Client stimmt.
        mock_gspread.service_account.assert_called_once()
        assert client == mock_client

def test_authenticate_failure():
    """
    Testet den Fall, dass die Authentifizierung fehlschlägt, weil gspread.service_account eine Exception wirft.
    """
    error_message = "Authentication failed"
    with patch("gsheets_auth.gspread") as mock_gspread:
        # Simuliere, dass beim Aufruf der Authentifizierung eine Exception geworfen wird.
        mock_gspread.service_account.side_effect = Exception(error_message)

        # Act & Assert: Es wird eine Exception erwartet.
        with pytest.raises(Exception) as exc_info:
            gsheets_auth.authenticate()
        assert str(exc_info.value) == error_message

def test_open_sheet_success():
    """
    Testet, dass ein Google Sheet mit einem gültigen Sheet-Key korrekt geöffnet wird.
    """
    sheet_key = "valid_sheet_key"
    mock_client = MagicMock()
    mock_sheet = MagicMock()
    with patch("gsheets_auth.gspread") as mock_gspread:
        mock_gspread.service_account.return_value = mock_client
        # Simuliere, dass open_by_key das richtige Sheet zurückgibt.
        mock_client.open_by_key.return_value = mock_sheet

        # Act: Rufe die Funktion zum Öffnen des Sheets auf.
        sheet = gsheets_auth.open_sheet(sheet_key)

        # Assert: Überprüfe, ob open_by_key korrekt aufgerufen wurde und das erwartete Sheet zurückgegeben wird.
        mock_client.open_by_key.assert_called_once_with(sheet_key)
        assert sheet == mock_sheet

def test_open_sheet_failure():
    """
    Testet den Fall, dass das Öffnen eines Sheets fehlschlägt (z. B. ungültiger Sheet-Key).
    """
    sheet_key = "invalid_sheet_key"
    error_message = "Sheet not found"
    mock_client = MagicMock()
    with patch("gsheets_auth.gspread") as mock_gspread:
        mock_gspread.service_account.return_value = mock_client
        # Simuliere, dass open_by_key eine Exception wirft.
        mock_client.open_by_key.side_effect = Exception(error_message)

        # Act & Assert: Es wird eine Exception erwartet.
        with pytest.raises(Exception) as exc_info:
            gsheets_auth.open_sheet(sheet_key)
        assert str(exc_info.value) == error_message
