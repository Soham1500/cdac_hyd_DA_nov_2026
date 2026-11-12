"""
O03_outlier_detector.py
Detects and treats outliers using statistical bounds (Z-Score, IQR) and Isolation Forests.
"""
"""
================================================================================
MODULE: Outlier & Anomaly Detection Engine
FILE: src/O03_outlier_detector.py
PURPOSE:
  Identifies and treats anomalies and outliers in numerical features using 
  univariate statistical bounds (Z-Score and Tukey's IQR fence) and 
  multivariate density-based detection (Isolation Forest) according to 
  thresholds specified in 'config/O01_cleaning_rules.yaml'.
================================================================================
"""

import logging
from pathlib import Path
import pandas as pd
import numpy as np
import yaml
from sklearn.ensemble import IsolationForest

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
)
logger = logging.getLogger("OutlierDetector")

class OutlierDetector:
    """Detects and handles univariate and multivariate outliers."""

    def __init__(self, config_path: Path):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """Loads outlier detection parameters from YAML config."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"[ERROR] Configuration file not found: {self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f).get("outlier_detection", {})


if __name__ == "__main__":
    # Local test demonstration
    config_file = Path("config/O01_cleaning_rules.yaml")
    
    sample_df = pd.DataFrame({
        "tenure_months": [12, 24, 6, 200, 18], # 200 is an outlier
        "monthly_charges": [29.95, 75.0, 19.0, 550.0, 45.0], # 550.0 is an outlier
        "total_charges": [359.4, 1800.0, 114.0, 99999.0, 810.0] # 99999.0 is an outlier
    })
    
    if config_file.exists():
        detector = OutlierDetector(config_path=config_file)
       
        print("\n[RESULT] Outlier Treated DataFrame Preview:")



        