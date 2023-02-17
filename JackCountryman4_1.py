import re, csv

def main():
    #opening file, reading from file, then closing
    file = open('lab 4/input.txt', 'r+')
    split = file.readlines()
    file.close()

    #assigning lists from parse function
    SenderLines, XDSPAMLines = inputParse(split)

    #declaring freq dictionary to keep track of emails from each email and cutting lists
    frequency = {}
    SenderLines = [i[6:-1] for i in SenderLines]
    XDSPAMLines = [i[:-1] for i in XDSPAMLines]

    #for loop to change list with all emails to dictionary with frequency count
    for i in SenderLines:
        if frequency.get(i):
            frequency [i] += 1
        else:
            frequency [i] = 1

    #Calling FreqOut func to open and store contents of freq in output file.
    FreqOut(frequency)
    XDOut(XDSPAMLines)

#Parses file output and sorts lines based on certain criteria into two lists
def inputParse(split):
    SenderLines = []
    XDSPAMLines = []
    for line in split:
        send = re.search("^From:", line)
        spam = re.search("^X-DSPAM-Confidence:", line)
        if send:
            SenderLines.append(line)
        if spam:
            XDSPAMLines.append(line)
    return SenderLines, XDSPAMLines

#Formats and writes freq of emails to output.csv in current dir
def FreqOut(Freq):
    with open('output.csv', mode='w', newline='') as csvfile:
        out_writer = csv.writer(csvfile, delimiter=",")
        out_writer.writerow(['Email', 'Count'])
        for i in Freq:
            out_writer.writerow([i, Freq[i]])
        out_writer.writerow(['TOTAL', sum(Freq.values())])

#handles xdspam out and places in file inside of files dir
def XDOut(XD):
    nums = []
    with open('Lab 4/files/output.txt', 'w+') as file:
        print(XD)
        for i in XD:
            file.write(f'{i}\n')
            nums.append(float(i[20:]))
        file.write('-------------------------------------------------\n')
        file.write(f'Total dspam confidence = {sum(nums):.2f}\n')
        file.write(f'Average dspam confidence = {(sum(nums)/len(nums)):.2f}')


#checks if main script or not
if __name__ == "__main__":
    main()
