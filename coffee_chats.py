import pandas as pd
import numpy as np
import openpyxl
import re
import csv
import collections

slots = ["Monday 9-10AM", "Monday 9-10 AM", "Monday 10-11AM", "Monday 11AM-12PM", "Monday 12PM-1PM", "Monday 1PM-2PM", "Monday 2PM-3PM", "Monday 3PM-4PM", "Monday 4PM-5PM", "Monday 5PM-6PM", "Monday 6PM-7PM", "Monday 7PM-8PM", "Monday 8PM-9PM", "Monday 9PM-10PM", "Tuesday 9-10AM", "Tuesday 10-11AM", "Tuesday 11AM-12PM", "Tuesday 12PM-1PM", "Tuesday 1PM-2PM", "Tuesday 2PM-3PM", "Tuesday 3PM-4PM", "Tuesday 4PM-5PM", "Tuesday 5PM-6PM", "Tuesday 6PM-7PM", "Tuesday 7PM-8PM", "Tuesday 8PM-9PM", "Tuesday 9PM-10PM", "Wednesday 9-10AM", "Wednesday 10-11AM", "Wednesday 11AM-12PM", "Wednesday 12PM-1PM", "Wednesday 1PM-2PM", "Wednesday 2PM-3PM", "Wednesday 3PM-4PM", "Wednesday 4PM-5PM", "Wednesday 5PM-6PM", "Wednesday 6PM-7PM", "Wednesday 7PM-8PM", "Wednesday 8PM-9PM", "Wednesday 9PM-10PM",
"Thursday 9-10AM", "Thursday 10-11AM", "Thursday 11AM-12PM", "Thursday 12PM-1PM", "Thursday 1PM-2PM", "Thursday 2PM-3PM", "Thursday 3PM-4PM", "Thursday 4PM-5PM", "Thursday 5PM-6PM", "Thursday 6PM-7PM", "Thursday 7PM-8PM", "Thursday 8PM-9PM", "Thursday 9PM-10PM",
"Friday 9-10AM", "Friday 10-11AM", "Friday 11AM-12PM", "Friday 12PM-1PM", "Friday 1PM-2PM", "Friday 2PM-3PM", "Friday 3PM-4PM", "Friday 4PM-5PM", "Friday 5PM-6PM", "Friday 6PM-7PM", "Friday 7PM-8PM", "Friday 8PM-9PM", "Friday 9PM-10PM",
"Saturday 9-10AM", "Saturday 10-11AM", "Saturday 11AM-12PM", "Saturday 12PM-1PM", "Saturday 1PM-2PM", "Saturday 2PM-3PM", "Saturday 3PM-4PM", "Saturday 4PM-5PM", "Saturday 5PM-6PM", "Saturday 6PM-7PM", "Saturday 7PM-8PM", "Saturday 8PM-9PM", "Saturday 9PM-10PM", "Sunday 9-10AM", "Sunday 10-11AM", "Sunday 11AM-12PM", "Sunday 1PM-2PM", "Sunday 2PM-3PM", "Sunday 3PM-4PM", "Sunday 4PM-5PM", "Sunday 5PM-6PM", "Sunday 6PM-7PM", "Sunday 7-8PM", "Sunday 8-9PM", "Sunday 9-10PM",
"Week 4 Monday 9-10AM", "Week 4 Monday 10-11AM", "Week 4 Monday 11AM-12PM", "Week 4 Monday 12PM-1PM", "Week 4 Monday 1PM-2PM", "Week 4 Monday 2PM-3PM", "Week 4 Monday 3PM-4PM", "Week 4 Monday 4PM-5PM", "Week 4 Monday 5PM-6PM", "Week 4 Monday 6PM-7PM", "Week 4 Monday 7PM-8PM", "Week 4 Monday 8PM-9PM", "Week 4 Monday 9PM-10PM", "Week 4 Tuesday 9-10AM", "Week 4 Tuesday 10-11AM", "Week 4 Tuesday 11-12PM", "Week 4 Tuesday 12PM-1PM", "Week 4 Tuesday 1PM-2PM", "Week 4 Tuesday 2PM-3PM", "Week 4 Tuesday 3PM-4PM", "Week 4 Tuesday 4PM-5PM", "Week 4 Tuesday 5PM-6PM", "Week 4 Tuesday 6PM-7PM", "Week 4 Tuesday 7PM-8PM", "Week 4 Tuesday 8PM-9PM", "Week 4 Tuesday 9PM-10PM", "Week 4 Wednesday 9-10AM", "Week 4 Wednesday 10-11AM", "Week 4 Wednesday 11-12PM", "Week 4 Wednesday 12PM-1PM", "Week 4 Wednesday 1PM-2PM", "Week 4 Wednesday 2PM-3PM", "Week 4 Wednesday 3PM-4PM", "Week 4 Wednesday 4PM-5PM", "Week 4 Wednesday 5PM-6PM", "Week 4 Wednesday 6PM-7PM", "Week 4 Wednesday 7PM-8PM", "Week 4 Wednesday 8PM-9PM", "Week 4 Wednesday 9PM-10PM",
"Week 4 Thursday 9-10AM", "Week 4 Thursday 10-11AM", "Week 4 Thursday 11AM-12PM", "Week 4 Thursday 12PM-1PM", "Week 4 Thursday 1PM-2PM", "Thursday 2PM-3PM", "Week 4 Thursday 3PM-4PM", "Thursday 4PM-5PM", "Week 4 Thursday 5PM-6PM", "Week 4 Thursday 6PM-7PM", "Week 4 Thursday 7PM-8PM", "Week 4 Thursday 8PM-9PM", "Week 4 Thursday 9PM-10PM",
"Week 4 Friday 9-10AM", "Week 4 Friday 10-11AM", "Week 4 Friday 11AM-12PM", "Week 4 Friday 12PM-1PM", "Week 4 Friday 1PM-2PM", "Friday 2PM-3PM", "Week 4 Friday 3PM-4PM", "Week 4 Friday 4PM-5PM", "Week 4 Friday 5PM-6PM", "Friday 6PM-7PM", "Week 4 Friday 7PM-8PM", "Week 4 Friday 8PM-9PM", "Week 4 Friday 9PM-10PM",
"Week 4 Saturday 9-10AM", "Week 4 Saturday 10-11AM", "Week 4 Saturday 11AM-12PM", "Week 4 Saturday 12PM-1PM", "Week 4 Saturday 1PM-2PM", "Week 4 Saturday 2PM-3PM", "Week 4 Saturday 3PM-4PM", "Week 4 Saturday 4PM-5PM", "Week 4 Saturday 5PM-6PM", "Week 4 Saturday 6PM-7PM", "Week 4 Saturday 7PM-8PM", "Week 4 Saturday 8PM-9PM", "Week 4 Saturday 9PM-10PM", "Week 4 Sunday 9-10AM", "Week 4 Sunday 10-11AM", "Week 4 Sunday 11AM-12PM", "Week 4 Sunday 12PM-1PM", "Week 4 Sunday 1PM-2PM", "Week 4 Sunday 2PM-3PM", "Week 4 Sunday 3PM-4PM", "Week 4 Sunday 4PM-5PM", "Week 4 Sunday 5PM-6PM", "Week 4 Sunday 6PM-7PM", "Week 4 Sunday 7PM-8PM", "Week 4 Sunday 8PM-9PM", "Week 4 Sunday 9PM-10PM"]
matches = list()
with open("Week34final.csv", 'w', newline='', encoding = "utf-8") as schedule:
	for slot in slots:
		with open("Week34content.csv", 'r', encoding = "utf-8") as mems:
			reader = csv.reader(mems, delimiter=",")
			writer = csv.writer(schedule, delimiter =',')
			for row in reader:
				if slot in row:
					print(slot, row[0:2])
					matches.append(slot)
					matches.append(row[0:2])
					writer.writerow(matches)
					matches.clear()
print(len(slots))