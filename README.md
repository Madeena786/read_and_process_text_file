### **Task 19 - Read and Process a Text File**

###### 

###### **Description**

This project is a Python program that reads a text file and generates basic statistics from its contents.



The program calculates:

\- Number of lines

\- Number of words

\- Number of characters



It also handles the situation where the input file is missing by using FileNotFoundError exception handling.

###### 

###### **Objective**

To learn Python file handling and text processing using open(), readlines(), split(), and exception handling.



###### **Technologies Used**

\- Python

\- Text File (.txt)

\- Notepad / Python IDLE

###### 

###### **Input File**

File name: sample.txt



**Content:**

I am learning Python.

Python is easy to learn.

I am practicing file handling.



###### **Python Program**



try:

&#x20;   with open("sample.txt", "r") as file:

&#x20;       lines=file.readlines()

&#x20;       l=len(lines)

&#x20;       w=0

&#x20;       c=0

&#x20;       for line in lines:

&#x20;           w=w+len(line.split())

&#x20;           c=c+len(line)

&#x20;       print("Text File Statistics")

&#x20;       print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

&#x20;       print("Number of lines:", l)

&#x20;       print("Number of words:", w)

&#x20;       print("Number of characters:", c)

except FileNotFoundError:

&#x20;   print("Error: File not found.")



###### **Output**



Text File Statistics

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Number of lines: 3

Number of words: 14

Number of characters: 77

###### 

###### **Features**

1\. Reads data from a text file.

2\. Counts the number of lines.

3\. Counts the number of words.

4\. Counts the number of characters.

5\. Handles a missing file using FileNotFoundError.

6\. Uses the with statement to safely open and close the file.



###### **Concepts Learned**

\- File handling

\- open()

\- readlines()

\- len()

\- split()

\- for loop

\- try-except

\- FileNotFoundError



###### **Conclusion**

This project demonstrates how Python can be used to read and process text files. It calculates useful text statistics and handles a missing input file gracefully.

