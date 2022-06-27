import numpy as np
import plotly.express as px
import csv

def getDataSource(data_path):
 
  coffee_in_ml = []
  sleep_in_hours = []

  with open(data_path) as f:
    csv_reader = csv.DictReader(f)
    print(csv_reader)

    for row in csv_reader:
        print(row)
        coffee_in_ml.append(float(row["Coffee in ml"]))
        sleep_in_hours.append(float(row["sleep in hours"]))

    return {"x" : coffee_in_ml, "y" : sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print('correlation')
    print(correlation)
    print("The correlation is", correlation)


def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "cofee in ml", y = "sleep in hours")
        fig.show()
        


def setup():
    dataPath = "finding-correlation-master/cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(dataPath)
    print(dataSource)
    findCorrelation(dataSource)
    plotFigure(dataPath)
