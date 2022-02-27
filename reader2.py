import sys
import csv
import os
import pickle
import json
from pathlib import Path

brain = []


class CheckFiles:
    def __init__(self, src=None, dst=None):
        if not src:
            src=sys.argv[1]
        if not dst:
            dst=sys.argv[2]
        self.src = src
        self.dst = dst
        self.brain = []

    def file_exists(self):
        if os.path.exists(self.src):
            print("input file exists")
        if os.path.exists(self.dst):
            print("output file exists")
        else:
            print('No input or output file.Files in directory:')
            directory = list(os.listdir())
            print(directory)
            sys.exit()

    def sysargv3read(self):
        for changes in sys.argv[3:]:
            par = changes.split(",")
            row = int(par[0])
            column = int(par[1])
            value = ",".join(par[2:])
            self.brain[row][column]=value


class CsvRead(CheckFiles):

    def read(self):
        with open(self.src, "r", newline="") as f:
            reader = csv.reader(f)
            for line in reader:
                self.brain.append(line)


class CsvWrite(CheckFiles):
    # def __init__(self):
    # self.brain = []
    def write(self):
        with open(self.dst, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for line in self.brain:
                writer.writerow(line)


class PickleRead(CheckFiles):

    def read(self):
# with open(self.src, "rb", newline="", encoding="utf-8") as file:
        with open(self.src, "rb") as file:
            self.brain = pickle.loads(file.read())


class PickleWrite(CheckFiles):


    def write(self):
        with open(self.dst, "wb") as file:
#       with open(self.dst, "wb", newline="", encoding="utf-8") as file:
            file.write(pickle.dumps(self.brain))

class JsonRead(CheckFiles):
# def __init__(self):
# pass

    def read(self):
        with open(self.src, "r", newline="", encoding="utf-8") as file:
            reader = json.loads(file.read())
            self.brain = reader


class JsonWrite(CheckFiles):
# def __init__(self):
# pass

    def write(self):
        with open(self.dst, "w", newline="", encoding="utf-8") as file:
            file.write(json.dumps(self.brain))


src = sys.argv[1]
check = Path(src)
if check.match("*.json") is True:
    reader = JsonRead
if check.match("*.csv") is True:
    reader = CsvRead
if check.match("*.pickle") is True:
    reader = PickleRead

dst = sys.argv[2]
check = Path(dst)
if check.match("*.json") is True:
    writer = JsonWrite
if check.match("*.csv") is True:
    writer = CsvWrite
if check.match("*.pickle") is True:
    writer = PickleWrite


class Change(reader, writer):
    pass

obj = Change()
obj.read()
obj.sysargv3read()
obj.write()


