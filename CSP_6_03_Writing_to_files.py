import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    word = open(fileName, "w")
    for i in range(len(inputList)):
        if i != len(inputList)-1:
            word.write(f"{inputList[i]}\n")
        if i == len(inputList)-1:
            word.write(inputList[i])

writeFile(["This", "is", "here"], "inputWords.txt")
def sortNames(fileName, targetFile):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    # order = open(fileName, "r")
    # sorting = []
    # for i in order:
    #     sorting.append(order.readline())
    #     sorting.sort()
    # print(sorting)
    with open(fileName, "r") as f:
        names = [line.strip() for line in f if line.strip()]

    names.sort()

    with open(targetFile, "w") as f:
        for name in names:
            f.write(name + "\n")

    print(f"Sorted names written to '{targetFile}': {names}")



def highScore( newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    # score = open(newScore,"a")
    # read = score.read()
    with open("scores.txt", "a") as f:
        f.write(str(newScore) + "\n")

    with open("scores.txt", "r") as f:
        scores = [int(line.strip()) for line in f if line.strip()]

    average = sum(scores) / len(scores)
    print(f"New score: {newScore} | All scores: {scores} | Average: {average:.2f}")
    return average

highScore(random.randint(1,100))

