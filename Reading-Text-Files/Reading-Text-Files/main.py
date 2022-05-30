def count_words():
    with open("./story.txt", "r") as openFile:
        read_file= openFile.read()
        print(read_file)
        words = read_file.split()
        print(len(words))
        
        count ={}
        for i in words:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return count


print(count_words())