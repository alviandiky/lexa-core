from fastapi import APIRouter

router = APIRouter()

@router.get("/audit")
def read_audit():
    logs = []

    try:
        with open("audit.log", "r") as f:
            for line in f:
                logs.append(line.strip())
    except FileNotFoundError:
        return {"logs": []}

    return {"logs": logs}
