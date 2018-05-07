# -*- coding: utf-8 -*-
import simplejson
from websocket import create_connection


class BuilderBaseFunc(object):
    def __init__(self, ws, testdomain):
        self.ws = ws
        self.testdomain = testdomain

    def web_socket_request(self, dictmsg):
        print('send:', dictmsg)
        self.ws.send(simplejson.dumps(dictmsg))
        result = self.ws.recv()
        resp = simplejson.loads(result)
        print("recv:", resp)

        return resp


def get_ws_driver(ws_url):
    ws = create_connection("ws://%s/wsapi" % ws_url)
    return BuilderBaseFunc(ws, ws_url)

