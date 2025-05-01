# azure_data_eng_museums

this is a personal project to create a cloud data storage, analysis and visualisation solution. In this pilot projest only 3 datasets are processed; the final version will include 40+ datasets.
Requirements: a research project does not have a data storage solution due to low capabilities on premises (the university does not have a unified server storing all data involved in all labs; the research project does not have an engineer to create a data validation and storage solution). A cloud solution is required for international collaboration with the minimal cost involved.

The project diagram is stored here https://azurediagrams.com/XwuHo1bY

Data processing diagram:

![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/data_prossessing.png)

Ingestion of data:

![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/ingestion_pipeline.png)

1. Fetching raw data with Azure Data Factory pipelines and saving it to the Raw layer of the datalake.
   - first pipeline is looping over csv sources (files stored on GitHub)
   - second pipeline is looping over json sources (files rerceived as API requests)

![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/csv_pipeline.png)

Data standardization:

2. Using Azure Data Factory every dataset goes through individual trransformations and has the same schema in the output.
![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/standardization_pipelline.png)
- some transformations are complext and require multiple flattening, joins, and creating new derived columns
 ![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/complex_data_flow.png) 
- other transformations are straightforward and require selecting, renaming and type casting for columns
![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/simple_data_flow.png)

All the files are stored in a Parquet format in a Standardized Layer of the datalake
 

Database schema:

![alt text](https://github.com/ToninaP/azure_data_eng_museums/blob/main/docs/graphs/star_schema.svg)

