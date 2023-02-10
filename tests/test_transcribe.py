# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    assert transcribe("AGGCTAGTACTGC", reverse=False) == "AGGCUAGUACUGC", "Transcribe function does not function properly"

    try:
        empty_str = transcribe("", reverse=False)
        test_empty_str = False
    except ValueError:
        test_empty_str = True

    try:
        bad_str = transcribe("UCSF", reverse=False)
        test_bad_str = False
    except ValueError:
        test_bad_str = True

    try:
        no_str = transcribe(0, reverse=False)
        test_no_str = False
    except ValueError:
        test_no_str = True

    assert test_empty_str == True, "Input to transcribe cannot be an empty string"
    assert test_bad_str == True, "Input to transcribe must contain AGCT"
    assert test_no_str == True, "Input to transcribe must be a string"


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    assert reverse_transcribe("AGGCTAGTACTGC") == "UCCGAUCAUGACG", "Reverse transcribe function does not function properly"
    
    try:
        empty_str = reverse_transcribe("")
        test_empty_str = False
    except ValueError:
        test_empty_str = True

    try:
        bad_str = reverse_transcribe("UCSF")
        test_bad_str = False
    except ValueError:
        test_bad_str = True

    try:
        no_str = reverse_transcribe(0)
        test_no_str = False
    except ValueError:
        test_no_str = True

    assert test_empty_str == True, "Input to reverse_transcribe cannot be an empty string"
    assert test_bad_str == True, "Input to reverse_transcribe must contain AGCT"
    assert test_no_str == True, "Input to reverse_transcribe must be a string"

