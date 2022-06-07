with open('thamgia.csv', 'r+') as f:
    myDataList = f.readlines()
    print(myDataList)

    for line in myDataList:
        print(line)
        entry = line.split(',')
        print(entry[0])