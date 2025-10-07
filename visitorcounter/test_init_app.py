import os
os.environ["COSMOSDB_CONNECTION_STRING"] = "fake_connection_string"

import azure.functions as func
from unittest.mock import patch, MagicMock
from visitorcounter.VisitorCounterFunction import main


@patch("visitorcounter.VisitorCounterFunction.TableServiceClient")
def test_main(mock_table_client):
    # Mock the Table client and table operations
    mock_instance = MagicMock()
    mock_table_client.from_connection_string.return_value = mock_instance
    mock_table = MagicMock()
    mock_instance.get_table_client.return_value = mock_table

    # Mock get_entity and update_entity
    mock_table.get_entity.return_value = {"PartitionKey": "1", "RowKey": "1", "Count": 5}
    mock_table.update_entity.return_value = None

    # Create an HTTP request
    req = func.HttpRequest(
        method="GET",
        body=None,
        url="/api/VisitorCounterFunction"
    )

    # Call the function
    resp = main(req)

    # Verify
    assert resp.status_code == 200
    assert resp.get_body().isdigit()  # 👈 This must be INSIDE the test_main() function
