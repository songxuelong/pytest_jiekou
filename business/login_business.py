import requests
import pytest


def login(session, base_url):
    url = base_url + "/auth/oauth/token"
    payload = "loginDevice=39d0f50c317e40fe80c9877d0684f02b&ipAddress=111.204.119.83&latitude=39.996419&longitude=116.480456&terminal_version=11&appVersion=0.0.0&location=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E9%98%9C%E5%AE%89%E8%A5%BF%E8%B7%AF%E8%BE%85%E8%B7%AF&grant_type=password&scope=app&client_id=client&client_secret=secret&username=17709871234&loginType=1&password=MTIzNDU2"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    r = session.post(url, data=payload, headers=headers, verify=False)
    # 更新session会话的头部
    h = {
        "Authorization": "bearer " + r.json()["access_token"],
        "Content-Type": "application/x-www-form-urlencoded"

    }
    session.headers.update(h)
    print(r.json())
    print("-----------------------------------------------------------")
    return r


if __name__ == '__main__':
    s = requests.session()
    base_url = "https://gateway.crpt-cloud.liuheco.com"
    login(s, base_url)
