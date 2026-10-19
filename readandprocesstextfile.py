try:
    with open("sample.txt", "r") as file:
        lines=file.readlines()
        l=len(lines)
        w=0
        c=0
        for line in lines:
            w=w+len(line.split())
            c=c+len(line)
        print("Text File Statistics")
        print("*************************")
        print("Number of lines:", l)
        print("Number of words:", w)
        print("Number of characters:", c)
except FileNotFoundError:
    print("Error: File not found.")
