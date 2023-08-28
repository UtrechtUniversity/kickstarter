# Assigning NAICS codes to Kickstarter projects, using the ChatGPT API from OpenAI

### Introduction

The goal of this project is to assign NAICS codes to Kickstarter projects. 

[Kickstarter](https://www.kickstarter.com/) is a crowdfunding website to raise money for creative projects. The [North American Industry Classification System](https://www.census.gov/naics/) (NAICS) is a standard for classifying businesses on the basis of their type of economic activity.

We started with already-scraped [data about Kickstarter projects](https://webrobots.io/kickstarter-datasets/) from 2014 to 2023. We used the ChatGPT API (model `gpt-3.5-turbo`) to assign NAICS codes to these projects, on the basis of these four fields available from the data: 

 - Title 
 - Blurb   
 - Kickstarter category  
 - Kickstarter subcategory

### Prerequisites

- Open an [OpenAI account](https://platform.openai.com/signup) and generate an[ OpenAI API key](https://platform.openai.com/account/api-keys).   
- Install the requirements by typing the following on the terminal:
`pip install -r requirements.txt`

### Usage

- **Create input data file**: Process the raw data (which is in JSON format) into an input CSV file containing,  at a minimum, the project id and the fields you want to use as your input to ChatGPT. We have used the fields title, blurb, category, and subcategory here.
- **Obtain OpenAI API key**: Set the OpenAI key as an environment variable. On Linux, this is done by typing on the terminal:
`export OPENAI_API_KEY=<your openai api key>`
- **Create configuration file**: Specify user-defined variables in the `config.json` file in the directory `src`.
- **Run program**: In the `src` directory, run the program from the terminal:
`python naics_code_assigner.py`

### Output

The output is a CSV file which is the input file with an additional column containing the NAICS codes.

### License

This project is licensed under the terms of the [MIT License](/LICENSE).

### About the project

**Date**: July - September 2023

**Researcher**:
- Nicola Cortinovis (n.cortinovis@uu.nl)

**Research Assistant**:
- Marte Vroom (m.m.vroom@uu.nl)

**Research Engineers**:
- Modhurita Mitra (m.mitra@uu.nl)
- Shiva Nadi Najafabadi (s.nadinajafabadi@uu.nl)
- Parisa Zahedi (p.zahedi@uu.nl)
