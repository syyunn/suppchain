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

years = [i for i in range(1988, 2020)]

for year in years:
    try:
        crsr = connection.cursor()
        crsr.execute(
            f"""select * from raw___uncmtrd.annual where year = {year} and aggregate_level = 2 and trade_flow = 'Import' and commodity_code ='72' and reporter_code = 842;
        """
        )
        df = pd.DataFrame(crsr.fetchall())
        # print(df)
        df.to_csv(
            f"../../data/us_steel_imports_annual/year{year}_agg2_tfImport_reporterCode842_commodityCode72.csv",
            sep=",",
            index=False,
        )
        print("done", year)

    except psycopg2.OperationalError:
        print("error occurred", year)
        pass

if __name__ == "__main__":
    pass
