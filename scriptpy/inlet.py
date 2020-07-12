# coding: utf-8

import sys
import logging

logging.basicConfig(format='%(asctime)s - %(filename)s - %(lineno)-4d - %(levelname)-5s %(message)s',
                    filename=r'logger.log',
                    filemode='w',
                    level=logging.DEBUG)


def request_http(http_web):
    import requests
    import json
    url = 'http://' + http_web.strip()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36 '
    }
    response = requests.get(url, headers=headers)
    code_dic = json.loads(response.content.decode("utf-8"))
    logging.debug("code_dic: {}".format(code_dic))
    pass


if __name__ == "__main__":
    sys.path.append("../")
    logging.debug("sys.path: {}".format(sys.path))

    if True:
        import inletParse
        inletParse.inlet()
    pass

    # request_http(r"httpbin.org/")
    pass
