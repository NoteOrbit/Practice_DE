import polars as pl
import datetime
from db import  execute

def calculate_missing_timestamps(rows, frequency):
    try:
        if not rows:
            raise ValueError("No data provided")

        if frequency == '5min':
            rows = [row[0] for row in rows]
            complete = pl.datetime_range(min(rows), max(rows), '5m', eager=True)
            return [dt.isoformat() for dt in set(complete) - set(rows)]
        elif frequency == '30min':
            round_down = lambda dt: dt - datetime.timedelta(minutes=dt.minute % 30, seconds=dt.second, microseconds=dt.microsecond)
            rows = [round_down(row[0]) for row in rows]
            complete = pl.datetime_range(min(rows), max(rows), '30m', eager=True)
            return [dt.isoformat() for dt in set(complete) - set(rows)]
        elif frequency == 'H':
            rows = [row[0] for row in rows]
            complete = pl.datetime_range(min(rows), max(rows), '1h', eager=True)
            return [dt.isoformat() for dt in set(complete) - set(rows)]
    except Exception as e:
        print(f"An error occurred: {e}")

def logic(table_times, conn):
    table_column_map = {
        'REGIONSUM': ['SETTLEMENTDATE', '5min'],
        'PRICE': ['SETTLEMENTDATE', '5min'],
        'INTERCONNECTORRES': ['SETTLEMENTDATE', '5min'],
        'PREDISPATCHPRICE': ['LASTCHANGED', '30min'],
        'PREDISPATCHREGIONSUM': ['LASTCHANGED', '30min'],
        'PREDISPATCHINTERCONNECTORRES': ['LASTCHANGED', '30min'],
        'P5MIN_REGIONSOLUTION': ['RUN_DATETIME', '5min'],
        'P5MIN_INTERCONNECTORSOLN': ['RUN_DATETIME', '5min'],
        'STPASA_REGIONSOLUTION': ['RUN_DATETIME', 'H'],
        'STPASA_INTERCONNECTORSOLN': ['RUN_DATETIME', 'H']
    }

    result = {}

    for table_name, times in table_times.items():
        start_timestamp = times.get('start_timestamp')
        end_timestamp = times.get('end_timestamp')
        if start_timestamp and end_timestamp and table_name in table_column_map:
            column = table_column_map[table_name][0]
            frequency = table_column_map[table_name][1]
            data = execute(table_name, column, start_timestamp, end_timestamp, conn)
            print(f"Executed query for {table_name}")
            print(f"Start timestamp: {start_timestamp}")
            print(f"End timestamp: {end_timestamp}")
            
            if data:
                result[table_name] = {'missing_timestamps': calculate_missing_timestamps(data, frequency)}
            else:
                result[table_name] = []
        else:
            result[table_name] = []

    return result