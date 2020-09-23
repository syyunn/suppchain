import pandas as pd
import matplotlib.pyplot as plt
import datetime
import statistics

data = "../../data/us_imports_from_world_chapter_level.csv"
hs_desc = "../../data/h5_desc.csv"
df = pd.read_csv(data)
hs_desc = pd.read_csv(hs_desc)
hs_desc = dict(zip(hs_desc['id'], hs_desc['commodity']))

years = [i for i in range(2010, 2021)]
months = [i for i in range(1, 13)]

period_keys = []
for year in years:
    for month in months:
        period_keys.append(datetime.date(year=year, month=month, day=15))

period_keys = period_keys[:-7]

# plotting
plt.figure(1, figsize=(12, 6))

for i in range(1, 98):
    df_chapter = df.loc[df["commodity_code"] == i].sort_values("period", ascending=True)
    volumes = df_chapter["trade_value_usd"].to_list()
    if len(volumes) > 0:
        if statistics.median(volumes) >= 8000000000 or i == 72 or i == 73:
            try:
                plt.plot(period_keys, volumes, label=f"Ch{i}: " + hs_desc[i])
            except (ValueError, KeyError):
                print(i)
        else:
            pass
        pass

plt.xlabel("Period")
plt.ylabel("Total Value Imported USD")
# plt.title("US Steel & Iron Imports Total (HS 72)")

plt.legend(loc="upper left")
plt.show()

if __name__ == "__main__":
    pass
