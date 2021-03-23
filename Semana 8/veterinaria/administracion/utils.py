import requests


def consultarDNI(dni):
    base_url = "https://apiperu.dev/api/"
    solicitud = requests.get(url=base_url+"dni/"+dni, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer 6287da8da77342f7e4aab59b670dbe153f0e803c2553e7a7dcbcc7d2510ba793"
    })
    print(solicitud.status_code)
    print(solicitud.json())
    return solicitud.json()
