


SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/userinfo.profile']
SHEET_NAME = 'TodoApp'
STATUS_COLUMN = 4


def authenticate_google():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            try:
                creds = pickle.load(token)
            except Exception as e:
                print(f"Fehler beim Laden des Tokens: {e}")
                os.remove('token.pickle')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Token-Refresh fehlgeschlagen: {e}")
                creds = None

        if not creds:
            try:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            except Exception as e:
                print(f"Authentifizierung fehlgeschlagen: {e}")
                return None

    return creds