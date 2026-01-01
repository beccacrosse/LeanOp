def score_risk(savings_df):
    """
    Scores risk based on the savings and monthly cost.
    Returns a DataFrame with vendor_name, month, and risk_score.
    risk is approximated as a bounded ratio of savings to spend, 
    which serves as a proxy for operational impact.
    """
    # Calculate risk score
    risk_score = savings_df['savings'] / savings_df['monthly_cost']
    # Bound the risk score to be between 0 and 1
    return risk_score.clip(lower=0, upper=1)