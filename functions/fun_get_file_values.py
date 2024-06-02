# get data from file
from functions.helpers.fun_get_arr import getArr

def getFileValues(pathToData):

    tmp = ""
    tmpArr = []

    try:
        file = open(pathToData, "r")

        try:
            for f in file:
                tmpArr += getArr(f, ',')

        except:
            print("Došlo je do greške pri pokušaju čitanja fajla.")
        finally:
            file.close()

    except:
        print("Došlo je do greške pri pokušaju otvaranja dokumenta.")

    return tmpArr

