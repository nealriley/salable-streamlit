# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import requests


SALABLE_URL = 'https://api.salable.app/licenses/check'
CREATE_LICENSE_ENDPOINT = 'https://api.salable.app/licenses'
SALABLE_API_KEY = "test_38d98b4e2ea3c642ad7db33884c1a5831a8491da"
SALABLE_PRODUCT_ID = "15362adf-d088-4ded-86b0-4190e5fb404b"
BASIC_PLAN_ID = "0057ba16-8200-43a7-a33c-68942431e0d9"
FANCY_PLAN_ID = "55a88a41-fe2d-49d3-920b-0a996617e112"


def check_grantee_id(grantee_id):
    headers = {
        "x-api-key" : SALABLE_API_KEY
    }
    url=f'{SALABLE_URL}?productUuid={SALABLE_PRODUCT_ID}&granteeIds=[{grantee_id}]'
    response = requests.get(url=f'{SALABLE_URL}?productUuid={SALABLE_PRODUCT_ID}&granteeIds=[{grantee_id}]', headers=headers)
    if response.status_code == 200:
        return({
            'status': response.status_code,
            'data': response.json(),
            'licensed' : True
        })
    else:      
        return {
            'status': response.status_code,
            'data': {},
            'licensed' : False
        }

def create_license(grantee_id, plan_id):
    headers = {
        'x-api-key': SALABLE_API_KEY
    }
    body={
        "planUuid": plan_id,
        "member": grantee_id,
        "granteeId": grantee_id
    }
    response = requests.post(url=f'{CREATE_LICENSE_ENDPOINT}', headers=headers, json=body)
    if response.status_code == 200:
        return({
            'status': response.status_code,
            'data': response.json(),
            'licensed' : True
        })
    else:      
        return {
            'status': response.status_code,
            'data': {},
            'licensed' : False
        }