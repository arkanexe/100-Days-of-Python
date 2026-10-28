from pathlib import Path

import pandas as pd

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "api_logs.csv"

data = pd.read_csv(file_path)

response_times = data["response_time_ms"].to_list()
mean = sum(response_times) / len(response_times)
code_500 = data[data["status_code"] == 500]
max_row = data.loc[data["response_time_ms"].idxmax()]
endpoint = data["endpoint"].unique()

print("Mean response time:", mean)
print("500 status rows:\n", code_500)
print("Slowest request:\n", max_row)
print("Endpoints:", endpoint)

post_requests = data[data["method"] == "POST"]
slow_post_requests = post_requests[post_requests["response_time_ms"] > 500]
print("Slow POST requests:\n", slow_post_requests)
