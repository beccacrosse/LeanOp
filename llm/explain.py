from llm.schema import RecommendationExplanation
from llm.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

def generate_explanation(llm_client, analysis_result):
    ''' 
    We write the prompt template once, fill it with analysis results 
    at runtime, and send only the filled-in prompt to the LLM, while 
    enforcing a strict output schema on the response.
    '''
    
    
    # populate user prompt template using real data from analysis_result
    prompt = USER_PROMPT_TEMPLATE.format(**analysis_result)

    # send the prompts to the llm, and stores parsed system response in response variable 
    response = llm_client.chat(
        system=SYSTEM_PROMPT,
        user=prompt,
        response_model=RecommendationExplanation # parse the response using the schema
    )

    return response
