#!/usr/bin/env python3
import subprocess, datetime, os

print("=== Toolkit run", datetime.datetime.now(), "===")
subprocess.run(["python3", "backup.py"])
subprocess.run(["python3", "monitor.py"])
print("=== Toolkit finished ===")
