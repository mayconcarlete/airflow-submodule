import pandas as pd
from pyathena.pandas.util import as_pandas
from pyathena import connect
from engine.common.utils import load_config_file_to_dict

# Add support to  jinja
# Add support to run locally with Minio

def entrypoint(**kwargs) -> dict[str, pd.DataFrame]:
    print(f'Available resources: {kwargs}')
    etl = kwargs.get("etl")
    sqls = etl.get("sqls")
    s3_staging_dir = etl.get("s3_staging_dir")
    region = etl.get("region")
    cursor = connect(s3_staging_dir=s3_staging_dir, region_name=region).cursor()
    etl_results = {}
    for sql_table, sql in sqls.items():
      print(f'Using the following sql to run the query: {sql}')
      cursor.execute(sql)
      etl_results[sql_table] = as_pandas(cursor=cursor)
      # print(etl_results.get("mistplayetl.users"))
    return etl_results

# if __name__ == "__main__":
#     path = "/home/maycon/dev/airflow/airflow-submodule/templates/{{cookiecutter.monitoring_name}}/config.json"
#     configs = load_config_file_to_dict(path)
#     result = entrypoint(configs=configs)
#     print(result)
