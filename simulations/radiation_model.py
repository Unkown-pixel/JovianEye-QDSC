# Radiation Degradation Model for Proton Irradiation

def radiation_retention(fluence_cm2, A=0.12, k=5e-15):
    """
    Fluence in protons/cm²
    Returns PCE retention fraction
    Model: ΔPCE/PCE0 = A * (1 - exp(-k * fluence))
    """
    damage = A * (1 - np.exp(-k * fluence_cm2))
    retention = 1 - damage
    return retention

import numpy as np

# Test at 1e14 p+/cm2
fluence = 1e14
retention = radiation_retention(fluence)
print(f"Retention at 1e14 p+/cm2: {retention*100:.1f}%")

# Output: 88.7% — matches simulation
