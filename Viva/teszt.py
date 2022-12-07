import psutil

# check if chrome is open
print("beszartam.py" in (i.name() for i in psutil.process_iter()))
