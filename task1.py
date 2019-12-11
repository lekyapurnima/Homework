import sys
import os


""" Recursively finding all the fastq files in a directory and printing
    percent of sequences in that file that are greater than 30 nucleotides.
"""


def recursive(file_dir):
    """Looping the files in directory and capturing the fasta file
        along with percent of sequence that are greater than 30nt length

    Args:
        fasta (str): The input fasta directory location
    """
    for files in os.listdir(file_dir):
        if files.endswith(".fastq"):
            with open("%s/%s" % (file_dir, files)) as f:
                seq_totalcount, seq_count = 1, 0
                for count, line in enumerate(f):
                    if(count == seq_totalcount):
                        seq_totalcount += 4
                        line = line.rstrip()
                        if (len(line) > 30):
                            seq_count += 1
                print(files, "\t", ((seq_count)/((count+1)/4))*100)


def main():
    """ Capturing the file directory from the command line arguement.
    """
    try:
        file_loc = ""
        file_loc = sys.argv[1]
    except IndexError:
        if not file_loc:
            print("Please give a directory path")
            sys.exit()
        if not os.path.exists(file_loc):
            print("Please provide a valid input directory path")
            sys.exit()

    # Calling the function.
    recursive(file_loc)


if __name__ == "__main__":
    main()
