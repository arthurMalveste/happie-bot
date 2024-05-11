
import google.generativeai as genai
from apikey import *

# configuracoes

GOOGLE_API_KEY= "AIzaSyDiUvSpASqqkBm-nwD5O-KWKbLSdxwM1wQ"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "candidate_count": 1,
  "temperature": 1,
}

safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                            generation_config=generation_config,
                            safety_settings=safety_settings,)