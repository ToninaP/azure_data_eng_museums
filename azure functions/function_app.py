import azurefunctions as func
import logging
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import io

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger_moderna")
def http_trigger_moderna(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    url = "https://sis.modernamuseet.se/en/objects/"

    data_list = []
    for i in range(0, 10):
        try:
            fullUrl = url + str(i)
            print(fullUrl)
            page = requests.get(fullUrl, timeout=300)
            soup = BeautifulSoup(page.content, "html.parser")

            row = {}

            row["url"] = fullUrl
            row["i"] = i

            try:
                row["artist_name"] = soup.find("span", {"property": "name"}).text.strip(
                    "\n"
                )
            except:
                row["artist_name"] = None

            try:
                row["artwork_name"] = (
                    soup.find_all("div", {"class": "detailField titleField"})[0]
                    .text.strip()
                    .split("\n")[0]
                )
            except:
                row["artwork_name"] = None

            data_list.append(row)
            df = pd.DataFrame(data_list)
        except:
            print(i)

    # Save DataFrame to CSV in memory (without saving to a file on disk)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_content = csv_buffer.getvalue()

    # Return CSV content in HTTP response
    return func.HttpResponse(
        csv_content,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=moderna_test.csv"},
    )
