import os
import requests
import yaml

# get aoc data by number of task
def getData(taskNumber):

    # helper vars
    task = "{}.txt".format(taskNumber)
    workingDir = os.path.dirname(__file__)
    taskFile = os.path.join(workingDir, task)

    # load task from disc or adventofcode.com
    if (os.path.exists(taskFile)):
        data = open(taskFile, "r").read()
    else:
        # join path for working dir and yaml file with session id 
        sessionFile = os.path.join(workingDir, "aoc-2021.yaml")
        # session id
        with open(sessionFile) as file:
            session = yaml.safe_load(file).get("session")
        # task adress
        url = "https://adventofcode.com/2021/day/{}/input".format(taskNumber)
        data = requests.get(url, cookies={'session': session}).text
        open(taskFile.format(taskNumber), "w").write(data)
    
    # split data by new line char and return
    return data.split("\n")[:-1]