# Task 25-Capstone Project IV - Lists, Functions, and String Handling

# About the task:
# Create a program called, ‘SickleCellDisease.py’. You will simulate the effects of the Single Nucleotide Polymorphism that leads to this genetic disease.
# Write a function called ‘translate’ that, when given a DNA sequence of arbitrary length, the program identifies and returns the amino acid
# sequence of the DNA using the amino acid SLC code found in that table.
#    E.g. DNA Input: ATTATTATT
#    Output: III (representing: Isoleucine, Isoleucine, Isoleucine )
# There are many different amino acids, so this may get a bit repetitive. Just do the first five Amino Acids (i.e I, L, V, F M). Print any other codon as the
# amino acid 'X' . So basically, you would use an if - elif - elif .... else structure to translate each codon of DNA into the correct Amino Acid.
# Note that the program must be able to handle DNA sequences that are not of a length divisible by 3.
#    Hint:
#    len(DNA) - (Will return the length of a String)
#    DNA[0:3] - (Will get the first 3 characters of the string stored in DNA num = 3)
#    DNA[0:num] - (This will work too!)

# Function to translate DNA codons to SLC
# Task 1
def translate(dnaSequence):
    dnaList = []
    slc = ""
    amino = ""
    # Addming the DNA string into a list evenly of 3 char each
    dnaList = textwrap.wrap(dnaSequence, 3)
    # Checking each DNA if found in the DNA codons
    for dna in dnaList:
        if len(dna) != 3:
            dnaList.pop()
        elif dna == "ATT" or dna == "ATC" or dna == "ATA":
            slc = slc + "I"
            amino = amino + " Isoleucine"
        elif dna == "CTT" or dna == "CTC" or dna == "CTA" or dna == "CTG" or dna == "TTA" or dna == "TTG":
            slc = slc + "L"
            amino = amino + " Leucine"
        elif dna == "GTT" or dna == "GTC" or dna == "GTA" or dna == "GTG":
            slc = slc + "V"
            amino = amino + " Valine"
        elif dna == "TTT" or dna == "TTC":
            slc = slc + "F"
            amino = amino + " Phenylalanine"
        elif dna == "ATG":
            slc = slc + "M"
            amino = amino + " Methionine"
        else:
            slc = slc + "X"
            amino = amino + " X"
        dnaSequence = slc
    return dnaSequence + " (representing: " + amino

def mutate():
    try:
        # Open current DNA.TXT file and read the content to a file
        dnaFile = open('DNA1.txt', 'r')
        dnaContent = dnaFile.read()
        dnaFile.close()

        # Replace the 'a' with 'A'
        dnaContentA = dnaContent.replace("a", "A")
        # Writing change to a new file
        normalDNAfile = open('normalDNA.txt', 'w')
        normalDNAfile.write(dnaContentA)
        normalDNAfile.close()

        # Replace the 'a' with 'T'
        dnaContentT = dnaContent.replace("a", "T")
        # Writing change to a new file
        mutatedDNAfile = open('mutatedDNA.txt', 'w')
        mutatedDNAfile.write(dnaContentT)
        mutatedDNAfile.close()

    except FileNotFoundError:
        print("File not fould, please open the folder to run the program!")

    finally:
        # Close open files
        if not dnaFile.closed:
            dnaFile.close()
            normalDNAfile.close()
            mutatedDNAfile.close()

def txtTranslate():
    try:
        # Open the file normalDNA to read
        dnaFile = open('normalDNA.txt', 'r')
        dnaSequence = dnaFile.read()
        dnaFile.close()
        # Calling the translate function, passing data from the file to the function for results
        print("The SLC output for normalDNA.txt is:\n------------------------------------\n", translate(dnaSequence))

        # Open the file mutatedDNA to read
        dnaFile = open('mutatedDNA.txt', 'r')
        dnaSequence = dnaFile.read()
        dnaFile.close()
        # Calling the translate function, passing data from the file to the function for results
        print("\nThe SLC output for mutatedDNA.txt is:\n-------------------------------------\n", translate(dnaSequence))
    
    except FileNotFoundError:
        print("File not fould, please open the folder to run the program!")

    finally:
        if not dnaFile.closed:
            dnaFile.close()

# To user the .wrap on a string to split into 3 char each
import textwrap

mutate()
txtTranslate()
