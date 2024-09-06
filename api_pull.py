import pandas as pd
import requests
import datetime
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from os import path


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://api.ouraring.com/v2/usercollection/sleep'

    params={
    'start_date': datetime.datetime.strptime('2022-05-01', '%Y-%m-%d').strftime('%Y-%m-%d'),
    'end_date': datetime.datetime.now().strftime('%Y-%m-%d')
    }

    header={
    'Authorization': 'Bearer X'
    }

    sleep = requests.request('GET', url, headers=header, params=params)

    sleep = sleep.json()

    sleep = pd.json_normalize(sleep['data'])

    sleep.rename(columns=lambda s: s.replace("contributors.", ""), inplace=True)

    return sleep
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    # Add more tests as needed

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_snowflake(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Snowflake warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#snowflake
    """
    table_name = 'SLEEP'
    database = 'RAW'
    schema = 'SLEEP'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            table_name,
            database,
            schema,
            if_exists='replace',  # Specify resolution policy if table already exists
        )
