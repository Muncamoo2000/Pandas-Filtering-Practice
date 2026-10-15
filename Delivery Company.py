import pandas as pd

#1. Create the database
data = {"date": ["2026-10-01", "2026-10-01", "2026-10-02", "2026-10-02", "2026-10-03", "2026-10-03"],
        "city": ["Chicago", "Detroit", "Chicago", "Detroit", "Chicago", "Detroit"],
        "packages": [120, 85, 140, 92, 110, 78]
       }
df = pd.DataFrame(data)

#2 the highest number of packages delivered to Chicago on a single day
max_packages = df.loc[df["city"] == "Chicago", "packages"].max()
print(max_packages)                      