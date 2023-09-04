# Assigning NAICS codes to Kickstarter projects, using the ChatGPT API from OpenAI

### Introduction

The goal of this project is to assign NAICS codes to Kickstarter projects. 

[Kickstarter](https://www.kickstarter.com/) is a crowdfunding website to raise money for creative projects. The [North American Industry Classification System](https://www.census.gov/naics/) (NAICS) is a standard for classifying businesses on the basis of their type of economic activity.

We started with already-scraped [data about Kickstarter projects](https://webrobots.io/kickstarter-datasets/) from 2014 to 2023. We used the ChatGPT API (model `gpt-3.5-turbo`) to assign NAICS codes to these projects, on the basis of these four fields available from the data: 

 - Name (Title of the project) 
 - Blurb  (A short description of the project)
 - Kickstarter category  
 - Kickstarter subcategory

### Prerequisites

- Open an [OpenAI account](https://platform.openai.com/signup) and generate an [OpenAI API key](https://platform.openai.com/account/api-keys).   
- Install the requirements by typing the following on the terminal:
	`pip install -r requirements.txt`

### Usage

- **Create input data file**: Read the raw data (which is in JSON format) into an input CSV file containing,  at a minimum, the project id and the fields you want to use as your input to ChatGPT. Here the fields `name`, `blurb`, `category` and `subcategory` have been used.

- **Obtain OpenAI API key**: Set the OpenAI key as an environment variable. 
  - On Linux, type in the terminal:
 
   `export OPENAI_API_KEY=<your openai api key>`
  - On Windows, type in the command prompt:
  
   `setx OPENAI_API_KEY <your openai api key>`
- **Create configuration file**: Specify user-defined variables in the `config.json` file.
- **Run program**: Run the program from the terminal:

  `python src/assign_naics_code.py`

### Input
The input is a CSV file with information about Kickstarter projects. Here is an example with a few rows and the relevant columns shown:

| name | blurb | category | subcategory|                                                                                                            
|--|--|--|--
 Herbal Teas                                                 | All your herbal tea remedies here. From colds and sore throats to cramps and stress relaxation, you can find it here.          | Food         | Drinks         
| The Meat Candy Experience                                   | The BEST beef sticks, beef jerky and signature sauces you will find anywhere...PERIOD.                                         | Food         | Small batch    
| WHILE THE TREES SLEEP                                       | CalArts thesis film inspired by true events surrounding the 1965 murder of Civil Rights activist Viola Liuzzo.                 | Film & video | Shorts 
| Orage: Interactive Lightning Experience at Burning Man 2015 | A Musical Lightning Storm. Get struck by lightning while collaboratively playing music with a 18-foot-tall musical Tesla Coil. | Art  | Installations  
Graphic design tools for award-winning designs              | Professional graphic designers need professional tools. These are the best.                                                    | Design       | Graphic design 
| The Gettysburg Story                                        | America’s greatest battle as you have never seen it before:  'The Gettysburg Story' on public television.                      | Film & video | Television

### Output

The output is a CSV file which is the input file with additional columns containing the NAICS codes as well as the number of input tokens used and the output tokens produced by ChatGPT. Here is the output corresponding to the example input above, with the NAICS codes being from the year 2017:

| name | blurb | category | subcategory |  naics code | input tokens | output tokens                                                                                                          
|--|--|--|--|--|--|--
| Herbal Teas                                                 | All your herbal tea remedies here. From colds and sore throats to cramps and stress relaxation, you can find it here.          | Food         | Drinks         |         7223 |            108 |               2 
| The Meat Candy Experience                                   | The BEST beef sticks, beef jerky and signature sauces you will find anywhere...PERIOD.                                         | Food         | Small batch    |         3116 |            101 |               2 
| WHILE THE TREES SLEEP                                       | CalArts thesis film inspired by true events surrounding the 1965 murder of Civil Rights activist Viola Liuzzo.                 | Film & video | Shorts         |         5121 |            111 |               2 
| Orage: Interactive Lightning Experience at Burning Man 2015 | A Musical Lightning Storm. Get struck by lightning while collaboratively playing music with a 18-foot-tall musical Tesla Coil. | Art          | Installations  |         7113 |            115 |               2 
| Graphic design tools for award-winning designs              | Professional graphic designers need professional tools. These are the best.                                                    | Design       | Graphic design |         5414 |             97 |               2 
| The Gettysburg Story                                        | America’s greatest battle as you have never seen it before:  'The Gettysburg Story' on public television.                      | Film & video | Television     |         5121 |            110 |               2 |

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
