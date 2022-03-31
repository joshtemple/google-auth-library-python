import google.auth
from google.auth.transport import requests

def sample():
    cred, _ = google.auth.default()

    cred = cred.with_audience("root-default")
    print(cred)
    print(cred.__dict__)

    req = requests.Request()
    cred.refresh(req)

    print(cred.__dict__)


if __name__ == "__main__":
    # first "export GOOGLE_APPLICATION_CREDENTIALS=./gdch.json"
    sample()