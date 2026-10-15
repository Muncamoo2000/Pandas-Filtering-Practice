import pandas as pd

#1 create the database
data = {
        "order_id": ["1001", "1002", "1003", "1004", "1005", "1006"],
        "customer_type": ["New", "Returning", "New", "Returning", "New", "Returning"],
        "amount": [45.50, 120.00, 32.75, 89.20, 67.00, 150.40]
        }
db = pd.DataFrame(data)

#2 Create Boolean mask using query()(True when the customer type is new)


