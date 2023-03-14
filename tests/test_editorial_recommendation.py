import pytest
import requests
from config import EBAY_EDITORIAL_URL, EBAY_EDITORIAL_TOKEN
from includes import notify

test_name = 'Test: Editorial recommendation api'
ebay_url = EBAY_EDITORIAL_URL
ebay_pr = {'token': EBAY_EDITORIAL_TOKEN}


# If test failed - send message, fail test
def failed(message):
    message = notify.generate_message(test_name, message)
    notify.notify_ending(message)
    pytest.fail(message)


# Step1: Check response status == 200
def test_get_ebay_editorial_recommendation_status_code_equals_200():
    response = requests.get(ebay_url, params=ebay_pr)
    if response.status_code != 200:
        failed("Step1 -> Check response status: " + ebay_url + " - status code != 200")


# Step2: Check response type == "application/json"
def test_get_ebay_editorial_recommendation_check_content_type_equals_json():
    response = requests.get(ebay_url, params=ebay_pr)
    if response.headers["Content-Type"] != "application/json":
        failed("Step2 -> Check response type: " + ebay_url + "- Content-Type != application/json")


# Step3: Check response param "success" == 1
def test_get_ebay_editorial_recommendation_check_success_is_returned():
    response = requests.get(ebay_url, params=ebay_pr)
    response_body = response.json()
    if response_body["success"] != 1:
        failed("Step3 -> Check response param: " + ebay_url + " - Success param != 1")
