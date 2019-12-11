import sys


"""Printing the top ten repeated sequences along with its count in a given fasta file
"""


def count_sequence(fasta_file):
    """Counting the number of times a sequence is repeated and giving it to a dictionary with keys as sequence and
        value is the repeat counts of the sequence in the file

    Args:
        fasta_file (str): The inputted fasta file

    Returns: Dictionary variable(counts) with sequence and its count
    """
    with open(fasta_file) as fa:
        fasta = fa.readlines()
        counts = dict()
        for count, seq in enumerate(fasta):
            seq = seq.rstrip()
            if count % 2 == 1:
                if seq in counts:
                    counts[seq] += 1
                else:
                    counts[seq] = 1
        return(counts)


def main():
    """Call the function count_sequence.

    Returns: Printing the top 10 most repeated sequence along with its count
    """
    # Using try and except to open the file
    try:
        file_name = ""
        file_name = sys.argv[1]
    except FileNotFoundError:
        print("Please provide a valid input file path/file")
        sys.exit()
    except IndexError:
        if not file_name:
            print("Please give an input fasta file")
            sys.exit()

    seq_counts = count_sequence(file_name)
    print({key: seq_counts[key] for key in sorted(seq_counts, key=seq_counts.get, reverse=True)[:10]})


if __name__ == "__main__":
    main()
