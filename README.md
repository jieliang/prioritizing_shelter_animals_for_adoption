
## Description of submitted files

### Project Description Slides
* prioritizing_shelter_animals_for_adoption_slides.pdf

### Data cleaning and transformation

* clean_animal_services_data.ipynb : cleans animal services data
* clean_animal_services_data_save_to_database.ipynb : saves cleaned animal services data as a table named animal_services in aws postgres database
* clean_economic_index_data.ipynb : cleans economic data and saves it as a table named economic_index in aws postgres database
* clean_expenditures_data.ipynb : cleans animal services department expenditure data and saves it as a table named expenses in aws postgres database

### Modelling 

* model_selection.ipynb : joins tables in database as clean data for modelling; tries different models and selects winner based on metrics
* model_evaluation.ipynb : plots and compares roc curves of finalists and winner from model selection

### Data directory(not included in submission because size exceeds git hub limit)
* downloaded csv files from data sources
* saved pickle files

### Flask directory
* files for creating web based app that takes in user input and returns prediction using selected model

### Helper file
* generate_template_for_flask_api.ipynb : generates a template filled with some default values for api.py in flask directory to use

