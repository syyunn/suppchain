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

try:
    crsr = connection.cursor()
    crsr.execute(
        """select * from raw___uncmtrd.monthly m where period = 202001 and aggregate_level = 2 and trade_flow = 'Imports' and commodity_code ='72' and reporter_code = 842;
    """
    )
    df = pd.DataFrame(crsr.fetchall())
    print(df)
except psycopg2.OperationalError:
    pass

if __name__ == "__main__":
    pass
