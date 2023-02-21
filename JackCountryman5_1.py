import os.path
import re
import csv

def main():
    #input file checking and storing                        ADD EXCEPTION HANDLING TO TEST FOR MISSING FILE
    file = input('Input file name: ').strip()
    fPath = "files/" + file
    exist = checkFile(fPath)
    while exist == False:
        print("File does not exist!")
        file = input('Input file name: ').strip()
        fPath = "files/"+file
        exist = checkFile(fPath)

    #output file checking and storing
    out = input('Output file name: ').strip()
    oPath = "files/" + out
    finOut = ''
    while finOut == '':
        finOut=getOutput(oPath)
        while finOut == '':
            out = input("New output file name:").strip()
            oPath = "files/" + out
            finOut = getOutput(oPath)

    #parsing through lines of input file to obtain info
    parse = [] 
    with open(fPath, 'r+') as In:
        contents = In.readlines()
        for line in contents:
            send = re.search('^From:', line)
            subj = re.search('^Subject:', line)
            spam = re.search('^X-DSPAM-Confidence:', line)
            if send:
                line = line[6:-1]
                parse.append(line)
            if subj:
                line = line[29:35]
                parse.append(line)
            if spam:
                line = line[-7:-1]
                parse.append(line)

    #output to csv
    with open(finOut, mode='w', newline='') as Out:
        Out_writer = csv.writer(Out, delimiter=',')
        Out_writer.writerow(["Email","Subject","Confidence"])
        for i in range(len(parse))[::3]:
            Out_writer.writerow([parse[i], parse[i+1], parse[i+2]])
    print("Data Stored!")




#checks if file exists, i know it seems useless but I like it better this way
def checkFile(file):
    return os.path.isfile(file)

#logic to test if file exists and output accordingly. easier when you can call this
def getOutput(out):
    exist = checkFile(out)
    while exist == True:
        ow = input('Overwrite existing file (y/n): ').strip().lower()
        while ow != 'y' and ow != 'n':
            ow = input('Enter (y/n): ').strip().lower()
        if ow == 'y':
            return out
        if ow == 'n':
            return ''
    return out




if __name__ == '__main__':
    main()