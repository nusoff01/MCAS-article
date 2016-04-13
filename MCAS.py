# MCAS.py
# created by: Nick Usoff

import csv






# extract_scores: takes in a name of a CSV file with school districts and 
#                 MCAS scores and extracts Math scores, and returns a list
#                 with the format (districtName, numPandA, percentPandA)

def extract_scores (csvFileName):
    mathScoreDict = {}
    with open(csvFileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Subject'] == "MTH":
                mathScoreDict[row['Org Code'].zfill(8)] = (("num passing", row['P+A #']), 
                    ("percent passing", row['P+A %']), ("num taking test", row["Stud. Incl. #"]))

    return mathScoreDict

# extract_demographics: takes in a name of a csv file with school district and
#                       class size/demographics info and returns a dictionary
#                       with the demographic data for each district

def extract_demographics (csvFileName):
    demList = []
    demDict = {}
    with open(csvFileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            districtTup = (("name", row["DISTRICT"]),
                           ("class_size", row["Average Class Size"]))
            demDict[row['Org Code'].zfill(8)] = districtTup
    return demDict

# extract_funding: takes in a name of a CSV file with school districts and 
#                  functing data and extracts funding data, and returns a 
#                  dictionary with the funding data for each district

def extract_funding (csvFileName):
    fundingList = []
    fundingDict = {}
    with open(csvFileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            districtTup = (("name", row['District']), 
                           ("total spent", cleanCost(row['Total Expenditures'])), 
                           ("per student spent", cleanCost(row['Expenditure Per Pupil'])))
            fundingDict[row['Org Code'].zfill(8)] = districtTup
    return fundingDict


# combineDistrictInfo: takes in a list of districtInfo dictionaries, and 
#                      creates a new dictionary where the info from each
#                      dictionary is inserted into the new dictionary. This
#                      new dictionary is then returned.

def combineDistrictInfo (districtInfoList):
    districtInfo = {}
    numHits = 0
    numMisses = 0
    print("number of elements in districtInfoList: " + str(len(districtInfoList)))
    for dInfoCurr in districtInfoList:
        for dNum in dInfoCurr:
            # print("curr dNum: " + dNum)
            if districtInfo.get(dNum) == None:

                numMisses += 1
                districtInfo[dNum] = dInfoCurr[dNum]
            else:
                currD = districtInfo[dNum] + dInfoCurr[dNum]
                numHits += 1
                districtInfo[dNum] = currD

    # print("number of hits: " + str(numHits))
    # print("number of misses: " + str(numMisses))
    return districtInfo
                # add values of the current dictionary to the current object 
                # in disctrictInfo



############################### UTILITIES #####################################

def cleanCost (costStr):
    return costStr.replace(" ", "").replace("$", "").replace(",","")

def printDict (dict):
    for key in dict:
        print(key, dict[key])

    print("number of entries in the dictionary: " + str(len(dict)))


numEntriesExpected = 8
def printFinalDict (dict):
    num_total = 0
    for key in dict:
        if(len(dict[key]) == numEntriesExpected):
            num_total += 1
            # print(key, dict[key])
            print("{x: "+ dict[key][7][1] + ", y: " 
                  + dict[key][4][1] + ", name: \"" + dict[key][0][1]
                  + "\"},")
    print("number total " + str(num_total))

# takes in a list and an index of an element used to sort the list


# def extractLowestHighest ()


###############################################################################

# extract disctionaries
scoreDict = extract_scores("MCAS.csv")
fundingDict = extract_funding("funding_data.csv")
dem_dict = extract_demographics("demographics.csv")

districtList = [fundingDict, scoreDict, dem_dict]
districtInfo = combineDistrictInfo(districtList)



printFinalDict(districtInfo)