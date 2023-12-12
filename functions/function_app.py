import azure.functions as func
import json
import time
from process import logic
from db import create_db_connection , execute
import logging


app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="http_trigger",auth_level=func.AuthLevel.ANONYMOUS , methods=["GET"])
def main(req: func.HttpRequest) -> func.HttpResponse:
    table_times = req.params.get('table_times')

    print(table_times)
    if not table_times:
        try:
            req_body = req.get_json()
            print(req_body)
        except ValueError:
            pass
        else:
            table_times = req_body.get('table_times')

    if table_times:
        conn = create_db_connection()
        start_time = time.time()
        result = logic(table_times, conn)
        end_time = time.time()
        runtime = end_time - start_time
        logging.info(result)
        conn.close()

        result_with_runtime = {**result, 'runtime': runtime}


        return func.HttpResponse(json.dumps(result_with_runtime), mimetype="application/json")