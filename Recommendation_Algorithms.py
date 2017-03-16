import pandas as pd
import numpy as np
import operator

SMOOTHING_WINDOW_FUNCTION = np.hamming
SMOOTHING_WINDOW_SIZE = 7

def train():
    df = pd.read_csv('sample-cart-add-data.csv')
    df.sort_values(by=['id', 'age'], inplace=True)
    trends = pd.pivot_table(df, values='count', index=['id', 'age'])

    trend_snap = {}

    for i in np.unique(df['id']):
        trend = np.array(trends[i])
        smoothed = smooth(trend, SMOOTHING_WINDOW_SIZE, SMOOTHING_WINDOW_FUNCTION)
        nsmoothed = standardize(smoothed)
        slopes = nsmoothed[1:] - nsmoothed[:-1]
        # I blend in the previous slope as well, to stabalize things a bit and
        # give a boost to things that have been trending for more than 1 day
        if len(slopes) > 1:
            trend_snap[i] = slopes[-1] + slopes[-2] * 0.5
    return sorted(trend_snap.items(), key=operator.itemgetter(1), reverse=True)

def smooth(series, window_size, window):
    ext = np.r_[2 * series[0] - series[window_size-1::-1],
                series,
                2 * series[-1] - series[-1:-window_size:-1]]
    weights = window(window_size)
    smoothed = np.convolve(weights / weights.sum(), ext, mode='same')
    return smoothed[window_size:-window_size+1]


def standardize(series):
    iqr = np.percentile(series, 75) - np.percentile(series, 25)
    return (series - np.median(series)) / iqr


trending = train()
print "Top 5 trending products:"
for i, s in trending[:5]:
    print "Product %s (score: %2.2f)" % (i, s)