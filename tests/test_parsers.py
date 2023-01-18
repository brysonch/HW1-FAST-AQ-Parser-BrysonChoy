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

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """

    self.assertRaises(ValueError, FastaParser("bad.fa"))
    self.assertRaises(ValueError, FastaParser("empty.fa"))
    seq_fasta, line_fasta = FastaParser("~/data/test.fa")
    seq_txt = Parser("fasta-check.txt")
    assert seq_fasta == seq_txt



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
