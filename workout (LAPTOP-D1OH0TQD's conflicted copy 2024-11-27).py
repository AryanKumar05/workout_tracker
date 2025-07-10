import requests
from datetime import datetime
exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint="https://api.sheety.co/d70dfebe12bbd2afa7b95998ad3015d1/workout/workouts"

text=input("Tell me the excercise you did?:")
APP_ID="c6cc134d"
API_KEY="af84b3903a57cf04942e5550a9f98b38"
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
exercise_params={
    "query":text,
    "gender":"Male",
    "weight_kg":70,
    "height_cm":178,
    "age":19,

}
response=requests.post(url=exercise_endpoint,json=exercise_params,headers=headers)
results=response.json()
print(results)

today_date = datetime.now().strftime("%d/%m/%Y")
print(today_date)
now_time = datetime.now().strftime("%X")
for exercises in results["exercises"]:
    sheet_param={
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercises["name"].title(),
            "duration": exercises["duration_min"],
            "calories": exercises["nf_calories"],

        }
    }
    sheet_response = requests.post(sheets_endpoint, json=sheet_param)

    print(sheet_response.text)