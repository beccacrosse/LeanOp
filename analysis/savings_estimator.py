def estimate_savings(utilization, seats, monthly_cost,target_utilization=.75):
    """
    Estimate savings by reducing seats to match target utilization.
    """
    if utilization >= target_utilization:
        return 0
    
    cost_per_seat = monthly_cost / seats
    recommended_seats = int(seats * target_utilization / utilization) #percent of seats being utilized at target utilization
    seat_reduction = max(seats - recommended_seats, 0)

    seat_savings = seat_reduction * cost_per_seat

    # add more savings estimates here


    #combine all savings estimates
    total_savings = seat_savings
    
    return round(seat_savings, 2) #return the total savings rounded to 2 decimal places