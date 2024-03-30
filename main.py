from dotenv import load_dotenv
import os 
from pathlib import Path 
import pandas as pd 

from data.prompt_template import prompt_template
from data.topics import topics
from src.gemini import gemini_bot
from utils.formatter import parse_json_text
from utils.logger import logger 

logger.info("Loading variables")
load_dotenv()
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
MODEL_NAME = os.environ['MODEL_NAME']

SECOND_LANGUAGE = os.environ["SECOND_LANGUAGE"]
OUTPUT_COLUMNS_RAW = os.environ['OUTPUT_COLUMNS']
OUTPUT_COLUMNS_FORMATTED = OUTPUT_COLUMNS_RAW.format(second_language=SECOND_LANGUAGE)
OUTPUT_COLUMNS = eval(OUTPUT_COLUMNS_FORMATTED)
OUTPUT_FILE_NAME = os.environ["OUTPUT_FILE_NAME"]
output_path = Path("./output")

MAX_TRY = int(os.environ['MAX_TRY'])


if __name__ == "__main__": 
    # set up the variables 
    gemini_bot_inst = gemini_bot(api_key=GEMINI_API_KEY, model_name=MODEL_NAME) 
    result_df = pd.DataFrame(columns=OUTPUT_COLUMNS)
    failed_text = []
    
    for field in topics: 
        for sub_field in topics[field]: 
            for topic in topics[field][sub_field]: 
                trial_num = 1 
                current_progress = f"field: {field} /// sub_field: {sub_field} /// topic: {topic}"
                while trial_num <= MAX_TRY: 
                    logger.info(f"{current_progress}  try #{trial_num}")
                    try: 
                        logger.info("formatting prompt") 
                        prompt_template_formatted = prompt_template.format(
                            field=field,
                            sub_field=sub_field,
                            topic=topic,
                            columns=OUTPUT_COLUMNS,
                            language=SECOND_LANGUAGE
                        )
                        logger.info("talking to gemini")
                        response = gemini_bot_inst.chat(
                            temp=0.4,
                            message=prompt_template_formatted
                        )
                
                        logger.info("parsing response from gemini")
                        response_json_list = parse_json_text(response)

                        logger.info("adding to pandas dataframe")
                        tmp_df = pd.DataFrame(response_json_list)
                        result_df = pd.concat([result_df, tmp_df]) # Concat to the result_df
                        
                        # house cleaning after success
                        response = None
                        break

                    except Exception as e: 
                        logger.error(f"Error occurred: {e}")
                        if response: 
                            fail_dict = {
                                current_progress: response
                            }
                            failed_text.append(fail_dict)
                        intermediary_output_file_name = OUTPUT_FILE_NAME.split(".")[0] + "_intermediary.csv"
                        intermediary_output_file_destination = output_path / intermediary_output_file_name
                        result_df.to_csv(intermediary_output_file_destination, encoding='utf-32', sep='\t', index=False)
                        trial_num += 1
    
    output_file_destination = output_path / OUTPUT_FILE_NAME
    result_df.to_csv(output_file_destination, encoding='utf-32', sep='\t', index=False)
    logger.error("These are the errors that occurred during the run:")
    logger.error(failed_text)



