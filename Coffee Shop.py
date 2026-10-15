import pandas as pd

# 1. create DataFrame from the wordproblem data
data = {
        "day": ["Monday", "Monday", "Tuesday", "Tuesday", "Wednesday", "Wednesday"],
        "product": ["Latte", "Espresso", "Latte", "Espresso", "Latte", "Espresso"],
        "cups": [45,30,52,28,38,41]
        }
df = pd.DataFrame(data)

#2. create a Boolean mask (True only for the rows we want)
mask = df["product"] == "Latte"   #True where prodcut is Latte

#3. Apply the mask to keep only Latte rows
latte_rows = df[mask]

#4. Calculate the average of the 'cups' column on the filtered rows
average_latte = latte_rows["cups"].mean()

print(average_latte)