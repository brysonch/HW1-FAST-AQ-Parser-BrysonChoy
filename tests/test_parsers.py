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


    try:
        empty_p = FastaParser("~/tests/empty.fa")
        test_empty = False
    except ValueError:
        test_empty = True

    try:
        bad_p = FastaParser("~/tests/bad.fa")
        test_bad = False
    except ValueError:
        test_bad = True

    assert test_empty == True, "FastaParser cannot take an empty fasta file"
    assert test_bad == True, "Input fasta file for FastaParser must be formatted correctly"

    seq_fasta, line_fasta = FastaParser("~/data/test.fa")
    seq_txt = Parser("fasta-check.txt")
    assert seq_fasta == seq_txt, "FastaParser does not parse sequences from fasta file correctly"



def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    self.assertRaises(ValueError, FastqParser("bad.fa"))
    self.assertRaises(ValueError, FastqParser("empty.fa"))
    seqname_fastq, seq_fastq, line_fastq = FastqParser("~/data/test.fq")
    seq_txt = Parser("fastaq-seq.txt")
    assert seqname_fastq == seq_txt
