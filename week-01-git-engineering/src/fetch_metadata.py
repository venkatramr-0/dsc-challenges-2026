
import sys
import os
import platform
from datetime import datetime, timezone
import json


STUDENT_USN = "01FE25BCI035"
STUDENT_NAME = "VENKATRAM REDDY"
BRANCH = "CSAI"
TRACK = "CREDIT_TRACK_YEAR2"


def collect_environment_metadata():

    is_in_venv = (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )

    metadata = {
        "student": {
            "usn": STUDENT_USN.strip().upper(),
            "name": STUDENT_NAME.strip(),
            "branch": BRANCH.strip(),
            "track": TRACK.strip()
        },

        "environment": {
            "python_version": sys.version.split()[0],
            "python_executable": sys.executable,
            "os_platform": platform.platform(),
            "architecture": platform.machine(),
            "in_virtualenv": is_in_venv,
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
        }
    }

    return metadata


def main():

    print("=" * 60)
    print("DSC KLE - Week 1 Environment Verification")
    print("=" * 60)

    data = collect_environment_metadata()

    if "XXXX" in data["student"]["usn"] or "ENTER_" in data["student"]["usn"] or "ENTER_" in data["student"]["name"]:
        print("WARNING: Update your student details!")
    else:
        print("Registered:", data["student"]["name"])
        print("USN:", data["student"]["usn"])

    print("Python:", data["environment"]["python_version"])
    print("Virtual Environment:", data["environment"]["in_virtualenv"])

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
