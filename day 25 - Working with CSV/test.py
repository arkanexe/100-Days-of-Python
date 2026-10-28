import pandas as pd

data = pd.read_csv("api_logs.csv")

reponse_time = data["response_time_ms"].to_list()

mean = sum(reponse_time) / len(reponse_time)
code_500 = data[data["status_code"] == 500]

max = data[data["response_time_ms"] == data["response_time_ms"].max()]

endpoint = data[data["endpoint"]]
print(max)
post_request = data[data["method"] == "POST"]
slow_post_request = post_request[post_request["reponse_time_ms"] > 500]
