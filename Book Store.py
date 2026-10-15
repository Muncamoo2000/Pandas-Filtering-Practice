import pandas as pd

#1. Create dataframe from the word problem
data = {
        "days": ["Mon", "Mon", "Tue", "Tue", "Wed", "Wed"],
        "category": ["Fiction", "Science", "Fiction", "Science", "Fiction", "Science"],
        "books_sold": [12, 8, 15, 6, 9, 11]
        }
df = pd.DataFrame(data)

#2 Create a Bool mask (True only for the rows we want)
sum_category = df.loc[df["category"] == "Science", "books_sold"].sum()
print(sum_category)

#3 Using query()
sum_category = df.query("category == 'Science'")["books_sold"].sum()
print(sum_category)