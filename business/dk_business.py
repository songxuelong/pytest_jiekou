import requests


def dk(session, base_url):
    url = base_url + "/crpt-cust/identification/myinfo"

    r = session.post(url, verify=False)
    print(r.json())
    return r







if __name__ == '__main__':
    s = requests.session()
    base_url = "https://gateway.crpt-cloud.liuheco.com"

    dk(s, base_url)
