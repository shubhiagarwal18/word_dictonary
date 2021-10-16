import time

while True:
    start_time = time.time()
    with open('list.txt', 'r') as document:
        wrd_dictonary = {}
        for line in document:
            line = line.split()
            if not line:
                continue
            wrd_dictonary[line[0]] = line[1:]

    word = input("Enter the word: ")    

    if word==' ' or len(word)==0 or word.isdigit():
        print("Enter a valid word")
    else:
        if word in wrd_dictonary:
            print(word)
            end_time = time.time()
            print('Searching done in: ', end_time-start_time)
        else:
            print('No relevant word found')



    
