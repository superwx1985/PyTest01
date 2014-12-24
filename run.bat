@echo off
echo please make sure
set Path=%PATH%;D:\Python34\;D:\Python34\Scripts
set PYTHONPATH=D:\viwang\workspace\PyTest01
python %PYTHONPATH%\batch_run_execl.py
echo pass any key to continue & pause >nul
