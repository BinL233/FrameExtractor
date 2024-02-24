import extractor

def main():
    path = input("Folder path: ")
    currRate = int(input("Current frame rate: "))
    targetRate = int(input("Target frame rate: "))


    while currRate <= targetRate:
        print("Target frame rate must larger than Current frame rate.")
        currRate = int(input("Current frame rate: "))
        targetRate = int(input("Target frame rate: "))
    
    print("Start extracting...")

    op = extractor.extract(path, currRate, targetRate)

    if op:
        print("Success!")
    else:
        print("Failed")

if __name__ == "__main__":
    main()