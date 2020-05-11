from statsmodels.compat.python import lzip
import numpy as np
from scipy import stats, optimize
from sys import float_info

from statsmodels.stats.base import AllPairsResults
from statsmodels.tools.sm_exceptions import HypothesisTestWarning


def proportion_confint(count, nobs, alpha=0.05, method='normal'):
    q_ = count * 1. / nobs
    alpha_2 = 0.5 * alpha

    if method == 'normal':
        std_ = np.sqrt(q_ * (1 - q_) / nobs)
        dist = stats.norm.isf(alpha / 2.) * std_
        ci_low = q_ - dist
        ci_upp = q_ + dist

    elif method == 'binom_test':
        # inverting the binomial test
        def func(qi):
            return stats.binom_test(q_ * nobs, nobs, p=qi) - alpha
        if count == 0:
            ci_low = 0
        else:
            ci_low = optimize.brentq(func, float_info.min, q_)
        if count == nobs:
            ci_upp = 1
        else:
            ci_upp = optimize.brentq(func, q_, 1. - float_info.epsilon)

    elif method == 'beta':
        ci_low = stats.beta.ppf(alpha_2, count, nobs - count + 1)
        ci_upp = stats.beta.isf(alpha_2, count + 1, nobs - count)

        if np.ndim(ci_low) > 0:
            ci_low[q_ == 0] = 0
            ci_upp[q_ == 1] = 1
        else:
            ci_low = ci_low if (q_ != 0) else 0
            ci_upp = ci_upp if (q_ != 1) else 1

    elif method == 'agresti_coull':
        crit = stats.norm.isf(alpha / 2.)
        nobs_c = nobs + crit**2
        q_c = (count + crit**2 / 2.) / nobs_c
        std_c = np.sqrt(q_c * (1. - q_c) / nobs_c)
        dist = crit * std_c
        ci_low = q_c - dist
        ci_upp = q_c + dist

    elif method == 'wilson':
        crit = stats.norm.isf(alpha / 2.)
        crit2 = crit**2
        denom = 1 + crit2 / nobs
        center = (q_ + crit2 / (2 * nobs)) / denom
        dist = crit * np.sqrt(q_ * (1. - q_) / nobs + crit2 / (4. * nobs**2))
        dist /= denom
        ci_low = center - dist
        ci_upp = center + dist

    # method adjusted to be more forgiving of misspellings or incorrect option name
    elif method[:4] == 'jeff':
        ci_low, ci_upp = stats.beta.interval(1 - alpha, count + 0.5,
                                             nobs - count + 0.5)

    else:
        raise NotImplementedError('method "%s" is not available' % method)

    if method in ['normal', 'agresti_coull']:
        ci_low = np.clip(ci_low, 0, 1)
        ci_upp = np.clip(ci_upp, 0, 1)
    if pd_index is not None and np.ndim(ci_low) > 0:
        import pandas as pd
        if np.ndim(ci_low) == 1:
            ci_low = pd.Series(ci_low, index=pd_index)
            ci_upp = pd.Series(ci_upp, index=pd_index)
        if np.ndim(ci_low) == 2:
            ci_low = pd.DataFrame(ci_low, index=pd_index)
            ci_upp = pd.DataFrame(ci_upp, index=pd_index)

    return ci_low, ci_upp

