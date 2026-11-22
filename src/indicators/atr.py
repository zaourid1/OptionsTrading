"""
Building ATR in two steps:
    - true range for one candle
    - smmothing those ranges into ATR

ATR: averagr true range, measures market volatility.
Measures how much an assest moves, not which direction.
Highter ATR = Higher Volatility + Wider Price Swings
Lower ATR = Low Vilatility or Consolidation

true_ranges = [2,4,6,7,1]
ATR = (2+4+6)/3 = 4 (atr at day 3)
update it when another day arrives
new_atr = (p_atr x 2 + new true range) / 3
"""

def calculate_true_range(
    high: float,
    low: float,
    previous_close: float,
) -> float:
    """Return one candle's true range, including any gap."""
    if high < low:
        raise ValueError("High cannot be smaller than Low")
    if high <= 0 or low <= 0 or previous_close <= 0:
        raise ValueError("Prices must be positive")

    diference_highLow = high - low
    diference_highPC = abs(high - previous_close)
    diference_lowPC = abs(low - previous_close)

    return max(diference_highLow,diference_highPC,diference_lowPC)
    
#Adding Wilder's ATR calculation
def calculate_atr(
    true_ranges: list[float],
    period: int = 14,
) -> float:
    """Return the latest ATR using Wilder's smoothing."""
    if period <= 0:
        raise ValueError("Period must be postive")

    if len(true_ranges) < period:
        raise ValueError("Not enough Values")

    for value in true_ranges:
        if value < 0:
            raise ValueError("True ranges cannot be negative")
    
    #Starting with an ordinary avg
    atr = 0
    for i in range(period):
        atr += true_ranges[i]
    atr = atr/period #this gives us atr at end of day 3

    for i in range(period,len(true_ranges)):
        atr = (atr * (period - 1) + true_ranges[i]) / period

    return atr

if __name__ == "__main__":
    print(calculate_true_range(105.0, 99.0, 102.0)) #6.0
    #calculate_true_range(105.0, 99.0, 102.0)   # 6.0
    print(calculate_true_range(106.0, 103.0, 100.0))  # 6.0 — gap up
    print(calculate_true_range(97.0, 94.0, 100.0))    # 6.0 — gap down
    #calculate_true_range(94.0, 97.0, 100.0)    # ValueError

    print(calculate_atr([2.0, 4.0, 6.0, 7.0, 1.0], period=3))
    print(calculate_atr([2.0, 4.0, 6.0], period=3))            # 4.0
    print(calculate_atr([2.0, 4.0, 6.0, 7.0], period=3))       # 5.0
    print(calculate_atr([2.0, 4.0, 6.0, 7.0, 1.0], period=3))  # ≈ 3.6667