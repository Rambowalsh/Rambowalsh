from processdata import ProcessData
import json
import os

def main():
    runreport()

             
def runreport():
    filePath = f"C:\\Users\Acer\Documents\evergreenenergy\evergreen-energy-tech-exercise-main\houses.json"
    outFilePath = f"C:\\Users\Acer\Documents\evergreenenergy\report.txt"
    runningTotal = 0
    vat = 0.20
    obj = ProcessData()
    f = open('report.txt', "a")
    with open(filePath) as data_file: 
        jsonObject = json.load(data_file)
        for tag in jsonObject:  
            designArea = tag["designRegion"]
            degreeDaysbyRegion = obj.findDegreeDays(designArea)
            floorArea = tag["floorArea"]
            heatingFactor = tag["heatingFactor"]
            insolationFactor = tag["insulationFactor"]
            degreeDaysbyRegionValue = degreeDaysbyRegion.get('designRegion')
            f.write(tag["submissionId"] + '\n')
            if type(degreeDaysbyRegionValue) == int or float and degreeDaysbyRegionValue is not None:
                heatLoss = obj.calculateHeatLoss(floorArea,heatingFactor,insolationFactor)
                powerLoss = obj.calculatePowerHeatLoss(heatLoss,degreeDaysbyRegion.get('designRegion'))
                rightPump =findrightpump(powerLoss)
                f.write("Estimated Heat Loss = " + str(heatLoss) + '\n') 
                f.write("Design Region = " + str(designArea) + '\n')
                f.write("Power Heat Loss = " + str(powerLoss) + '\n')
                f.write("Recommended Heat Pump = " + str(rightPump[1]) + '\n')
                for entry in enumerate(rightPump[0]):
                    label = str(entry[1]['label'])
                    cost = str(entry[1]['cost'])
                    f.write(label + "|" + "Cost =" + cost + '\n')
                    runningTotal = runningTotal + float(cost)
                runningTotal = runningTotal + (runningTotal / vat)
                f.write("Total Cost, including VAT =  " + str(runningTotal) + '\n')
                f.write(" " + '\n')
                f.write(" " + '\n')
                f.write("-------------------------------" + '\n')
                runningTotal=0
            else:
                f.write ('Warning: Could not find design region' + '\n')
                f.write(" " + '\n')
                f.write(" " + '\n')
                f.write("-------------------------------" + '\n')
        f.close
  
def findrightpump(powerLoss):
    filePath = f"C:\\Users\Acer\Documents\evergreenenergy\evergreen-energy-tech-exercise-main\heat-pumps.json"
    rightPump = []
    rightPumpText = ""
    lastOutPutCapacity = 100
    with open(filePath) as data_file: 
        jsonObject = json.load(data_file)
        for tag in jsonObject:
            outputCapacity = tag["outputCapacity"]
            if (outputCapacity > powerLoss) and (outputCapacity < lastOutPutCapacity):
                rightPump = tag["costs"]
                lastOutPutCapacity = outputCapacity
                rightPumpText = tag["label"]
        return [rightPump,rightPumpText]

if __name__ == "__main__":
    main()