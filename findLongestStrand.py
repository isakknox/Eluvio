
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.1', 'rb')
output1 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.2', 'rb')
output2 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.3', 'rb')
output3 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.4', 'rb')
output4 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.5', 'rb')
output5 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.6', 'rb')
output6 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.7', 'rb')
output7 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.8', 'rb')
output8 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.9', 'rb')
output9 = a.read()
a = open(r'C:\Users\isakk\Documents\Eluvio Challenge\sample_files\sample.10', 'rb')
output10 = a.read()
outputArray = [output1, output2, output3, output4, output5,
output6, output7, output8, output9, output10]
namesArray = []
offsetArray = []

# check whether inserted strand is found in two files at least

def multipleFiles(start, strand, dataArray):
    if len(strand) < 1:
        return False
    present = 0
    counter = 0
    for string in dataArray:
        if counter == start:
            counter += 1
            continue
        if strand in string:
            present += 1
            if present == 1:
                namesArray.clear()
                offsetArray.clear()
            namesArray.append(counter + 1)
            offsetArray.append(string.find(strand))
        counter += 1
    if present > 0:
        return True
    return False

# go through each string in the array and find every strand 
# and then check whether its longer than the current 
# longest found strand and also whether it is found in at least
# one other file

def findStrand(stringArray):
    global namesArray
    global offsetArray
    strand = ''
    for i in range(len(stringArray)):
        for j in range(len(stringArray[i])):
            for k in range(len(stringArray[i]) - j + 1):
                if k > len(strand) and multipleFiles(i, stringArray[i][j:j+k], stringArray):
                    strand = stringArray[i][j:j+k]
                    # add the number of the file and offset 
                    # of where the strand starts
                    namesArray.append(i + 1)
                    offsetArray.append(j)
    return strand
# Uncomment below to have the actual longest strand printed out
#print(findStrand(outputArray))
# Print out the strand length
print('Strand Length: ' + str(len(findStrand(outputArray))))
# Sort the file by number for best presentation
namesCopy = namesArray.copy()
namesCopy.sort()
# Present the name of each file which contains the longest strand 
# and the corresponding offset where the strand is found
for i in range(len(namesArray)):
    print('sample.' + str(namesCopy[i]) + ':' + ' ' + str(offsetArray[namesArray.index(namesCopy[i])]))

