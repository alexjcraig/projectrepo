""" this will test the ris capabiility"""
from ajcpkg import Works


REF_RIS = """TY  - JOUR
AU  - John R. Kitchin
PY  - 2015
TI  - Examples of Effective Data Sharing in Scientific Publishing
JO  - ACS Catalysis
VL  - 5
IS  - 6
SP  - 3894
EP  - 3899
DO  - https://doi.org/10.1021/acscatal.5b00538"""


def test_ris():
    """here is the test method for RIS"""
    w = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_RIS == w.ris
