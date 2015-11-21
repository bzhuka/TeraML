import json
import numpy as np
import scipy.io as spl

def getDict(string):
    dictlist = json.loads(string)
    return dictlist
def getArray(dictlist):
    list = []
    for num,index in enumerate(dictlist):
        list.append([])
        for num2,j in enumerate(index):
            list[num].append(index[j])
    return list

if __name__ == "__main__":
    dictlist = getDict('{"data":[{"Year":1325307600000,"Total Murders":12664,"Total by Firearms":8583,"Handguns":6220,"Rifles":323,"Shotguns":356,"Other guns":97,"Firearms, type not stated":1587,"Knives":1694,"Blunt objects":496,"Personal weapons":728,"Poison":5,"Explosives":12,"Fire":75,"Narcotics":29,"Drowning":15,"Strangulation":85,"Asphyxiation":89,"Other":853},{"Year":1293771600000,"Total Murders":13164,"Total by Firearms":8874,"Handguns":6115,"Rifles":367,"Shotguns":366,"Other guns":93,"Firearms, type not stated":1933,"Knives":1732,"Blunt objects":549,"Personal weapons":769,"Poison":11,"Explosives":4,"Fire":78,"Narcotics":45,"Drowning":10,"Strangulation":122,"Asphyxiation":98,"Other":872},{"Year":1262235600000,"Total Murders":13752,"Total by Firearms":9199,"Handguns":6501,"Rifles":351,"Shotguns":423,"Other guns":96,"Firearms, type not stated":1828,"Knives":1836,"Blunt objects":623,"Personal weapons":817,"Poison":7,"Explosives":2,"Fire":98,"Narcotics":52,"Drowning":8,"Strangulation":122,"Asphyxiation":84,"Other":904},{"Year":1230699600000,"Total Murders":14224,"Total by Firearms":9528,"Handguns":6800,"Rifles":380,"Shotguns":442,"Other guns":81,"Firearms, type not stated":1825,"Knives":1888,"Blunt objects":603,"Personal weapons":875,"Poison":9,"Explosives":11,"Fire":85,"Narcotics":34,"Drowning":16,"Strangulation":89,"Asphyxiation":87,"Other":999},{"Year":1199077200000,"Total Murders":14916,"Total by Firearms":10129,"Handguns":7398,"Rifles":453,"Shotguns":457,"Other guns":116,"Firearms, type not stated":1705,"Knives":1817,"Blunt objects":647,"Personal weapons":869,"Poison":10,"Explosives":1,"Fire":131,"Narcotics":52,"Drowning":12,"Strangulation":134,"Asphyxiation":109,"Other":1005}]}')
    #print(dictlist["data"])
    array = getArray(dictlist["data"])
    array = np.array(array)
    #print(array)
    spl.savemat("mat1.mat", {"X":array})