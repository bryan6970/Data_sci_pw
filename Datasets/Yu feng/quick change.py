import pandas as pd

def remove_tcl_col():
    df = pd.read_csv("Cleaned singapore electricity usage and demand.csv")
    df.loc[df["SOLAR(MW)"] == "-", "SOLAR(MW)"] = 0

    # df.drop("False", axis=1, inplace=True)

    print(df)

    df.to_csv("Cleaned singapore electricity usage and demand.csv", index=False)


remove_tcl_col()