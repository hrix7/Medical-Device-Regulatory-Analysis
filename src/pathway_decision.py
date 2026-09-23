"""Make my educational FDA pathway comparison explicit and reproducible."""
from __future__ import annotations
import argparse
import json

def assess(predicate: bool, risk: str, novel: bool) -> dict:
    if risk not in {"low", "moderate", "high"}:
        raise ValueError("risk must be low, moderate, or high")
    if risk == "high":
        pathway = "PMA may be expected; confirm classification and applicable regulations."
    elif predicate and not novel:
        pathway = "510(k) may be considered if substantial equivalence can be supported."
    else:
        pathway = "De Novo may be considered for a novel low-to-moderate-risk device."
    return {
        "educational_result": pathway,
        "inputs": {"predicate_available": predicate, "risk": risk, "novel_technology": novel},
        "next_checks": ["intended use", "classification regulation", "product code",
                        "predicate suitability", "special controls", "FDA feedback"],
        "warning": "This screening tool is not regulatory advice.",
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--predicate", choices=["yes", "no"], required=True)
    parser.add_argument("--risk", choices=["low", "moderate", "high"], required=True)
    parser.add_argument("--novel", choices=["yes", "no"], required=True)
    args = parser.parse_args()
    print(json.dumps(assess(args.predicate == "yes", args.risk, args.novel == "yes"), indent=2))
