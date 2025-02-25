import gspread

def authenticate():
    """
    Authentifiziert sich bei Google Sheets und gibt den Client zurück.
    """
    return gspread.service_account()

def open_sheet(sheet_key):
    """
    Öffnet das Google Sheet mit dem angegebenen Sheet-Key.
    """
    client = authenticate()
    return client.open_by_key(sheet_key)
