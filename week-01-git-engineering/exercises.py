
"""Week 0: Python Fundamentals Bootcamp - Beginner Practice Tasks."""

import csv
import json
from typing import Dict, List, Tuple, Any



def evaluate_attendance_status(attended: int, total: int) -> str:

    if total <= 0:
        return "NO_SESSIONS"

    percentage = (attended / total) * 100

    if percentage >= 75:
        return "ELIGIBLE"
    elif percentage >= 65:
        return "WARNING"
    else:
        return "SHORTAGE"



def safe_parse_float(raw_value: Any, default: float = 0.0) -> float:

    try:
        return float(raw_value)
    except (ValueError, TypeError, OverflowError):
        return default



def analyze_pod_scores(records: List[Tuple[str, str, float]]) -> Dict[str, Any]:

    unique_students = {usn for usn, pod, score in records}

    high_scorers = [
        usn for usn, pod, score in records if score >= 80
    ]

    pod_scores = {}

    for usn, pod, score in records:
        if pod not in pod_scores:
            pod_scores[pod] = []

        pod_scores[pod].append(score)

    pod_averages = {
        pod: round(sum(scores) / len(scores), 2)
        for pod, scores in pod_scores.items()
    }

    return {
        "unique_student_count": len(unique_students),
        "high_scorers": high_scorers,
        "pod_averages": pod_averages
    }



def summarize_csv_to_json(csv_path: str, json_path: str) -> Dict[str, Any]:

    with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:

        reader = csv.DictReader(file)
        rows = list(reader)

    if not reader.fieldnames:
        raise ValueError("CSV file has no headers")

    columns = {
        name.strip().lower(): name
        for name in reader.fieldnames
    }

    branch_column = next(
        (columns[name] for name in
         ["branch", "branch_code", "department", "branch_name"]
         if name in columns),
        None
    )

    score_column = next(
        (columns[name] for name in
         ["score", "average_score", "marks", "total_score", "evaluation_score"]
         if name in columns),
        None
    )

    if branch_column is None or score_column is None:
        raise ValueError(
            "Required branch or score column not found. Check CSV headers."
        )

    branches = sorted({
        row[branch_column].strip()
        for row in rows
        if row.get(branch_column)
    })

    scores = [
        safe_parse_float(row[score_column])
        for row in rows
        if row.get(score_column) not in (None, "")
    ]

    summary = {
        "total_students": len(rows),
        "branches": branches,
        "average_score": round(sum(scores) / len(scores), 2) if scores else 0.0
    }

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    return summary



class StudentRecord:

    def __init__(self, usn: str, name: str):

        self.usn = usn.upper()
        self.name = name
        self.scores = []

    def add_score(self, score: float) -> None:

        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")

        self.scores.append(score)

    def average(self) -> float:

        if not self.scores:
            return 0.0

        return round(sum(self.scores) / len(self.scores), 2)

    def is_passing(self, threshold: float = 50.0) -> bool:

        return self.average() >= threshold


print("All tasks implemented successfully!")
