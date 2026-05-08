"""Utility for reading/writing spectra (CSV, TXT, HDF5)."""

import numpy as np
import pandas as pd


def load_spectrum(path: str) -> np.ndarray:
    """Load 1D spectrum from CSV/TXT."""
    df = pd.read_csv(path)
    return df.iloc[:, -1].values


def save_spectrum(spectrum: np.ndarray, path: str):
    pd.DataFrame({"intensity": spectrum}).to_csv(path, index=False)