import json
import time
import logging
import environs

from influxdb import InfluxDBClient
from datetime import datetime, timedelta

from .io import decoder

config = environs.Env()
config.read_env()

LOG_FORMAT = "%(asctime)s | %(name)-18s | %(levelname)-8s | %(message)s"

def export_data():
    client = InfluxDBClient(
        host=str(config("INFLUX_HOST")),
        port=str(config("INFLUX_PORT")),
        username=str(config("INFLUX_USERNAME")),
        password=str(config("INFLUX_PASSWORD"))
        )
    response = client.get_list_database()
    
    if response is not None:
        if any('covid' in item.values() for item in response):
            pass
        else:
            logging.info("Creating new database...")
            client.create_database('covid')
            logging.info("Database created")
    client.switch_database('covid')
    

    regional_data = decoder.regional_data()
    for region in regional_data:
        region_data = [
            {
                "measurement": "covid-19",
                "tags":{
                    "comunidad": region.name
                },
                "time":str(datetime.now()),
                "fields":{
                    "total_confirmed": region.today_confirmed,
                    "total_deaths": region.today_deaths,
                    "total_intesive_care": region.today_intensive_care,
                    "today_new_confirmed": region.today_new_confirmed,
                    "today_new_deaths": region.today_new_deaths,
                    "today_new_UCI": region.today_new_intensive_care,
                    "today_new_open_cases": region.today_new_open_cases,
                    "today_new_recovered": region.today_new_recovered,
                    "today_new_total_hospitalised": region.today_new_total_hospitalised_patients,
                    "total_open_cases": region.today_open_cases,
                    "total_recovered": region.today_recovered,
                    "total_hospitalised": region.today_total_hospitalised_patients,
                    "today_vs_yesterday_confirmed": region.today_vs_yesterday_confirmed,
                    "today_vs_yestarday_deaths": region.today_vs_yesterday_deaths,
                    "today_vs_yesterday_UCI": region.today_vs_yesterday_intensive_care,
                    "today_vs_yestarday_recoverd": region.today_vs_yesterday_recovered
                }
            }]
        if client.write_points(region_data): logging.info(f"INSERT {region.name} SUCCESS")
        else: logging.error(f"INSERT {region.name} ERROR")

    spain_data = decoder.spain_data()
    data = [
        {
            "measurement": "covid-spain",
            "tags":{
                "pais": spain_data.name
            },
            "time":str(datetime.now()),
            "fields":{
                "total_confirmed": spain_data.today_confirmed,
                "total_deaths": spain_data.today_deaths,
                "total_intesive_care": spain_data.today_intensive_care,
                "today_new_confirmed": spain_data.today_new_confirmed,
                "today_new_deaths": spain_data.today_new_deaths,
                "today_new_UCI": spain_data.today_new_intensive_care,
                "today_new_open_cases": spain_data.today_new_open_cases,
                "today_new_recovered": spain_data.today_new_recovered,
                "today_new_total_hospitalised": spain_data.today_new_total_hospitalised_patients,
                "total_open_cases": spain_data.today_open_cases,
                "total_recovered": spain_data.today_recovered,
                "total_hospitalised": spain_data.today_total_hospitalised_patients,
                "today_vs_yesterday_confirmed": spain_data.today_vs_yesterday_confirmed,
                "today_vs_yestarday_deaths": spain_data.today_vs_yesterday_deaths,
                "today_vs_yesterday_UCI": spain_data.today_vs_yesterday_intensive_care,
                "today_vs_yestarday_recoverd": spain_data.today_vs_yesterday_recovered
            }
        }]
    if client.write_points(data): logging.info(f"INSERT {spain_data.name} SUCCESS")
    else: logging.error(f"INSERT {region.name} ERROR")

    andalucia_data = decoder.andalucia_data()
    for region in andalucia_data:
        subregion_data = [
            {
                "measurement": "covid-andalucia",
                "tags":{
                    "provincia": region.name
                },
                "time":str(datetime.now()),
                "fields":{
                    "total_confirmed": region.today_confirmed,
                    "total_deaths": region.today_deaths,
                    "total_intesive_care": region.today_intensive_care,
                    "today_new_confirmed": region.today_new_confirmed,
                    "today_new_deaths": region.today_new_deaths,
                    "today_new_UCI": region.today_new_intensive_care,
                    "today_new_recovered": region.today_new_recovered,
                    "today_new_total_hospitalised": region.today_new_total_hospitalised_patients,
                    "total_recovered": region.today_recovered,
                    "total_hospitalised": region.today_total_hospitalised_patients,
                    "today_vs_yesterday_confirmed": region.today_vs_yesterday_confirmed,
                    "today_vs_yestarday_deaths": region.today_vs_yesterday_deaths,
                    "today_vs_yesterday_UCI": region.today_vs_yesterday_intensive_care,
                    "today_vs_yestarday_recoverd": region.today_vs_yesterday_recovered
                }
            }] 
        if client.write_points(subregion_data): logging.info(f"INSERT {region.name} SUCCESS")
        else: logging.error(f"INSERT {region.name} ERROR")

    last_update = decoder.last_update()
    print(last_update)
    date = [
        {
            "measurement": "last-update",
            "time":str(datetime.now()),
            "fields":{
                "date": last_update
            }
        }
    ]
    if client.write_points(date): logging.info(f"INSERT LAST UPDATE SUCCESS")
    else: logging.error(f"INSERT LAST UPDATE ERROR")


def main():
    logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
    time_slepp = timedelta(hours=2)
    print(time_slepp.seconds)
    while True:
        logging.info("----------- GETTING DATA ---------------")
        export_data()
        time.sleep(time_slepp.seconds)



