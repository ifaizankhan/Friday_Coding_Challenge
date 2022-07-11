import json

def hasNumber(inputString):
    return any(char.isdigit() for char in inputString)


def string_to_json(input):

    #Creating dictonary to store output values
    output = dict()

    ## Considering some of the cases had comma in the address line
    #Spliting string with comma
    commaSplits = input.split(',')

    #checkign 
    if len(commaSplits)>1:
        if hasNumber(commaSplits[0]):
            output["street"] = commaSplits[1].strip()
            output["housenumber"] = commaSplits[0].strip()
        else:
            output["street"] = commaSplits[0].strip()
            output["housenumber"] = commaSplits[1].strip()

    else:
        #Spliting string with comma
        spaceSplits = input.split(' ')
        numberIndex = dict()


        for splitstr in spaceSplits:
            if hasNumber(splitstr):
                numberIndex[spaceSplits.index(splitstr)]= spaceSplits.index(splitstr)
        
        numberSplitCount = len(numberIndex.keys())
        
        if numberSplitCount==1:
            startingIndexHouseNumber = int(list(numberIndex.keys())[0])
            
            if startingIndexHouseNumber==0:
                output["street"] = (' '.join(spaceSplits[1:])).strip()
                output["housenumber"] = spaceSplits[0]
            else:
                output["street"] = (' '.join(spaceSplits[0:startingIndexHouseNumber])).strip()
                output["housenumber"] = (' '.join(spaceSplits[startingIndexHouseNumber:])).strip()

        else:
            startingIndexHouseNumber = int(list(numberIndex.keys())[1])
            endingIndexStreet = int(list(numberIndex.keys())[0])
            output["street"] = (' '.join(spaceSplits[0:endingIndexStreet+1])).strip()
            output["housenumber"] = (' '.join(spaceSplits[endingIndexStreet+1:])).strip()

        
    jsonoutput = json.dumps(output)

    return jsonoutput

input = input("Please enter an address: ")

output = string_to_json(input)
print (output)