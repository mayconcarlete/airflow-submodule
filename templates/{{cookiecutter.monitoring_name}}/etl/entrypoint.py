import sys
from loguru import logger
import pandas as pd
from pyathena.pandas.util import as_pandas
from pyathena import connect

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")



def entrypoint(**kwargs) -> dict[str, pd.DataFrame]:
    logger.info(f'Available resources: {kwargs}')
    etl = kwargs.get("etl")
    sqls = etl.get("sqls")
    s3_staging_dir = etl.get("s3_staging_dir")
    region = etl.get("region")
    cursor = connect(s3_staging_dir=s3_staging_dir, region_name=region).cursor()
    etl_results = {}
    for sql_table, sql in sqls.items():
      logger.info(f'Using the following sql to run the query: {sql}')
      cursor.execute(sql)
      etl_results[sql_table] = as_pandas(cursor=cursor)
      logger.info(etl_results.get(sql_table))
    return etl_results
