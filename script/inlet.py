
import os
from urllib import request

def requestHttp(httpWeb):
    response = request.urlopen("http://" + httpWeb, timeout=5).read().decode("utf-8")
    print("response: {}".format(response))
    pass

if __name__ == "__main__":
    print("env: {}".format(os.environ))

    requestHttp("httpbin.org/")
    pass