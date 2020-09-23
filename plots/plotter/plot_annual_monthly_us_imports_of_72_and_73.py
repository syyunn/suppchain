import pandas as pd
import matplotlib.pyplot as plt
import datetime
import plots.plotter.utils as utils

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
years = [str(i) for i in range(2000, 2021)]
# years = [str(i) for i in range(2010, 2021)]


year_keys = []
world_import_value_usds_annual = []


period_keys = []
world_import_value_usds_monthly_72 = []
world_import_value_usds_monthly_73 = []


df_72 = pd.read_csv("../../data/usitc_ad_orders/orders.csv")
df_orders = pd.read_csv("../../data/usitc_ad_orders/orders.csv")

dates = [utils.change_to_datetime(date) for date in df_orders["order_date"].to_list()]
dates = [date for date in dates if date.year >= 2010]
for year in years:
    for month in months:
        period = int(year + month)
        month_key = datetime.date(
            year=int(year), month=int(month[0].replace("0", "") + month[1]), day=1
        )

        csv_72 = f"/Users/suyeol/suppchain/data/us_steel_imports_monthly_72/period{period}_agg2_tfImports_reporterUS_commcode72.csv"
        csv_73 = f"/Users/suyeol/suppchain/data/us_steel_imports_monthly_73/period{period}_agg2_tradeFlowImports_reporterCode842_commodityCode73.csv"
        try:
            df_72 = pd.read_csv(csv_72)
            world_row_idx = df_72.index[df_72["12"] == "World"].tolist()
            world_import_value_usd = df_72.iloc[world_row_idx]["20"].to_numpy()[0]
            world_import_value_usds_monthly_72.append(world_import_value_usd)

            df_73 = pd.read_csv(csv_73)
            world_row_idx = df_73.index[df_73["12"] == "World"].tolist()
            world_import_value_usd = df_73.iloc[world_row_idx]["20"].to_numpy()[0]
            world_import_value_usds_monthly_73.append(world_import_value_usd)

            period_keys.append(month_key)
            pass
        except pd.errors.EmptyDataError:
            world_import_value_usds_monthly_72.append(0)
            world_import_value_usds_monthly_73.append(0)

            period_keys.append(month_key)
            pass

# section_232_date = datetime.date(year=2018, month=3, day=18)


# plotting
plt.figure(1, figsize=(10, 6))
plt.plot(
    period_keys[120:245], world_import_value_usds_monthly_72[120:245], label="US Imports of HS Chapter 72")

plt.plot(
    period_keys[120:245], world_import_value_usds_monthly_73[120:245],  label="US Imports of HS Chapter 73"
)

plt.plot(
    period_keys[120:245], [x + y for x, y in zip(world_import_value_usds_monthly_72, world_import_value_usds_monthly_73)][120:245], label = "US Steel & Iron Import Total (USD)"
)  # , label="US Steel Imports Total (HS 72)")

plt.scatter(dates, [5000000000] * len(dates), c="red", label="AD/CVD Orders On Steel")

plt.xlabel("Period")
plt.ylabel("Total Value Imported USD ($B)")
plt.title("US Steel & Iron Imports")

plt.legend(loc="upper left")
plt.show()

if __name__ == "__main__":
    pass
