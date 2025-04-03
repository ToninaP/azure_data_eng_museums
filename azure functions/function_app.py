import azurefunctions as func
import logging
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger_moderna")
def http_trigger_moderna(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    #  we need to download web content
    url = "https://sis.modernamuseet.se/en/objects/"  # saving link in the working memory; "=" means "assign value to a variable"s

    data_list = []  # we create an empty list, so we will attach scraped data there
    for i in range(0, 10):

        try:  # try/except used to give the machine instructions what to do if the code does not work
            fullUrl = url + str(
                i
            )  # in the cycle we change the webpage address, so we could scrape one page by one
            print(fullUrl)
            page = requests.get(
                fullUrl, timeout=300
            )  # we download the page we want to take data from
            soup = BeautifulSoup(
                page.content, "html.parser"
            )  # we make this page more readable for the machine and human

            row = (
                {}
            )  # we create an new row with data; {} means empty dictionary (it is a data structure, like a list)

            row["url"] = (
                fullUrl  # we create a first column and put there the link to a source page
            )
            row["i"] = (
                i  # we create a second column and assign it the number of the cycle
            )
            # this is the section to copypaste and change tags to extracts another column with data
            # in this section we are creating a column with the artist name
            try:
                row["artist_name"] = soup.find("span", {"property": "name"}).text.strip(
                    "\n"
                )  # this is our main command
            except:
                row["artist_name"] = (
                    None  # this is what we tell the machine to do if it cannot execute the main command
                )
                # if the requested page was empty, the machine would not find the information and would stop
                # so we are telling it to write that the section was empty (None means empty value)
                pass  # here we tell to continue
            # in this section we are creating a column with the artwork name
            try:
                row["artwork_name"] = (
                    soup.find_all("div", {"class": "detailField titleField"})[0]
                    .text.strip()
                    .split("\n")[0]
                )
            except:
                row["artwork_name"] = None
                pass

            data_list.append(
                row
            )  # we save the row in the list we created in the beginning
            df = pd.DataFrame(
                data_list
            )  # we make this list a dataframe (a table in Python)
        except:
            print(i)
        pass
