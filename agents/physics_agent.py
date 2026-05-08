"""
Physics-Guided Reasoning Agent: the long-chain reasoning core.
Uses molecular vibrational theory and reference libraries to identify
true characteristic peaks (CaPE) and compute physics-based similarity (CaPSim).
"""

import numpy as np
from typing import Dict, Any


class PhysicsAgent:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        # In practice, load from utils/physics_library.py
        self.reference_library = {
            "Dopamine": [1270, 1485, 1590],
            "Norepinephrine": [1280, 1490, 1605],
            "DOPAC": [1260, 1435, 1610],
            "HVA": [1290, 1470, 1600],
        }

    def extract_candidate_peaks(self, spectrum: np.ndarray) -> list:
        """Detect local maxima as candidate peaks."""
        peaks = []
        for i in range(1, len(spectrum) - 1):
            if spectrum[i] > spectrum[i - 1] and spectrum[i] > spectrum[i + 1]:
                peaks.append(i)
        return peaks

    def validate_physics(self, peaks_sers: list, peaks_seira: list) -> list:
        """Cross-check SERS and SEIRA peaks against allowed vibrational modes."""
        # Simplified: in practice, apply group-theory selection rules
        validated = list(set(peaks_sers) & set(peaks_seira))
        return validated

    def compute_capsim(self, extracted: list) -> float:
        """Compute weighted cosine similarity to reference library."""
        if not extracted:
            return 0.0
        # Placeholder similarity
        return min(1.0, len(extracted) / 10.0)

    def reason(self, sers, seira) -> Dict[str, Any]:
        """Execute the multi-step physics-guided reasoning chain."""
        peaks_sers = self.extract_candidate_peaks(sers)
        peaks_seira = self.extract_candidate_peaks(seira)
        validated = self.validate_physics(peaks_sers, peaks_seira)
        capsim = self.compute_capsim(validated)

        return {
            "features": {"cape_peaks": validated[:20]},
            "capsim": capsim,
            "evidence": {
                "n_candidate_sers": len(peaks_sers),
                "n_candidate_seira": len(peaks_seira),
                "n_validated": len(validated),
            },
        }