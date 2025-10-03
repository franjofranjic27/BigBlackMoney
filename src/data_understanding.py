import pandas as pd

def load_data(path="../data/Big_Black_Money_Dataset.csv"):
    df = pd.read_csv(path, low_memory=False)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.shape)
    print(df.head())
