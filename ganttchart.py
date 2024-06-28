import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define the tasks with their specific start and end dates
tasks = [
    {"Task": "Collect Background Information", "Start Date": "2023-09-23", "End Date": "2023-10-13"},
    #{"Task": "Start Writing Report", "Start Date": "2023-10-14", "End Date": "2023-10-23"},
    {"Task": "Decide on Model (LSTM, SVM)", "Start Date": "2023-10-14", "End Date": "2023-11-14"},
    {"Task": "Related Work & Literature Review", "Start Date": "2023-10-14", "End Date": "2023-11-30"},
    {"Task": "Interim Report", "Start Date": "2023-11-14", "End Date": "2024-02-20"},
    {"Task": "Examine Datasets (EGX)", "Start Date": "2023-11-30", "End Date": "2023-12-30"},
    {"Task": "Pre-process Dataset", "Start Date": "2023-12-31", "End Date": "2024-02-25"},
    {"Task": "Apply Data to LSTM, SVM", "Start Date": "2024-02-26", "End Date": "2024-03-01"},
    {"Task": "Calculate Accuracy Metrics", "Start Date": "2024-02-01", "End Date": "2024-02-06"},
    {"Task": "Document Implementation", "Start Date": "2023-11-30", "End Date": "2024-06-10"},
    {"Task": "Model Tuning", "Start Date": "2024-02-26", "End Date": "2024-06-10"},
    {"Task": "Document Tuning Results", "Start Date": "2024-02-26", "End Date": "2024-06-10"},
    {"Task": "Finalize Research Writing", "Start Date": "2024-02-23", "End Date": "2024-06-15"},
    #{"Task": "Write Executive Summary", "Start Date": "2024-04-29", "End Date": "2024-05-08"}
]

# Convert start and end dates to datetime
for task in tasks:
    task["Start Date"] = datetime.strptime(task["Start Date"], "%Y-%m-%d")
    task["End Date"] = datetime.strptime(task["End Date"], "%Y-%m-%d")

# Convert tasks to DataFrame
df = pd.DataFrame(tasks)

# Create Gantt chart
fig, ax = plt.subplots(figsize=(14, 8))

for idx, task in df.iterrows():
    ax.barh(task["Task"], (task["End Date"] - task["Start Date"]).days, left=task["Start Date"], align='center', edgecolor='black')

# Formatting the chart
ax.set_xlabel('Date')
ax.set_ylabel('Tasks')
ax.set_title('Gantt Chart')
ax.grid(True)
ax.xaxis_date()

# Set date format on x-axis
date_format = mdates.DateFormatter('%b %d, %Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
