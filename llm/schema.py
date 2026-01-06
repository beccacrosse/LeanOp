from pydantic import BaseModel, Field

''' This file contains the output contract (format) for the LLM to follow.
    output not in this format will be rejected''' 


class RecommendationExplanation(BaseModel):
    summary: str = Field(
        description="Concise explanation of the cost issue and why it matters"
    )
    recommendation: str = Field(
        description="Specific cost-saving action tied to the numeric analysis"
    )
    risk_explanation: str = Field(
        description="What could go wrong if this recommendation is applied"
    )
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="Model confidence in the recommendation"
    )


# import time
# from pydantic import ValidationError
# from llm.schema import RecommendationExplanation
# from llm.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

# MAX_RETRIES = 3
# RETRY_BACKOFF = 1.5  # seconds

# class LLMGenerationError(Exception):
#     pass

# def generate_explanation(llm_client, analysis_result):
#     prompt = USER_PROMPT_TEMPLATE.format(**analysis_result)
#     last_error = None

#     for attempt in range(1, MAX_RETRIES + 1):
#         try:
#             response = llm_client.chat(
#                 system=SYSTEM_PROMPT,
#                 user=prompt,
#                 response_model=RecommendationExplanation
#             )
#             return response

#         except ValidationError as e:
#             last_error = f"Schema validation failed: {e}"

#         except TimeoutError:
#             last_error = "LLM request timed out"

#         except Exception as e:
#             last_error = f"Unexpected LLM error: {e}"

#         time.sleep(RETRY_BACKOFF * attempt)

#     raise LLMGenerationError(
#         f"LLM failed after {MAX_RETRIES} attempts. Last error: {last_error}"
#     )
