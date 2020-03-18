from http.client import HTTPConnection


def check_internet_connection(host='www.google.com'):
    conn = HTTPConnection( host, timeout= 7 )
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
