import os
import numpy as np
import math
import requests
import yaml

# get config data 
def getConfigData(configFile = 'adventofcode.yaml'):

    # load yaml file
    with open(configFile) as f:
        data = yaml.load(f)
        print(data)

    # return data (as dictionay)
    return data

# get input data by number
def getData(number):

    # define filename
    workingDir = os.path.dirname(__file__)
    fileName = "input-{}.txt".format(number)
    filePath = os.path.join(workingDir, fileName)

    data = ""
    fileId = ""

    # load file from disc if exists otherwise get it from adventofcode.com
    if (os.path.exists(filePath)):
        fileId = open(filePath, "r")
        data = fileId.read()
    else:
        data = downloadData(number)
        fileId = open(filePath.format(number), "w")
        fileId.write(data)

    fileId.close()

    # format data and return
    return data.split("\n")[:-1]

# download input data by number
def downloadData(number):

    # define filename
    workingDir = os.path.dirname(__file__)
    filePath = os.path.join(workingDir, "adventofcode.yaml")

    # get data using requests library and session id stored in config file
    session = getConfigData(filePath).get("session")
    uri = "https://adventofcode.com/2020/day/{}/input".format(number)
    response = requests.get(uri, cookies={'session': session})
    return response.text

# rotation of p around c by degrees
def rotate(p: [int, int], c: [int, int], degrees: int) -> [int, int]:

    # degrees in radian
    phi = degrees * (math.pi/180)

    # rotation matrix
    m_rot = [[math.cos(phi), -(math.sin(phi))], [math.sin(phi), math.cos(phi)]]

    # translation
    m_trans = np.subtract(p, c)

    # rotated p
    p_rot = np.dot(m_rot, m_trans)

    # rotated and translated p
    p_rot_trans = np.add(c, p_rot)

    return [round(p_rot_trans[0], 2), round(p_rot_trans[1], 2)]
