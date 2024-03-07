"""
Purpose:
  Include common use analytics for ease-of-access in this file.
"""


def sharpe(returns, returns_freq='1d'):
    """ Get the sharpe ratio based on the returns provided """

    shrp = returns.mean() / returns.std()
    shrp_annualized = shrp * ( 252 ** 0.5 )
    # TODO: Add logic so that 252 is not hard-coded i.e. 
    #       infer the scalar multiplier using returns_freq

    return shrp_annualized

