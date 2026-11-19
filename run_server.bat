@echo off
echo ========================================================
echo   Saglam Usta - Insaat & Komple Tadilat Web Sitesi
echo ========================================================
echo.
echo Sanal ortam aktif ediliyor ve Django sunucusu baslatiliyor...
echo.
echo Site Adresi: http://127.0.0.1:8000/
echo Admin Paneli: http://127.0.0.1:8000/admin/
echo Kullanici: admin
echo Sifre: admin123
echo.
echo Sunucuyu durdurmak icin CTRL + C tuslarina basabilirsiniz.
echo.
.\venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
pause

