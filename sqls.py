import psycopg2
import auth
import pandas as pd


connection = psycopg2.connect(
    user=auth.user,
    password=auth.password,
    host=auth.host,
    port=auth.port,
    database=auth.database,
)  # please make sure to run ssh -L <local_port>:localhost:<remote_port> <user_at_remote>@<remote_address>

conn_status = connection.closed  # 0

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
years = [str(i) for i in range(2000, 2021)]

for year in years:
    for month in months:
        period = int(year + month)
        print(period)
        try:
            crsr = connection.cursor()
            crsr.execute(
                f"""select * from raw___uncmtrd.monthly m where period = {period} and aggregate_level = 2 and trade_flow = 'Imports' and commodity_code ='72' and reporter_code = 842;
            """
            )
            df = pd.DataFrame(crsr.fetchall())
            # print(df)
            df.to_csv(f"./us_steel_imports_monthly/period{period}_agg2_tfImports_reporterUS_commcode72.csv", sep=",", index=False)
        except psycopg2.OperationalError:
            print("error occurred", period)
            pass

if __name__ == "__main__":
    pass
