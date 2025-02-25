import os
import unittest
from google.oauth2 import service_account
from googleapiclient.discovery import build

class TestGoogleSheetsAPI(unittest.TestCase):
    def setUp(self):
        # Pfad zur JSON-Datei mit den Anmeldeinformationen
        self.credentials_path = 'path/to/your/credentials.json'
        self.spreadsheet_id = 'your_spreadsheet_id'
        self.range_name = 'Sheet1!A1:D10'

    def test_authenticate_and_read(self):
        # Authentifizierung mit dem Dienstkonto
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_path,
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )

        # Erstellen des API-Clients
        service = build('sheets', 'v4', credentials=credentials)

        # Abrufen der Daten aus dem angegebenen Bereich
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheet_id, range=self.range_name).execute()
        values = result.get('values', [])

        # Überprüfen, ob Daten vorhanden sind
        self.assertIsNotNone(values)
        self.assertGreater(len(values), 0)

if __name__ == '__main__':
    unittest.main()
