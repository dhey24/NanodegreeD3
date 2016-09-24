# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:13:27 2016
For Nanodegree d3 project

@author: dhey2
"""
import csv
import pprint

filepath = "./SOUTH.csv"

states = []
regions = []

with open(filepath, "rU") as infile:
    reader = csv.reader(infile, dialect=csv.excel_tab, delimiter = ",")
    reader.next()
    row = reader.next()
    
    #states are in columns 7 : 30
    #Census region of respondent is in columns 49 : 57
    for c in range(6, 31):
        states.append(row[c])
    for c in range(49, 58):
        regions.append(row[c])
    #add unknown region for those who did not answer
    regions.append("No Response")
    
    #create a nice handy way to store responses per region
    dataDict = {region: {key: 0 for key in states} for region in regions}
    
    for row in reader:
        region = ""
        for c in range(49, 58):
            if row[c] <> "":
                region = row[c]
        if region == "":
            region = "No Response"
        
        for c in range(6,31):
            if row[c] <> "":
                dataDict[region][row[c]] += 1
                
    pprint.pprint(dataDict)
    
    header = ["Region", "State", "Votes"]
    dataList = []
    for region in regions:
        for state in states:
            dataList.append([region, state, dataDict[region][state]])
        
    with open("./SOUTH_transformed_2.csv", "wb") as outfile:
        writer = csv.writer(outfile, delimiter = ',')
        writer.writerow(header)
        for row in dataList:
            writer.writerow(row)
        