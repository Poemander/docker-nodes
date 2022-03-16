
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import math
import json

IP_list = {
    "agoric",
    "akash",
    "cosmoshub",
    "osmosis",
    "secret",
    "regen",
    "persistence",
    "impacthub",
    "juno",
    "stargaze",
}

for ip in IP_list:
    url = 'https://lcd-' +ip+ '.keplr.app/gov/proposals?'

    parameters = {
        'status': "PROPOSAL_STATUS_VOTING_PERIOD",
    }
    headers = {
        'Accept': 'application/json',
    }

    session = Session()
    session.headers.update(headers)

    print(url)

    try:
        response = session.get(url, params=parameters, headers=headers)
        data = response.text
        pretty = json.dumps(data, indent=0)
        print(data)
        print(pretty)
        print("\n")

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
