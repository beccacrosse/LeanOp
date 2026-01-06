import statistics
from llm.explain import generate_explanation

def test_explanation_consistency(llm_client, analysis_result, runs=10):
    confidences = []
    summaries = []

    for _ in range(runs):
        response = generate_explanation(llm_client, analysis_result)
        confidences.append(response.confidence)
        summaries.append(response.summary)

    return {
        "confidence_std_dev": statistics.pstdev(confidences),
        "unique_summaries": len(set(summaries))
    }
