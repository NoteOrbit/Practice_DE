## Function: Find_Missing

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
