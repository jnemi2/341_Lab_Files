import os

packages = open("envios.txt", "rt")
threshold = 50000


def log(file_name, text_line):
    log_file = open(file_name, 'a')
    log_file.write(text_line)
    log_file.close()


line = packages.readline().strip()
while line != "":
    data = line.split("-")
    if int(data[0]) < threshold:
        log("menos.txt", "-".join(data) + "\n")
    line = packages.readline().strip()

packages.close()
