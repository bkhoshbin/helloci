import requests
import os
import pytest

BASE_Address = "http://localhost:5000/"

def test_add():
    response = requests.get("%sadd/2/3" % BASE_Address)
    assert response.text == "5"

def test_multiply():
    response = requests.get("%smultiply/2/3" % BASE_Address)
    assert response.text == "6"
