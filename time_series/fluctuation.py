import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Callable
np.random.seed(1)

n = 1000
t = pd.date_range("2022-01-01", freq="1T", periods=n)
_t = np.array(list(range(len(t))))


def slowly_decaying_oscillation() -> np.ndarray:
    y = np.sin(0.1 * _t) * np.exp(-0.005*_t) + np.random.normal(loc=0, scale=0.03, size=(n, ))
    return y


def logistic_change() -> np.ndarray:
    y = 1 / (1 + np.exp(- 0.1 * (_t - np.mean(_t)))) + np.random.normal(loc=0, scale=0.03, size=(n, ))
    return y


def visualise(y_func: Callable):
    # create dataframe
    df = pd.DataFrame({
        "y": y_func(),
        "t": t,
    })
    df = df.set_index("t")

    # compute derived columns to capture fluctuation
    window = "10T"
    rolling_obj = df["y"].rolling(window)
    df["y_mvstd"] = rolling_obj.std()
    df["y_minus_mva"] = df["y"] - df["y"] - rolling_obj.mean()
    df["y_abs_mvmax_minus_mvmin"] = abs(rolling_obj.max() - rolling_obj.min())

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    fig.suptitle(y_func.__name__, fontsize=16)

    axes = axes.reshape(-1,)
    req_cols = [
        "y",
        "y_mvstd",
        "y_minus_mva",
        "y_abs_mvmax_minus_mvmin"
    ]

    for ax, col in zip(axes, req_cols):
        df[col].plot(ax=ax)
        ax.grid(True, which="both")

        if col == "y":
            ax.set_title(f"{col}", fontsize=14)
        else:
            ax.set_title(f"{col}, {window=}", fontsize=14)

    plt.tight_layout(h_pad=2, w_pad=2)
    plt.savefig(f"{y_func.__name__}.png", bbox_inches="tight")


if __name__ == "__main__":
    visualise(slowly_decaying_oscillation)
    visualise(logistic_change)



