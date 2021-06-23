import sys
sys.path.append(".")
import json
from apiconnection import GetData


class ProcessData:

    def calculateHeatLoss(self, floorArea,heatingFactor, insulationFactor):
        heatLoss = floorArea  * heatingFactor * insulationFactor
        return heatLoss

    def calculatePowerHeatLoss(self, heatLoss, heatingDegrees):
        powerHeatLoss = float(heatLoss) / float(heatingDegrees) 
        return powerHeatLoss

    def findDegreeDays(self,designRegion):
        houseDict = {}
        obj = GetData()
        resp = obj.fetchData(str(designRegion))
        if resp.status_code == 200:
            data = resp.text
            parse_json = json.loads(data)
            degreeDays = parse_json['location']['degreeDays']
            houseDict['designRegion'] = degreeDays
        else:
            houseDict['designRegion'] = None
        return houseDict

