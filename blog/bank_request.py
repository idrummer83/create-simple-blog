
import http.client

conn = http.client.HTTPSConnection("dev.api.sberbank.ru")

payload = "{\"bankInvoiceId\":\"4482bd290cbdaa7738e7d0ed9a9b1c25\",\"merchantInvoiceId\":\"654321654321\"}"

headers = {
    'x-ibm-client-id': "7473b988-2796-4692-9581-354141c93cc3",
    'authorization': "Bearer REPLACE_BEARER_TOKEN",
    'x-introspect-rquid': "uL6pD1nE0rC7tV7sF7mH6tG0iD6fR2oM1wN4rQ6dK2rO5qK4iJ",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/ru/prod/sberbankid/v2.1/status", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))