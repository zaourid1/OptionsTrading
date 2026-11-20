"""
calculating levels

{
    "pivot": 500.0,
    "upper_0.5": 502.0,
    "lower_0.5": 498.0,
    "upper_1.0": 504.0,
    "lower_1.0": 496.0,
}
"""

def calculate_levels(
    session_open: float,
    previous_daily_atr: float,
    multipliers: tuple[float, ...] = (0.5, 1.0),
) -> dict[str, float]:
    """Return the opening pivot and ATR-based support/resistance levels."""
    #Opening Pivot = session open price
    #ATR-based supor: up by

    if session_open <= 0 or previous_daily_atr <= 0:
        raise ValueError("session_open or previous_daily_atr must be positive")
    

    prices = {'pivot':session_open}
    for m in multipliers:
        prices[f"upper_{m}"] = session_open + (previous_daily_atr * m)
        prices[f"lower_{m}"] = session_open - (previous_daily_atr * m)

    
    return prices

if __name__ == "__main__":
    print(calculate_levels(500.0, 4.0))
    