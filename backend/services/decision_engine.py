def decision_engine(expenses_df, usage_df):
    """
    Decision engine that takes in expenses and usage data and returns a decision dict to use in LLM prompt
    
    
    """
    # Calls utilization analysis
    utilization_df = analyze_utilization(expenses_df, usage_df)
    # Calls savings estimator
    savings_df = estimate_savings(utilization, seats, monthly_cost)
    # Calls risk scoring
    risk_df = score_risk(savings_df)

    # Produces a single analysis_result dict
    analysis_result = {
        "utilization": utilization_df,
        "savings": savings_df,
        "risk": risk_df
    }

    return analysis_result