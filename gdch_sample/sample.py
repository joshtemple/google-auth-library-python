import google.auth
from google.auth.transport import requests
import logging
from http.client import HTTPConnection # py3

HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


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