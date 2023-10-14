import sys
import pytest

sys.path.append("..")
from test import test_project1 as base_test
    
@pytest.mark.parametrize("bucket", [("20"), ("40"), ("60"), ("80"), ("100")])
def test_project(bucket):
    base_test(bucket)

