# import requests
# import os
# import pytest

from app import addNumbers
from math import multiplyNumbers

BASE_Address = "http://localhost:5000/"

def test_add():
    assert (addNumbers(2, 3)== 5)
    assert (addNumbers(-2, 5)== 3)
    assert (addNumbers(0, 0)== 0)
    # response = requests.get("%sadd/2/3" % BASE_Address)
    # assert response.text == "5"

def test_multiply():
    assert (multiplyNumbers(2, 3)== 6)
    # response = requests.get("%smultiply/2/3" % BASE_Address)
    # assert response.text == "6"
