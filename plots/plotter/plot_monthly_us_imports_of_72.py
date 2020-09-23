import pandas as pd
import matplotlib.pyplot as plt
import datetime


months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
years = [str(i) for i in range(2000, 2021)]

period_keys = []
world_import_value_usds = []

for year in years:
    for month in months:
        period = int(year + month)
        date = datetime.date(year=int(year), month=int(month[0].replace("0", "") + month[1]), day=1)

        csv = f"/Users/suyeol/suppchain/data/us_steel_imports_monthly/period{period}_agg2_tfImports_reporterUS_commcode72.csv"
        try:
            df = pd.read_csv(csv)
            world_row_idx = df.index[df["12"] == "World"].tolist()
            world_import_value_usd = df.iloc[world_row_idx]["20"].to_numpy()[0]
            world_import_value_usds.append(world_import_value_usd)
            period_keys.append(date)
            pass
        except pd.errors.EmptyDataError:
            world_import_value_usds.append(0)
            period_keys.append(date)
            pass

# plotting
plt.figure(1, figsize=(10, 6))
plt.plot(
    period_keys[120:245], world_import_value_usds[120:245]
)  # , label="US Steel Imports Total (HS 72)")

plt.xlabel("Period")
plt.ylabel("Total Value Imported USD")
plt.title("US Steel Imports Total (HS 72)")

# plt.legend(loc="upper left")
plt.show()

if __name__ == "__main__":
    pass
