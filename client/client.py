#!/usr/bin/python

import sys
import requests

SERVER_DNAME = "localhost"

def _get_path():
    return "http://{}/get_message".format(SERVER_DNAME)

def _post_path():
    return "http://{}/post".format(SERVER_DNAME)

def _send_message(src, dst, msg):
    meta = {'src': src, 'dst': dst, "msg": msg}
    r = request.post(url = _post_path(), data = meta)
    print r.text
    

def _get_message(user):
    params = {'user': user}
    r = request.get(url = _get_path(), params = params)
    print r.content

def _usage():
    print "./client send src dst msg"
    print "./client get user"

def main():
    if sys.argv[1] == "get":
        user = sys.argv[2]
	_get_message(user)
    elif sys.argv[2] == "send":
	src = sys.argv[2]
	dst = sys.argv[3]
	msg = sys.argv[4]
	_send_message(src, dst, msg)
    else:
        _usage()

if __name__ == "__main__":
    main()
