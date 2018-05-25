import sys
import hashlib
import os
import csv

def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128 * md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()

rootdir = "C:/Users/trieu/PycharmProjects/DecisionTree/Src-Virus-Test/"
output = "C:/Users/trieu/PycharmProjects/DecisionTree/md5.csv"

count = 1

csv_file = open(output, "a+")

writer = csv.writer(csv_file, delimiter=',')
writer.writerow(["fileName", "MD5hash"])

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        try:
            fileHash = md5sum(rootdir + '/' + file)
            #fileHash = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
        except Exception as e:
            print ("Error while calculating MD5 for the file", file)
        else:
            print("Writing file number", count)
            writer.writerow([file, fileHash])
            count += 1
    csv_file.close()



