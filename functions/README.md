##  Azure Functions

### Objective

Find missing data from real time given conditions.


### Description
This function is the main entry point for the Azure Function App. It processes an HTTP request, retrieves the 'table_times' parameter from the request, and calls the `logic` function to process the data. The results are returned as an HTTP response.

### Parameters
- `req` (func.HttpRequest): The HTTP request object.

### Returns
- `func.HttpResponse`: The HTTP response object. The body of the response contains a JSON object with the results from the `logic` function. If the 'table_times' parameter is not provided in the request, the function returns an empty response.

### Input
The input is a JSON object in the body of an HTTP request. The object has a single property, `table_times`, which is another object. Each property of `table_times` is the name of a table, and the value is an object with `start_timestamp` and `end_timestamp` properties.

```json
{
    "table_times": {
        "<table_name>": {
            "start_timestamp": "<start_timestamp>",
            "end_timestamp": "<end_timestamp>"
        },
        // ... more tables
    }
}
```

- <table_name>: The name of a table. Replace this with the actual table name.
- <start_timestamp>: The start timestamp in the format 'YYYY-MM-DD HH:MM:SS'. Replace this with the actual start timestamp.
- <end_timestamp>: The end timestamp in the format 'YYYY-MM-DD HH:MM:SS'. Replace this with the actual end timestamp.


### Output
The output is a JSON object in the body of an HTTP response. The object has the same structure as the input, but each table object has an additional `missing_timestamps` property, which is an array of missing timestamps.

```json
{
    "<table_name>": {
        "start_timestamp": "<start_timestamp>",
        "end_timestamp": "<end_timestamp>",
        "missing_timestamps": ["<missing_timestamp>", ...]
    },
    // ... more tables
}
```
- <missing_timestamp>: A missing timestamp in the format 'YYYY-MM-DD HH:MM:SS'. Replace this with the actual missing timestamp.

### Example
This function is automatically called by the Azure Functions runtime when an HTTP request is made to the function's endpoint. Here's an example of how you might call this function with an HTTP request:


```http
GET /api/http_trigger HTTP/1.1
Host: localhost:7071
Content-Type: application/json

{
    "table_times": {
        "P5MIN_REGIONSOLUTION": {
            "start_timestamp": "2022-01-01 00:00:00",
            "end_timestamp": "2022-01-31 23:59:59"
        },
        "P5MIN_INTERCONNECTORSOLN": {
            "start_timestamp": "2022-01-01 00:00:00",
            "end_timestamp": "2022-01-31 23:59:59"
        }
    }
}

```
```json
{
    "P5MIN_REGIONSOLUTION": {
        "start_timestamp": "2022-01-01 00:00:00",
        "end_timestamp": "2022-01-31 23:59:59",
        "missing_timestamps": [
            "2022-01-05 00:00:00",
            "2022-01-10 00:00:00",
            "2022-01-15 00:00:00"
        ]
    },
    "P5MIN_INTERCONNECTORSOLN": {
        "start_timestamp": "2022-01-01 00:00:00",
        "end_timestamp": "2022-01-31 23:59:59",
        "missing_timestamps": [
            "2022-01-02 00:00:00",
            "2022-01-07 00:00:00",
            "2022-01-12 00:00:00"
        ]
    }
}
```
# Project Components

This project consists of several Python scripts that work together to perform a series of tasks. Below is a brief description of each script's role in the project.


## functions_app.py

### main(req: func.HttpRequest) -> func.HttpResponse

This function is the main entry point for the application. It is triggered by an HTTP request and returns an HTTP response.

The function first retrieves the `table_times` parameter from the request. If the parameter is not found in the request parameters, it tries to retrieve it from the request body.

If the `table_times` parameter is found, the function creates a database connection and records the start time. It then calls the `logic` function from the `process` module, passing the `table_times` parameter and the database connection. The `logic` function processes the data and returns a result.

The function then records the end time and calculates the runtime by subtracting the start time from the end time. It logs the result and closes the database connection.

Finally, the function adds the runtime to the result and returns it as a JSON-formatted HTTP response.

If the `table_times` parameter is not found in either the request parameters or the request body, the function does not perform any processing and does not return a response.



## process.py

### calculate_missing_timestamps(rows, frequency)

This function calculates the missing timestamps in the data. It takes two parameters:

- `rows`: The rows of data returned from the database. Each row is expected to contain a timestamp.
- `frequency`: The frequency at which the data should be sampled. This can be '5min', '30min', or 'H' (hourly).


### logic(table_times, conn)

This function processes the data for a set of tables. It takes two parameters:

- `table_times`: A dictionary mapping table names to a pair of a column name and a frequency.
- `conn`: The database connection object.

The function initializes an empty dictionary `result` to store the results.

## db.py

### create_db_connection()

This function establishes a connection to the PostgreSQL database. It reads the database configuration (database name, user, password, host, and port) from environment variables, which are loaded using the `dotenv` library. If the connection is successful, it prints a success message and returns the connection object. If an error occurs during the connection, it prints the error message.

### execute(table_name, column, start_timestamp, end_timestamp, conn)

This function executes a SQL query on the database. It takes five parameters:

- `table_name`: The name of the table in the database to query.
- `column`: The name of the column in the table to select.
- `start_timestamp`: The start of the timestamp range for the query.
- `end_timestamp`: The end of the timestamp range for the query.
- `conn`: The database connection object.
