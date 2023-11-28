
import pandas as pd
from io import BytesIO
from rich.console import Console
from rich.table import Table


def create_dataframe(file_data, tag):
    byte_io = BytesIO(file_data)
    df = pd.read_excel(byte_io) if tag == 'Excel' else pd.read_csv(byte_io)
    df = set_date_format(df)
    return df

def show_dataframe(tag, file_name, df):
    console = Console()
    table = Table(title=f"Tag: {tag} - DataFrame: {file_name}")

    for col in df.columns:
        table.add_column(col)

    for _, row in df.iterrows():
        table.add_row(*[str(row[col]) for col in df.columns],style='bright_green')
    print('\n')
    console.print(table)
    print('\n')
    

def set_date_format(df, date_format='%Y-%m-%d'):
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.strftime(date_format)
    return df



