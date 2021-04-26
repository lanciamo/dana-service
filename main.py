# This is a sample Python script.
import json

import requests
import urllib

import numpy as np
import pandas as pd

import keras as ks
import tensorflow as tf


url_rest = 'http://83.220.172.94/api/prediction/orders/nn'
headers = {
    "cache-control": "no-cache",
    "content-type": "application/json"  # application/x-www-form-urlencoded"
}
preds = {
      "predictions": {
        "products": [
          {
            "order_system_id": 11233,
            "order_seller_system_id": 21211,
            "order_type": 1,
            "seller_id": 6,
            "buyer_id": 5,
            "products": [
              {
                "product_id": 56,
                "amount": 9999999
              },
              {
                "product_id": 11,
                "amount": 9999999
              },
              {
                "product_id": 85,
                "amount": 9999999
              },
              {
                "product_id": 57,
                "amount": 9999999
              }
            ],
            "timestamp": 1615313990,
            "edit_timestamp": 1615313990,
            "period": 1,
            "status": 4
          },
          {
            "order_system_id": 11233,
            "order_seller_system_id": 21311,
            "order_type": 1,
            "seller_id": 6,
            "buyer_id": 5,
            "products": [
              {
                "product_id": 1,
                "amount": 9999999
              },
              {
                "product_id": 75,
                "amount": 9999999
              },
              {
                "product_id": 115,
                "amount": 9999999
              }
            ],
            "timestamp": 1615313990,
            "edit_timestamp": 1615313990,
            "period": 2,
            "status": 4
          },
          {
            "order_system_id": 12233,
            "order_seller_system_id": 13211,
            "order_type": 1,
            "seller_id": 76,
            "buyer_id": 5,
            "products": [
              {
                "product_id": 50,
                "amount": 9999999
              },
              {
                "product_id": 41,
                "amount": 9999999
              },
              {
                "product_id": 39,
                "amount": 9999999
              },
              {
                "product_id": 88,
                "amount": 9999999
              },
              {
                "product_id": 89,
                "amount": 9999999
              }
            ],
            "timestamp": 1615313990,
            "edit_timestamp": 1615313990,
            "period": 3,
            "status": 4
          },
          {
            "order_system_id": 1102233,
            "order_seller_system_id": 2013211,
            "order_type": 1,
            "seller_id": 76,
            "buyer_id": 5,
            "products": [
              {
                "product_id": 66,
                "amount": 9999999
              },
              {
                "product_id": 67,
                "amount": 9999999
              },
              {
                "product_id": 68,
                "amount": 9999999
              },
              {
                "product_id": 69,
                "amount": 9999999
              },
              {
                "product_id": 70,
                "amount": 9999999
              },
              {
                "product_id": 99,
                "amount": 9999999
              }
            ],
            "timestamp": 1615313990,
            "edit_timestamp": 1615313990,
            "period": 4,
            "status": 1
          }
        ],
        "materials": [
          {
            "timestamp": 1615313990,
            "edit_timestamp": 1615313990,
            "seller_id": 5,
            "status": 1,
            "materials": [
              {
                "amount": 12,
                "material_id": 54
              },
              {
                "amount": 4,
                "material_id": 3
              },
              {
                "amount": 7,
                "material_id": 15
              },
              {
                "amount": 10,
                "material_id": 17
              },
              {
                "amount": 1,
                "material_id": 45
              }
            ]
          },
          {
            "timestamp": 1615313990,
            "edit_timestamp": 1615313990,
            "seller_id": 4,
            "status": 1,
            "materials": [
              {
                "amount": 12,
                "material_id": 21
              },
              {
                "amount": 4,
                "material_id": 76
              },
              {
                "amount": 7,
                "material_id": 46
              },
              {
                "amount": 10,
                "material_id": 33
              },
              {
                "amount": 1,
                "material_id": 98
              }
            ]
          },
          {
            "timestamp": 1615313990,
            "edit_timestamp": 1615313990,
            "seller_id": 3,
            "status": 1,
            "materials": [
              {
                "amount": 12,
                "material_id": 8
              },
              {
                "amount": 4,
                "material_id": 5
              },
              {
                "amount": 7,
                "material_id": 12
              },
              {
                "amount": 10,
                "material_id": 22
              },
              {
                "amount": 1,
                "material_id": 44
              }
            ]
          }
        ]
      }
    }


def app_input(url):
    req = requests.get(url)
    orders = pd.DataFrame(req.json()['orders'])
    events = pd.DataFrame(req.json()['events'])

    pd.to_datetime(orders.timestamp, unit='s')
    return req, orders, events


def time_series_forecast(dataset):
    pass


def app_output(url, preds):
    params = urllib.parse.quote_plus(json.dumps(preds))
    string = url + '?predictions=' + params
    r = requests.post(string)
    return r


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r, orders, events = app_input(url_rest)
    print('Status GET', r)
    r = app_output(url_rest, preds)
    print('Status POST', r)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
