import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = 'odoo'
USER = 'killerstrunger@gmail.com'
PASS = '8ddba7112c0aacc6c264161a65d7a376dd7b1c89'


def json_rpc(method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type": "application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


def call(service, method, *args):
    return json_rpc("call", {"service": service, "method": method, "args": args})


def fetch_data_from_odoo(*args):
    return call("object", "execute", DB, uid, PASS, 'mymodule.medicine', 'search_read', *args)


def sync_data_to_odoo(*args):
    return call("object", "execute", DB, uid, PASS, 'mymodule.medicine', 'create', *args)


url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call("common", "login", DB, USER, PASS)
