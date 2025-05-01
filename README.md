# azure_data_eng_museums
this is a personal project to showcase my data engineering skills

The project diagram is stored here https://azurediagrams.com/XwuHo1bY

Data processing diagram:

![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/data_prossessing.png)
Ingestion of data:
1. Fetching raw data with Azure Data Factory pipelines and saving it to the Raw layer of the datalake.
   - first pipeline is looping over csv sources (files stored on GitHub)
   - second pipeline is looping over json sources (files rerceived as API requests)
![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/ingestion_pipeline.png)
![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/csv_pipeline.png)

Database schema:

![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/star_schema.svg)

