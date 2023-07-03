import pandas as pd

def remove_tcl_col():
    df = pd.read_csv("Cleaned singapore electricity usage and demand.csv")
    print(df)
    df.drop(labels="TCL(MW)", axis=1, inplace=True)

    df.to_csv("Cleaned singapore electricity usage and demand.csv", index=False)


remove_tcl_col()