'''
Driver function for NAICSCodeAssigner class
'''

import os
import json
from naics_code_assigner import NAICSCodeAssigner

def main():

    '''
    Main function:
        Reads in the OPEN API key which must be set as an environment variable.
        Loads user-defined variables from the config file.
        Creates an instance of the NAICSCodeAssigner class
        and calls its obtain_naics_code function, to assign NAICS codes
        to the data in the input file.
    '''
    # Read the OpenAI API key
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if not openai_api_key:
        raise ValueError("OpenAI API key not found. \
                          Ensure it is set as an environment variable.")

    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    # Create an instance of the class
    assigner = NAICSCodeAssigner(**config)

    # Obtain NAICS codes
    assigner.obtain_naics_codes()

if __name__ == "__main__":
    main()
