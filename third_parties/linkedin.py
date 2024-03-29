import json
import os
import requests


def clean_json_data(json_data):
    json_data = {
        k: v
        for k, v in json_data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if json_data.get("groups"):
        for group_dict in json_data.get("groups"):
            group_dict.pop("profile_pic_url")

    return json_data


def scrape_linkedin_profile():
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    api_endpoint = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"

    response = requests.get(api_endpoint)

    return clean_json_data(response.json())
