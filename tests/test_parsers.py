# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def get_filepath(which):
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    if which == "fasta":
        return data_dir / "test.fa"
    else:
        return data_dir / "test.fq"


def open_fastq_reference():
    f = pathlib.Path(__file__).resolve().parent / "fastq-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip().split("|"), f.readlines()))
    return seqs  # will be list of lists with seq, quality that were parsed from the test files using get-seq.sh


def open_fasta_reference():
    f = pathlib.Path(__file__).resolve().parent / "fasta-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip(), f.readlines()))
    return seqs  # will be a list of seqs, quality that were parsed from the test files using get-seq.sh

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """

    """
    try:
        empty_p = FastaParser("empty.fa")
        empty_fasta = {}
        for seq_name, seq in empty_p:
            empty_fasta[seq_name] = seq
        test_empty = False
    except ValueError:
        test_empty = True

    try:
        bad_p = FastaParser("bad.fa")
        bad_fasta = {}
        for seq_name, seq in bad_p:
            bad_fasta[seq_name] = seq
        test_bad = False
    except ValueError:
        test_bad = True

    assert test_empty == True, "FastaParser cannot take an empty fasta file"
    assert test_bad == True, "Input fasta file for FastaParser must be formatted correctly"
    """

    test_fa = FastaParser(get_filepath("fasta"))
    seq_fasta = []
    for seq_name, seq in test_fa:
        seq_fasta.append(seq)

    #with open("~/data/fasta-check.txt") as file:
    #    seq_check = [line.rstrip() for line in file]

    seq_check = open_fasta_reference()

    assert seq_fasta == seq_check, "FastaParser does not parse sequences from fasta file correctly"



def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    test_fq = FastqParser(get_filepath("fastq"))
    seq_fastq = []
    qual_fastq = []
    for seq_name, seq, quality in test_fa:
        seq_fasta.append(seq)
        qual_fastq.append(quality)

    #with open("~/data/fasta-check.txt") as file:
    #    seq_check = [line.rstrip() for line in file]
    #    qual_check
    seq_check = 8
    qual_check = 8

    assert seq_fasta == seq_check, "FastaParser does not parse sequences from fastq file correctly"
    assert qual_fastq == qual_check, "FastaParser does not parse quality scores from fastq file correctly"
