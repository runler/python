import http.client

conn = http.client.HTTPConnection("200,200,200,14")

payload = ""

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "f5d60348-8d24-4bfe-8c86-9a5bc0296dc3"
    }

conn.request("GET", "healthDocApi,data,sysdia", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))