Pandas Filtering Practice
Simple beginner exercises practicing the most common Pandas pattern:
Boolean Filtering + Aggregation
(Select rows that meet a condition → then calculate mean / sum / max / count)
---
The Pattern
```python
# Classic style
mask = df["column"] == "value"
result = df[mask]["other_column"].mean()   # or .sum() / .max() / .count()

# Modern one-liner
result = df.loc[df["column"] == "value", "other_column"].mean()

# Using query()
result = df.query("column == 'value'")["other_column"].mean()
```
---
Problems
Problem 1 – Coffee Shop
Question: What is the average number of Latte cups sold per day?
day	product	cups
Monday	Latte	45
Monday	Espresso	30
Tuesday	Latte	52
Tuesday	Espresso	28
Wednesday	Latte	38
Wednesday	Espresso	41
Answer: 45.0
---
Problem 2 – Bookstore
Question: What is the total number of Science books sold?
day	category	books_sold
Mon	Fiction	12
Mon	Science	8
Tue	Fiction	15
Tue	Science	6
Wed	Fiction	9
Wed	Science	11
Answer: 25
---
Problem 3 – Delivery Company
Question: What is the highest number of packages delivered to Chicago on any single day?
date	city	packages
2026-10-01	Chicago	120
2026-10-01	Detroit	85
2026-10-02	Chicago	140
2026-10-02	Detroit	92
2026-10-03	Chicago	110
2026-10-03	Detroit	78
Answer: 140
---
Problem 4 – Online Store
Question: How many orders were placed by New customers?
order_id	customer_type	amount
1001	New	45.50
1002	Returning	120.00
1003	New	32.75
1004	Returning	89.20
1005	New	67.00
1006	Returning	150.40
Answer: 3
---
How to Use
Create a Python file for each problem (or put them all in one file).
Copy the data into a DataFrame.
Apply the filtering + aggregation pattern.
Print the result and check against the answers above.
Happy practicing!
