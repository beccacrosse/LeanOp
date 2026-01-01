import pandas as pd

def analyze_utilization(expenses_df, usage_df):
    """
    Computes utilization = active_users / seats_purchased.
    Returns a DataFrame with vendor_name, month, and utilization.
    """

    # Merge the expenses and usage data on vendor and month to store both in a new dataframe called 'merged'
    merged = expenses_df.merge(
        usage_df,
        on=['vendor_name', 'month'],
        how='left'
    )

    # Calculate the utilization percentage and place in a new column called 'utilization'
    merged['utilization'] = (
        merged['active_users'] / merged['seats_purchased']
    ).fillna(0)

    # Return the merged data
    return merged[['vendor_name', 'month', 'utilization']]