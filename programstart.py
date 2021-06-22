from processdata import ProcessData
import json

def main():
    runreport()

             
def runreport():
    filePath = f"C:\\Users\Acer\Documents\evergreenenergy\evergreen-energy-tech-exercise-main\houses.json"
    obj = ProcessData()
    degreeDaysbyRegion = obj.findDegreeDays(filePath)
    with open(filePath) as data_file: 
        jsonObject = json.load(data_file)
        for tag in jsonObject:  
            designArea = tag["designArea"]
            floorArea = tag["floorArea"]
            heatingFactor = tag["heatingFactor"]
            insolationFactor = tag["insolationFactor"]
            heatLoss = obj.calculateHeatLoss(floorArea,heatingFactor,insolationFactor)
            powerLoss = obj.calculatePowerHeatLoss(heatLoss,degreeDaysbyRegion.get(designArea)
    

if __name__ == "__main__":
    main()