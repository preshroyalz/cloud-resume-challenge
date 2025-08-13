import azure.functions as func
import logging
import os
from azure.data.tables import TableServiceClient, UpdateMode
from azure.core.exceptions import ResourceNotFoundError

COSMOS_CONNECTION = os.environ["COSMOSDB_CONNECTION_STRING"]
TABLE_NAME = "VisitorCounter"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("VisitorCounterFunction triggered")

    try:
        service = TableServiceClient.from_connection_string(conn_str=COSMOS_CONNECTION)
        table_client = service.get_table_client(table_name=TABLE_NAME)

        try:
            entity = table_client.get_entity(partition_key="counter", row_key="visits")
            count = entity["Count"] + 1
        except ResourceNotFoundError:
            count = 1

        entity = {
            "PartitionKey": "counter",
            "RowKey": "visits",
            "Count": count
        }
        table_client.upsert_entity(entity=entity, mode=UpdateMode.REPLACE)

        return func.HttpResponse(str(count), status_code=200)

    except Exception as e:
        logging.error(f"Function error: {e}")
        return func.HttpResponse("Internal server error", status_code=500)
