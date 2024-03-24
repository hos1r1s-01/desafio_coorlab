from flask import Flask, jsonify, make_response
import json

app = Flask(__name__)

with open ("app/data.json") as file:
    database = json.load(file)

"""@app.route('/home', methods=['GET'])
def home():
    return make_response(jsonify(database))"""

def get_travels(city):
    
    travels = []
    
    for destination in database['transport']:
        if destination['city'] == city:
            travels.append(destination)
    
    return travels


def order_comfort(travel_list):

    for travel in travel_list:
        travel['duration'] = int(travel['duration'][:-1])

    sortedlist = sorted(travel_list, key=lambda x: (x['bed'], x['duration']))

    for item in sortedlist:
        item['duration'] = str(item['duration']) + 'h'

    return sortedlist[0]


def order_economy(travel_list):

    sortedlist = sorted(travel_list, key=lambda x: (x['price_econ']))

    return sortedlist[0]



print(order_comfort(get_travels('São Paulo')))
print('-------------------------------------')
print(order_economy(get_travels('São Paulo')))

#app.run(debug=True)