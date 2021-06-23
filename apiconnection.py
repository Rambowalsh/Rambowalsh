import requests



class GetData:  

    def fetchData(self,designArea):
        url = f"https://063qqrtqth.execute-api.eu-west-2.amazonaws.com/v1/weather?location={designArea}"
        header={"x-api-key": "f661f74e-20a7-4e9f-acfc-041cfb846505"}
        getResponse = requests.get(url,headers=header)
        return getResponse