@echo off
echo Starting local web server for Google Notebook Documentation...
start http://localhost:8080/
python -m http.server 8080
pause
