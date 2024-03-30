from typing import Dict, List 
import json
from utils.logger import logger 
import pandas as pd
import os 

def parse_json_text(text:str) -> List[Dict]: 
    """Parses plain text containing json-formatted text and converts it to a list of dictionaries

    Args:
        text (str): text containing json-formatted data

    Returns:
        List[Dict]: list of dictionaries
    """
    #Extract JSON data
    logger.info("Parsing the json line text to a list of dictionaries")
    start_index = text.find('```json') + len('```json')
    end_index = text.find('```', start_index)
    json_data = text[start_index:end_index]

    json_list = json.loads(json_data)
    
    return json_list


    