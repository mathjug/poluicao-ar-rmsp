from requests import request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants_test import (
    BASE_URL,
    HEADERS,
)


POSSIBILITIES = [
    {
        "interval": "yearly",
        "indicators": ["MP2.5", "O3", "MP10"]
    },

    {
        "interval": "monthly",
        "month": 8,
        "indicators": ["MP2.5", "O3", "MP10"]
    },

    {
        "interval": "monthly",
        "indicators": ["MP2.5", "O3", "MP10"]
    },

    {
        "interval": "daily",
        "year": 2008,
        "month": 12,
        "indicators": ["MP2.5", "O3", "MP10"]
    },

    {
        "interval": "hourly",
        "month": 1,
        "indicators": ["MP2.5", "O3", "MP10"]
    }
]


class TestLineGraph:
    def test_line_graph(self):
        endpoint = f"/linegraph"
        method = "GET"

        for possibility in POSSIBILITIES:
            payload = possibility

            url = f"{BASE_URL}{endpoint}"
            response = request(
                method.upper(),
                url,
                headers=HEADERS,
                json=payload
            )

            # Change to meaningful asserts here
            print(payload)
            print(response)