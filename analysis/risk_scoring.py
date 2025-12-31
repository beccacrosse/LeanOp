def score_risk(savings_df):
    """ risk scoring fucnt
    """
    # Calculate risk score
    risk_score = savings_df['savings'] / savings_df['monthly_cost']
    return risk_score