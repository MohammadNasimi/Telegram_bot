import requests


token = "7291366744:AAFFY0L0FL-_HQHBN8QB2SelC24T6l8fD6k"
get_list_update = requests.get(f"https://api.telegram.org/bot{token}/getUpdates").json()
# print(response)
chat_id = get_list_update['result'][0]['message']['chat']['id']

send_message = requests.post(url=f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": "kong"}).json()
print(send_message)
