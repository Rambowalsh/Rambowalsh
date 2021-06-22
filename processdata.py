import sys
sys.path.append(".")
import json
from apiconnection import GetData


class ProcessData:

    def calculateHeatLoss(self, floorArea,heatingFactor, insulationFactor):
        heatLoss = floorArea  * heatingFactor * insulationFactor
        return heatLoss

    def calculatePowerHeatLoss(self, heatLoss, heatingDegrees):
        powerHeatLoss = heatLoss / heatingDegrees 
        return powerHeatLoss

    def findDegreeDays(self,filePath):
        houseDict = {}
        obj = GetData()
        with open(filePath) as data_file:    
            jsonObject = json.load(data_file)
        for tag in jsonObject:
            designRegion = tag["designRegion"]
            degreeDays = obj.fetchData(str(designRegion))
            houseDict['designRegion'] = tag["degreeDays"]
        return houseDict

