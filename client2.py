import httpx

url = "http://127.0.0.1:8000/predict"

data = [
    {
        "trans_date_trans_time": "2019-01-01 00:00:18",
        "cc_num": 2703186189652095,
        "merchant": "fraud_Rippin, Kub and Mann",
        "category": "misc_net",
        "amt": 4.97,
        "first": "Jennifer",
        "last": "Banks",
        "gender": "F",
        "street": "561 Perry Cove",
        "city": "SomeCity",
        "state": "SomeState",
        "zip": 12345,
        "lat": 36.0788,
        "long": -81.1781,
        "city_pop": 3495,
        "job": "Psychologist, counseling",
        "dob": "1988-03-09",
        "trans_num": "0b242abb623afc578575680df30655b9",
        "unix_time": 1325376018,
        "merch_lat": 36.011293,
        "merch_long": -82.048315
    }
]

response = httpx.post(url, json={"item": data})


print(response.json())
