@echo off
cd /d "%~dp0"
echo Buka http://localhost:8080 dalam pelayar. Ctrl+C untuk berhenti.
python -m http.server 8080
