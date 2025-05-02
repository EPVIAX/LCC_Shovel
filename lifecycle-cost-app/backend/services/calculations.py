def calculate_lifecycle_cost(initial_cost, maintenance_cost, operational_cost, lifespan_years):
    total_cost = initial_cost + (maintenance_cost * lifespan_years) + (operational_cost * lifespan_years)
    return total_cost

def calculate_annual_cost(total_cost, lifespan_years):
    if lifespan_years <= 0:
        raise ValueError("Lifespan must be greater than zero.")
    return total_cost / lifespan_years

def calculate_cost_per_use(total_cost, total_uses):
    if total_uses <= 0:
        raise ValueError("Total uses must be greater than zero.")
    return total_cost / total_uses

def calculate_discounted_cost(total_cost, discount_rate, years):
    discounted_cost = total_cost / ((1 + discount_rate) ** years)
    return discounted_cost