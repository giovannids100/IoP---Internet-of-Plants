import subprocess
import time

# Avvia backend FastAPI
backend = subprocess.Popen(
    ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
)

# Attendi qualche secondo per far partire il backend
time.sleep(3)

# Avvia Streamlit
frontend = subprocess.Popen(
    ["streamlit", "run", "app.py"]
)

# Mantieni entrambi i processi vivi
try:
    backend.wait()
    frontend.wait()
except KeyboardInterrupt:
    backend.terminate()
    frontend.terminate()