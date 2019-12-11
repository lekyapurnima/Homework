1. What does ls -alt do?
A. ls function when applied on a given directory,lists all the files present in that directory.
-   ls parameters:
            - a - list all the files in the directory including the hidden files
            - l - list in long format. The following information is displayed for each file:
                        file mode, number of links, owner name, group name, number of bytes in the
                        file, abbreviated month, day-of-month file was last modified, hour file last modified, minute file last modified, and the pathname.
            - t - lists all the files in the sorted order based on the time modified with most recently modified first



2. What command would you use to list all files starting with 'Run' and ending with '.txt' in a directory and all of its subdirectories?
A. find . -type f -name "Run*.txt"
  This command finds and lists all the files starting with "Run" and ending with ".txt" from current directory. This works recursively and looks into all the directories and subdirectories from the current directory.


3. How would you append the contents of 'exampleFile1.txt' to 'exampleFile2.txt'?
A. cat exampleFile1.txt >> exampleFile2.txt
    This command with append all the contents of exampleFile1.txt to exampleFile2.txt without overwriting the contents of exampleFile2.txt


4. How would you (1) sort the contents of 'exampleFile1' and (2) redirect the sorted content to 'exampleFile2.txt' in one line using the pipe operator?
Not sure how to implement a pipe when can be done with ">" symbol.
A. sort exampleFile1 > exampleFile2.txt



5. Which commands would you use to find files whose name match a certain pattern, and to find files containing a certain text?
A. "grep" command can find files with a matching pattern along with files containing certain text.


SQL:
1. For the following SQL statement, what is wrong with it and how would you fix it:
-- Question:
SELECT UserId, AVG(Total) AS AvgOrderTotal
FROM Invoices
HAVING COUNT(OrderId) >= 1

The query below gives an average order of a customer.
A. SELECT UserId, AVG(Total) AS AvgOrderTotal
    FROM Invoices
    GROUP BY Userid
    HAVING COUNT(OrderId) >= 1


Bioinformatics tasks:
All the tasks are written with a command line arguement so no file is hardcoded within the code.
Arguement for task 1: python3 task1.py fastq/read1/   python3 task1.py fastq/read2/
Arguement for task 2: python3 task2.py fasta/sample.fasta 
Arguement for task 3: python3 task3.py annotate/coordinates_to_annotate.txt gtf/hg19_annotations.gtf
For task 3, the output has a lot of repitions which is not an effective way and can be condensed to only unique values but since that is not mentioned in the question, didn't want to mess it up. Output is in output.tsv present in the folder for viewing the output created.


#Added this new line before committing the new changes to github.