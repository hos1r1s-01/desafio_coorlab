from flask import Flask, jsonify, make_response, request
import json

app = Flask(__name__)


#using json archive as database file
with open ("app/data.json") as file:
    database = json.load(file)


# Global Functions ---------------------------------------------------------------------------------

#function to get travels to specify destination
def get_travels(city):
    
    travels = []
    
    for destination in database['transport']:
        if destination['city'] == city:
            travels.append(destination)
    
    return travels


#function to sort comfort travel options
def order_comfort(travel_list):

    for travel in travel_list:
        travel['duration'] = int(travel['duration'][:-1])

    sortedlist = sorted(travel_list, key=lambda x: (x['bed'], x['duration']))

    for item in sortedlist:
        item['duration'] = str(item['duration']) + 'h'

    return sortedlist[0]


#function to sort economic travel options
def order_economy(travel_list):

    sortedlist = sorted(travel_list, key=lambda x: (x['price_econ']))

    return sortedlist[0]

# ---------------------------------------------------------------------------------------------------


#function expose as API Method to search options
@app.route('/home', methods=['GET'])
def get_travels_result():

    json_request = request.json
    
    city = json_request['city']

    result = {"comfort": order_comfort(get_travels(city)), "economy": order_economy(get_travels(city))}
    
    return make_response(jsonify(result))
    

app.run(debug=True)