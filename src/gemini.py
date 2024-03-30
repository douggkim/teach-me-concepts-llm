import google.generativeai as genai
from utils.logger import logger

class gemini_bot: 
    def __init__(self, api_key:str, model_name:str='gemini-pro'): 
        """initializes gemini or other google language models 

        Args:
            model_name (str): model name. `gemini-pro` by default
            api_key (str): api-keys to use the api
        """
        self.model_name = model_name
        self.api_key = api_key 
        self.model = self.init_model()
    
    def init_model(self): 
        try: 
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel(self.model_name)
            return model 
        except Exception as e: 
            logger.error(f"Error occured while initiating the model: {e}")
            return None 
        
    def get_client(self): 
        return self.model
    
    def chat(self, message:str, temp:float=1.0) -> str: 
        """send message to model and get response

        Args:
            message (str): prompt to be sent to the model 
            temp (float): temperature for chat generation. Higher the variable the result

        Returns:
            text: response from the chatbot
        """
        try: 
            response = self.model.generate_content(message, 
                                                   generation_config=genai.types.GenerationConfig(
                                                       candidate_count=1,
                                                       temperature=temp)
                                                   )
            response_length = len(response.candidates)
            
            if response and response_length != 0: # if the response is properly received
                response_text = response.candidates[0].content.parts[0].text
                return response_text 
            else: 
                return "" 
            
        except Exception as e:
            # Log or handle any other potential errors:
            print(f"Error occurred during API call: {e}")
            return ""  # Return an empty string on general errors
        
        
    
    
        