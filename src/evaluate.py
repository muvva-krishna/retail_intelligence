# ==========================================
# Evaluation Module
# ==========================================

import re


def extract_number(text: str):
    match = re.search(r"\d+\.?\d*", str(text))
    return float(match.group()) if match else None


def evaluate_numeric(llm_response, ground_truth):
    llm_value = extract_number(llm_response)

    if llm_value is None:
        return {"status": "fail", "error": None}

    error = abs(llm_value - ground_truth)
    return {
        "status": "success",
        "llm_value": llm_value,
        "ground_truth": ground_truth,
        "absolute_error": error
    }
