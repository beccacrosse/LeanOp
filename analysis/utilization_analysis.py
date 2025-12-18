import pandas as pd

def analyze_utilization(expenses_df, usage_df):
    """
    Utilization = active_users / seats
    Returns a new column with the utilization percentage
    """
    # Merge the expenses and usage data on vendor and month to store both in a new dataframe called 'merged'
    merged = expenses_df.merge(usage_df, on=['vendor', 'month'], how='left')
    # Calculate the utilization percentage and place in a new column called 'utilization'
    merged['utilization'] = merged['active_users'] / merged['seats']
    # Return the merged data
    return merged[ 'utilization''vendor', 'month']