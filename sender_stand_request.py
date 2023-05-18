import configuration
import requests
import data
def post_new_orders(orders_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,  # подставляем полный url
                         json=orders_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
response = post_new_orders(data.orders_body)
print(response.status_code)
print(response.json())

def get_new_track():
    response = post_new_orders(data.orders_body)
    track = response.json()['track']
    current_new_track = track
    return current_new_track
print(response.status_code)
print(response.json()['track'])
def get_new_orders_track():
    t = {'track': get_new_track()}
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK_PATH, params=t)
response = get_new_orders_track()
print(response.status_code)
print(response.json())

