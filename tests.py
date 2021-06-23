# Third-party imports...
from nose.tools import assert_true
import requests
import responses
from processdata import ProcessData
from apiconnection import GetData


def test_fetch_api_data():
    designArea = 'Thames Valley (Heathrow)'
    obj = GetData()
    response = obj.fetchData(designArea)
    assert (response.status_code, 200)

def test_heat_loss_calculation():
    obj = ProcessData()
    floorArea = 30
    heatingFactor= 1.9
    insulationFactor = .8
    heatLoss = obj.calculateHeatLoss(floorArea,heatingFactor,insulationFactor)
    assert(heatLoss,45.6)


def test_power_heat_loss_calculation():
    obj = ProcessData()
    floorArea = 30
    heatingFactor= 1.9
    insulationFactor = .8
    heatLoss = obj.calculateHeatLoss(floorArea,heatingFactor,insulationFactor)
    assert(heatLoss,45.6)

def test_request_response():
    # Send a request to the API server and store the response.
    responses.add(responses.GET, 'https://063qqrtqth.execute-api.eu-west-2.amazonaws.com/v1/weather?location=<Severn Valley (Filton)>',
                  json={'success': 'found'}, status=200)
    
    resp = requests.get('https://063qqrtqth.execute-api.eu-west-2.amazonaws.com/v1/weather?location=<Severn Valley (Filton)>')

    # Confirm that the request-response cycle completed successfully.
    assert (resp.status_code, 200)

@responses.activate
def test_simple():
    responses.add(responses.GET, 'https://063qqrtqth.execute-api.eu-west-2.amazonaws.com/v1/weather?location=<Severn Valley (Filton)>',
                  json={'error': 'not found'}, status=404)

    resp = requests.get('https://063qqrtqth.execute-api.eu-west-2.amazonaws.com/v1/weather?location=<Severn Valley (Filton)>')

    assert (resp.status_code, 404)
