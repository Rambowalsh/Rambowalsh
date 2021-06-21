import sys
sys.path.append(".")
import json
from apiconnection import GetData


filePath = f"C:\\Users\Acer\Documents\evergreenenergy\evergreen-energy-tech-exercise-main\houses.json"


class processdata:


    def findDegreeDays(self):

        obj = GetData()
        with open(filePath) as data_file:    
            jsonObject = json.load(data_file)
        for tag in jsonObject:
            designRegion = tag["designRegion"]
            degreeDays = obj.fetchData(str(designRegion))
            return degreeDays

