import json
import requests

class APIError(Exception):
    def __init__(self, context_detail: str, status_code: int, server_response: str):
        self.context_detail = context_detail
        self.status_code = status_code
        self.server_response = server_response
        super(APIError, self).__init__(
            f"{context_detail}. Server response: ({status_code}) {server_response}"
        )


class NetworkError(Exception):
    pass

def get_regional_data(host:str, from_date:str, to_date:str) -> dict:
    try:
        response = requests.get(
            f"{host}/api/country/spain/region/all",
            headers={
                "Content-Type": "application/json"
            },
            params={
                "date_from": from_date,
                "date_to": to_date
            }
        )
    except requests.exceptions.HTTPError as e:
        raise NetworkError(str(e))
    else:
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(
            f"Cannot get item from Coronvirus API",
            response.status_code,
            response.text
        )

def get_data_by_region(host:str, region_code:str, from_date:str, to_date:str) -> dict:
    try:
        response = requests.get(
            f"{host}/api/country/spain/region/{region_code}",
            headers={
                "Content-Type": "applictaion/json"
            },
            params={
                "date_from": from_date,
                "date_to": to_date
            }
        )
    except requests.exceptions.HTTPError as e:
        raise NetworkError(str(e))
    else:
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(
            f"Cannot get item from Coronvirus API",
            response.status_code,
            response.text
        )

def get_last_update(host:str, from_date:str, to_date:str) -> str:
    try:
        response = requests.get(
            f"{host}/api/country/spain",
            headers={
                "Content-Type": "application/json"
            },
            params={
                "date_from": from_date,
                "date_to": to_date
            }
        )
    except requests.exceptions.HTTPError as e:
        raise NetworkError(str(e))
    else:
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(
            f"Cannot get item from Coronvirus API",
            response.status_code,
            response.text
        )