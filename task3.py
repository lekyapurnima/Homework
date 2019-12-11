import sys
import os


""" Anotating the chromosome along with its coordinates to a gene name from reference file.
"""


def remove_dup(annot_file):
    """Remove the duplicates if any present in the input file to enhance the script functionality.

    Args:
        annot_file (str): The file used for annotation

    Returns: the unique list without duplicates
    """
    with open(annot_file, 'r') as inp:
        to_annot = inp.readlines()
        new_list = []
        for line in to_annot:
            chrm_l = line.rstrip().split("\t")
            if chrm_l not in new_list:
                new_list.append(chrm_l)
        return(new_list)


def lookup(input_list, annot_f):
    """Lookup of the gene name associated with the input file chromosome and its position.

    Args:
        input_list (list): The unique list of input file
        annot_file (str): The file with annotations

    Returns: Tab separated output file with chromosome , position and its associated gene name.
    """
    with open(annot_f, 'r') as ref:
        annot_file = ref.readlines()
        with open("output.tsv", "w") as out:
            for line in input_list:
                for line1 in annot_file:
                    gtf_l = line1.rstrip().split("\t")
                    if line[0] == gtf_l[0] and int(gtf_l[3]) <= int(line[1]) <= int(gtf_l[4]):
                        feature = str(gtf_l[8:])
                        gene_name = feature.split(";")[-2].split(" ")[2]
                        outp = (line[0]+"\t"+line[1]+"\t"+gene_name+"\n")
                        out.write(outp)


def main():
    """Call the functions uniq_input & lookup
    """
    # Using try and except to open the files
    try:
        inp_file, ref_file = "", ""
        inp_file = sys.argv[1]
        ref_file = sys.argv[2]
    except IndexError:
        if not input_file or ref_file:
            print("Please give an input file and annotations file")
            sys.exit()
        if not os.path.exists(input_file):
            print("Please provide a valid input file")
            sys.exit()
        if not os.path.exists(ref_file):
            print("Please provide a valid reference file")
            sys.exit()
    # Calling the functions
    uniq_input = remove_dup(inp_file)
    lookup(uniq_input, ref_file)


if __name__ == "__main__":
    main()
