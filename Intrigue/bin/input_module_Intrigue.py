
# encoding = utf-8

import os
import sys
import time
import json
import datetime


class Header:

    def __init__(self, access_key, secret_key):

        self.Authorization = {
            "INTRIGUE_ACCESS_KEY": access_key,
            "INTRIGUE_SECRET_KEY": secret_key
        }


class UrlBuilder:
    def build(self):
        return "https://app.intrigue.io/api/collections/{}/export/{}/from_date/{}/".format(self.collection, self.issueType, self.startDate)

    def __init__(self, collection, issueType, startDate):

        self.collection = collection
        self.issueType = issueType
        self.startDate = startDate


def buildJsonResult(helper, jsonResult):
    items = []

    for item in jsonResult['result']['items']:
        state = helper.get_check_point(item["id"])
        if state is None:
            items.append(item)
            helper.save_check_point(item["id"], "Indexed")
        # else: #this would be used to delete an existing entry and add a new one. Possibly to update a value.
        #     helper.delete_check_point(item["id"])
        #     items.append(item)
        #     helper.save_check_point(item["id"], "Indexed")
        # UNCOMMENT THIS LINE WHILE TESTING
        # helper.delete_check_point(item["id"])
    return items


'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''
'''
# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''


def validate_input(helper, definition):
    # This example accesses the modular input variable
    # collection_name = definition.parameters.get('collection_name', None)
    # item_type = definition.parameters.get('item_type', None)
    # date = definition.parameters.get('date', None)
    pass


def collect_events(helper, ew):
    loglevel = helper.get_log_level()
    # (log_level can be "debug", "info", "warning", "error" or "critical", case insensitive)
    helper.set_log_level(loglevel)
    opt_collection_name = helper.get_arg('collection_name')
    opt_item_type = helper.get_arg('item_type')
    opt_date = helper.get_arg('start_date')
    opt_access_key = helper.get_arg("access_key")
    opt_secret_key = helper.get_arg("secret_key")
    helper.log_debug("collected data from fields")
    # get input type
    try:
        header = Header(opt_access_key, opt_secret_key)
        url = UrlBuilder(opt_collection_name, opt_item_type, opt_date)
    except:
        helper.log_debug("Error occurred when creating the request.")
        raise Exception("Error occurred when creating the request.")

    helper.log_debug("built url and headers")
    response = helper.send_http_request(url.build(),
                                        'GET',
                                        parameters=None,
                                        payload=None,
                                        headers=header.Authorization,
                                        cookies=None,
                                        verify=True,
                                        cert=None,
                                        timeout=None,
                                        use_proxy=True)
    helper.log_debug("got response back from API")
    r_status = response.status_code
    helper.log_debug("got status code back from API {}".format(r_status))
    if r_status != 200:
        response.raise_for_status()
        raise Exception("Error occurred when retrieving data.")
    # get response body as json. If the body text is not a json string, raise a ValueError
    r_json = response.json()
    helper.log_debug("started building json")
    items = buildJsonResult(helper, r_json)
    helper.log_debug("finished building json")
    # To create a splunk event
    event = helper.new_event(json.dumps(items), time=None, host=None,
                             index=None, source=None, sourcetype=None, done=True, unbroken=True)
    helper.log_debug("created new event")
    ew.write_event(event)
    helper.log_debug("finished writing event")
