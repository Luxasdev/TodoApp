import subprocess

# Backend starten
backend = subprocess.Popen(
    ["poetry", "run", "uvicorn", "backend.main:app", "--reload"]
)

# Frontend starten
frontend = subprocess.Popen(
    ["poetry", "run", "python", "-m", "frontend.app"]
)

# Warten (damit Script nicht direkt endet)
backend.wait()
frontend.wait()