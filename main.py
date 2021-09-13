import datetime.datetime as date
import random
import os

shipment = open("envios.txt", "rt")
threshold = 50000
vat = 1.21


def log(file_name, text_line):
    log_file = open(file_name, 'a')
    log_file.write(text_line)
    log_file.close()


line = shipment.readline().strip()
while line != "":
    data = line.split("-")

    # log products with code under threshold
    if int(data[0]) < threshold:
        log("menos.txt", data[0] + "-" + data[1] + "\n")

    # log products shipped internationally
    if data[3] != data[5]:
        log("internacionales.txt", "-".join(data) + "\n")

    # calculate VAT
    final_price = float(data[6]) * vat
    log("con_iva.txt", data[1] + "-" + data[7] + "-" + str(final_price) + "\n")

    # generate processed_file
    line_processed = data[0] + "-" + data[1].upper() + "-" + str(date.now()) + "-" + \
                     str(random.randint(1000000000, 9999999999))
    if data[8] == "True":
        line_processed = line_processed + "\n"
    else:
        line_processed = line_processed + "-" + data[6] + "\n"
    log("procesados.txt", line_processed)

    line = shipment.readline().strip()

shipment.close()
