import pandas as pd
import matplotlib.pyplot as plt
import datetime


months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
years = [str(i) for i in range(2000, 2021)]
# years = [str(i) for i in range(2010, 2021)]


year_keys = []
world_import_value_usds_annual = []


period_keys = []
world_import_value_usds_monthly = []

df = pd.read_csv("../../data/usitc_ad_orders/orders.csv")


def change_to_datetime(date_string):
    year = None
    month = None
    date = None
    splits = date_string.split("/")
    if len(splits[0]) == 2 and len(splits[2]) == 4:
        year = splits[2]
        month = splits[0]
        day = splits[1]
        date = datetime.date(
            year=int(year),
            month=int(month[0].replace("0", "") + month[1]),
            day=int(day[0].replace("0", "") + day[1]),
        )
        return date
    elif len(splits[0]) == 4:
        year = splits[0]
        month = splits[1]
        day = splits[2]
        date = datetime.date(
            year=int(year),
            month=int(month[0].replace("0", "") + month[1]),
            day=int(day[0].replace("0", "") + day[1]),
        )
        return date
    else:
        assert len("hi") != 2


dates = [change_to_datetime(date) for date in df["order_date"].to_list()]
dates = [date for date in dates if date.year >= 2010]


for year in years:
    # year_key = datetime.date(year=int(year), month=12, day=1)
    # year_csv = f"/Users/suyeol/suppchain/data/us_steel_imports_annual/year{year}_agg2_tfImport_reporterCode842_commodityCode72.csv"
    # try:
    #     df = pd.read_csv(year_csv)
    #     world_row_idx = df.index[df["12"] == "World"].tolist()
    #     world_import_value_usd = df.iloc[world_row_idx]["20"].to_numpy()[0]
    #     world_import_value_usds_annual.append(world_import_value_usd)
    #     year_keys.append(year_key)
    #     pass
    # except pd.errors.EmptyDataError:
    #     world_import_value_usds_annual.append(0)
    #     year_keys.append(year_key)
    #     pass

    for month in months:
        period = int(year + month)
        month_key = datetime.date(
            year=int(year), month=int(month[0].replace("0", "") + month[1]), day=1
        )

        csv = f"/Users/suyeol/suppchain/data/us_steel_imports_monthly/period{period}_agg2_tfImports_reporterUS_commcode72.csv"
        try:
            df = pd.read_csv(csv)
            world_row_idx = df.index[df["12"] == "World"].tolist()
            world_import_value_usd = df.iloc[world_row_idx]["20"].to_numpy()[0]
            world_import_value_usds_monthly.append(world_import_value_usd)
            period_keys.append(month_key)
            pass
        except pd.errors.EmptyDataError:
            world_import_value_usds_monthly.append(0)
            period_keys.append(month_key)
            pass

# section_232_date = datetime.date(year=2018, month=3, day=18)


# plotting
plt.figure(1, figsize=(10, 6))
plt.plot(
    period_keys[120:245], world_import_value_usds_monthly[120:245]
)  # , label="US Steel Imports Total (HS 72)")
plt.scatter(dates, [2500000000] * len(dates), c="red", label="AD Orders On Steel")

# plt.plot(
#     period_keys, world_import_value_usds_monthly
# )  # , label="US Steel Imports Total (HS 72)")

# plt.plot(
#     year_keys, world_import_value_usds_annual
# )

plt.xlabel("Period")
plt.ylabel("Total Value Imported USD")
plt.title("US Steel & Iron Imports Total (HS 72)")

plt.legend(loc="upper left")
plt.show()

if __name__ == "__main__":
    pass
