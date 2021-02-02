import requests
import environs
import logging
from typing import NamedTuple, List

from datetime import datetime
from . import rest

config = environs.Env()
config.read_env()

date = str(datetime.now().date())

class Region(NamedTuple):
    name: str
    today_confirmed: int
    today_deaths: int
    today_intensive_care: int
    today_new_confirmed: int
    today_new_deaths: int
    today_new_intensive_care: int
    today_new_open_cases: int
    today_new_recovered: int
    today_new_total_hospitalised_patients: int
    today_open_cases: int
    today_recovered: int
    today_total_hospitalised_patients: int
    today_vs_yesterday_confirmed: int
    today_vs_yesterday_deaths: int 
    today_vs_yesterday_intensive_care: int
    today_vs_yesterday_open_cases: int
    today_vs_yesterday_recovered: int

class SubRegion(NamedTuple):
    name: str
    today_confirmed: int
    today_deaths: int
    today_intensive_care: int
    today_new_confirmed: int
    today_new_deaths: int
    today_new_intensive_care: int
    today_new_recovered: int
    today_new_total_hospitalised_patients: int
    today_recovered: int
    today_total_hospitalised_patients: int
    today_vs_yesterday_confirmed: int
    today_vs_yesterday_deaths: int 
    today_vs_yesterday_intensive_care: int
    today_vs_yesterday_recovered: int


def regional_data() -> List[SubRegion]:
    try:
        data = rest.get_regional_data(config("API_HOST"), date, date)
    except (rest.APIError, rest.NetworkError) as e:
        logging.error(f"Error retriving data from API {str(e)}")

    try:
        regions = data["dates"][date]["countries"]["Spain"]["regions"]
        list_regions = []
        for region in regions:
            comunity = Region(
                name=region["name"],
                today_confirmed=region["today_confirmed"],
                today_deaths=region["today_deaths"],
                today_intensive_care=region["today_intensive_care"],
                today_new_confirmed=region["today_new_confirmed"],
                today_new_deaths=region["today_new_deaths"],
                today_new_intensive_care=region["today_new_intensive_care"],
                today_new_open_cases=region["today_new_open_cases"],
                today_new_recovered=region["today_new_recovered"],
                today_new_total_hospitalised_patients=region["today_new_total_hospitalised_patients"],
                today_open_cases=region["today_open_cases"],
                today_recovered=region["today_recovered"],
                today_total_hospitalised_patients=region["today_total_hospitalised_patients"],
                today_vs_yesterday_confirmed=region["today_vs_yesterday_confirmed"],
                today_vs_yesterday_deaths=region["today_vs_yesterday_deaths"],
                today_vs_yesterday_intensive_care=region["today_vs_yesterday_intensive_care"],
                today_vs_yesterday_open_cases=region["today_vs_yesterday_open_cases"],
                today_vs_yesterday_recovered=region["today_vs_yesterday_recovered"]
            )
            list_regions.append(comunity)
    except KeyError as e:
        logging.error(f"Not found expected key: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error ocurred {str(e)}")
    else:
        return list_regions

def spain_data() -> Region:
    try:
        data = rest.get_regional_data(config("API_HOST"), date, date)
    except (rest.APIError, rest.NetworkError) as e:
        logging.error(f"Error retriving data from API {str(e)}")

    try:
        region = data["dates"][date]["countries"]["Spain"]
        spain = Region(
            name=region["name"],
            today_confirmed=region["today_confirmed"],
            today_deaths=region["today_deaths"],
            today_intensive_care=region["today_intensive_care"],
            today_new_confirmed=region["today_new_confirmed"],
            today_new_deaths=region["today_new_deaths"],
            today_new_intensive_care=region["today_new_intensive_care"],
            today_new_open_cases=region["today_new_open_cases"],
            today_new_recovered=region["today_new_recovered"],
            today_new_total_hospitalised_patients=region["today_new_total_hospitalised_patients"],
            today_open_cases=region["today_open_cases"],
            today_recovered=region["today_recovered"],
            today_total_hospitalised_patients=region["today_total_hospitalised_patients"],
            today_vs_yesterday_confirmed=region["today_vs_yesterday_confirmed"],
            today_vs_yesterday_deaths=region["today_vs_yesterday_deaths"],
            today_vs_yesterday_intensive_care=region["today_vs_yesterday_intensive_care"],
            today_vs_yesterday_open_cases=region["today_vs_yesterday_open_cases"],
            today_vs_yesterday_recovered=region["today_vs_yesterday_recovered"]
        )
    except KeyError as e:
        logging.error(f"Not found expected key: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error ocurred {str(e)}")
    else:
        return spain

def andalucia_data() -> List[Region]:
    try:
        data = rest.get_data_by_region(config("API_HOST"), "andalucia", date, date)
    except (rest.APIError, rest.NetworkError) as e:
        logging.error(f"Error retriving data from API {str(e)}")

    try:
        regions = data["dates"][date]["countries"]["Spain"]["regions"][0]["sub_regions"]
        list_regions = []
        for region in regions:
            comunity = SubRegion(
                name=region["name"],
                today_confirmed=region["today_confirmed"],
                today_deaths=region["today_deaths"],
                today_intensive_care=region["today_intensive_care"],
                today_new_confirmed=region["today_new_confirmed"],
                today_new_deaths=region["today_new_deaths"],
                today_new_intensive_care=region["today_new_intensive_care"],
                today_new_recovered=region["today_new_recovered"],
                today_new_total_hospitalised_patients=region["today_new_total_hospitalised_patients"],
                today_recovered=region["today_recovered"],
                today_total_hospitalised_patients=region["today_total_hospitalised_patients"],
                today_vs_yesterday_confirmed=region["today_vs_yesterday_confirmed"],
                today_vs_yesterday_deaths=region["today_vs_yesterday_deaths"],
                today_vs_yesterday_intensive_care=region["today_vs_yesterday_intensive_care"],
                today_vs_yesterday_recovered=region["today_vs_yesterday_recovered"]
            )
            list_regions.append(comunity)
    except KeyError as e:
        logging.error(f"Not found expected key: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error ocurred {str(e)}")
    else:
        return list_regions   

def last_update() -> str:
    try:
        data = rest.get_last_update(config("API_HOST"), date, date)
    except (rest.APIError, rest.NetworkError) as e:
        logging.error(f"Error retriving data from API {str(e)}")
    
    day = data["dates"][date]["countries"]["Spain"]["date"]

    return day

