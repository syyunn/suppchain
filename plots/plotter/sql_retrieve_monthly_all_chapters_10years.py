import psycopg2
import auth
import pandas as pd
import plots.plotter.utils as utils


connection = psycopg2.connect(
    user=auth.user,
    password=auth.password,
    host=auth.host,
    port=auth.port,
    database=auth.database,
)  # please make sure to run ssh -L <local_port>:localhost:<remote_port> <user_at_remote>@<remote_address>

conn_status = connection.closed  # 0

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
years = [str(i) for i in range(2010, 2021)]
chapters = [utils.fill_up_to_2digit(str(i)) for i in range(1, 98)]

pass
for chapter in chapters:
    for year in years:
        for month in months:
            period = int(year + month)
            try:
                crsr = connection.cursor()
                crsr.execute(
                    f"""select * from raw___uncmtrd.monthly m where period = {period} and aggregate_level = 2 and trade_flow = 'Imports' and commodity_code=\'{chapter}\' and reporter_code = 842 and partner_code = 0;
                """
                )
                df = pd.DataFrame(crsr.fetchall())
                df.to_csv(
                    f"../../data/10year_us_imports_monthly_all_chapters/period{period}_agg2_tradeFlowImports_reporterCode842_partnerCode0_commodityCode{chapter}.csv",
                    sep=",",
                    index=False,
                )
                print(period, chapter)
            except psycopg2.OperationalError:
                print("error occurred", period, chapter)
                pass

if __name__ == "__main__":
    pass
