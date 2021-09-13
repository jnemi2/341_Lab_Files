import os

packages = open("envios.txt", "rt")

line = packages.readline()
while line != "":
    data = line.split("-")
    print(data)
    line = packages.readline()

packages.close()
