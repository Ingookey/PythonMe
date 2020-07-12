
import os
import

def requestHttp(httpWeb):
    import requests
    import json
    url = 'http://' + httpWeb.strip()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    code_dic = json.loads(response.content.decode("utf-8"))
    print("code_dic: {}".format(code_dic))
    pass

if __name__ == "__main__":
    print("env: {}".format(os.environ))

    requestHttp("httpbin.org/")
    pass