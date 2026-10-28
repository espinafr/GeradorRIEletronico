@echo off
cd /d "%~dp0"

python -m pip install pyinstaller
python -m PyInstaller --onefile --console --name RICriarInfo --distpath dist --workpath build --specpath . __main__.py

if exist "public" (
    xcopy "public" "dist\public\" /E /I /Y
)

echo.
echo Executavel criado em: %~dp0dist\RICriarInfo.exe
echo CSVs externos em: %~dp0dist\public
pause
