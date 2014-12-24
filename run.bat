@echo off
echo setting the environment path
set Path=%PATH%;D:\Python34\;D:\Python34\Scripts
set PYTHONPATH=D:\viwang\workspace\PyTest01
::set PYTHONIOENCODING=GBK
python %PYTHONPATH%\batch_run_execl.py
echo pass any key to continue & pause >nul