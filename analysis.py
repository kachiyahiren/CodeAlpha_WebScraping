import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/books.csv")

# Remove unwanted symbols
df["Price"] = df["Price"].str.replace("Â", "", regex=False)
df["Price"] = df["Price"].str.replace("£", "", regex=False)

# Convert to float
df["Price"] = df["Price"].astype(float)

print("\nDataset Shape")
print(df.shape)

print("\nAverage Price")
print(df["Price"].mean())

print("\nMaximum Price")
print(df["Price"].max())

print("\nMinimum Price")
print(df["Price"].min())

print("\nRating Counts")
print(df["Rating"].value_counts())

print("\nMost Expensive Book")

print(
    df.loc[
        df["Price"].idxmax()
    ]
)
df["Rating"].value_counts().plot(
    kind="bar"
)

plt.title("Book Ratings Distribution")

plt.xlabel("Rating")

plt.ylabel("Number of Books")

plt.savefig("Rating_Distribution.png")

plt.show()

plt.figure()

df["Price"].hist(
    bins=20
)

plt.title("Price Distribution")

plt.xlabel("Price")

plt.ylabel("Frequency")

plt.savefig(
    "Price_Distribution.png"
)

plt.show()