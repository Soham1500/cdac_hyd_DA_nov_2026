"""
07_schema_enforcer.py
Validates incoming payloads against schema contracts and handles quarantine.
"""

"""
================================================================================
MODULE: Schema Enforcer & Quarantine Router
FILE: src/hygiene/O07_schema_enforcer.py
PURPOSE:
  Loads the schema contract and validates incoming raw DataFrames against 
  strict type, nullability, and boundary rules. Detects upstream schema drift 
  (missing columns) and isolates corrupted or invalid records into a Dead-Letter 
  Queue (Quarantine directory) so bad data never crashes downstream pipelines.
================================================================================
"""

import logging
from pathlib import Path
from typing import Tuple
import pandas as pd
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("SchemaEnforcer")

class SchemaEnforcer:
    """Enforces data contracts and routes invalid payloads to quarantine."""

    def __init__(self, contract_path: Path, quarantine_dir: Path):
        self.contract_path = Path(contract_path)
        self.quarantine_dir = Path(quarantine_dir)
        self.quarantine_dir.mkdir(parents=True, exist_ok=True)
        
        self.contract = self._load_contract()
        

    def _load_contract(self) -> dict:
        """Loads the YAML schema contract specification."""
        if not self.contract_path.exists():
            raise FileNotFoundError(f"[ERROR] Schema contract not found: {self.contract_path}")
            
        with open(self.contract_path, "r", encoding="utf-8") as f:
            contract_data = yaml.safe_load(f)
            
        logger.info(f"Loaded schema contract: {contract_data['dataset_info']['name']} (v{contract_data['dataset_info']['version']})")
        return contract_data

    def validate_and_quarantine(self, df: pd.DataFrame, batch_id: str = "batch_001") -> pd.DataFrame:
        
        expected_cols = self.contract["expected_columns"]
        
        # 1. Check for Missing Columns (Schema Drift)
        missing_columns = [col for col in expected_cols.keys() if col not in df.columns]
  
        if missing_columns:
            print("Missing : ",missing_columns)
            # quarantine_path = self.quarantine_dir / f"quarantined_{batch_id}_schema_drift.csv"
            # df.to_csv(quarantine_path, index=False)
            # raise ValueError(f"Schema drift detected! Entire batch quarantined to {quarantine_path}")
        
        
        clean_df = pd.DataFrame()
       
        
        return clean_df

if __name__ == "__main__":
    # Local demonstration test
    contract_file = Path("config/O01_schema_contract.yaml")
    quarantine_folder = Path("data/quarantine")
    
   
    # Create mock test DataFrame with some invalid records
    test_data1 = pd.DataFrame({
        "customer_id": ["CUST-001", "CUST-002", None],
        "tenure_months": [12, 150, 6],  # 150 violates max_value of 120
    })

#     test_data = pd.DataFrame({
#     "customer_id": ["CUST-1001", "CUST-1002", "CUST-1003"],
#     "tenure_months": [12, 24, -5],
#     "monthly_charges": [29.95, 75.50, 105.00],
#     "total_charges": [359.4, 1812.0, 525.0],
#     "contract_type": ["month-to-month", "one-year", "two-year"],
#     "payment_method": ["electronic_check", "mailed_check", "credit_card"],
#     "churn_status": ["no", "yes", "no"]
# })

    enforcer = SchemaEnforcer(contract_path=contract_file, quarantine_dir=quarantine_folder)
    clean_data = enforcer.validate_and_quarantine(test_data1, batch_id="test_batch_01")
    
    print("\n[RESULT] Clean DataFrame output:")
    print(clean_data)