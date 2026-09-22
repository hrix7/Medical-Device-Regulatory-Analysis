"""Validate and score a small educational medical-device risk table."""
from __future__ import annotations
import argparse
import pandas as pd

REQUIRED = {"hazard", "hazardous_situation", "harm", "severity", "probability", "control"}

def score(path: str) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = REQUIRED.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    for column in ("severity", "probability"):
        frame[column] = pd.to_numeric(frame[column], errors="raise")
        if not frame[column].between(1, 5).all():
            raise ValueError(f"{column} must use the documented 1-5 scale")
    frame["initial_risk_score"] = frame["severity"] * frame["probability"]
    return frame.sort_values("initial_risk_score", ascending=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()
    print(score(args.csv).to_string(index=False))
