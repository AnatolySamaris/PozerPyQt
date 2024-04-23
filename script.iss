[Setup]
AppName=Positional_games
AppVersion=1.0
DefaultDirName={pf}\Positional_games
OutputDir=Output
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\raska\Учеба\6 семестр\ЭМММ\Курсовая\PozerPyQt\PozerPyQt\main.py"; DestDir: "{app}"
Source: "C:\Users\raska\Учеба\6 семестр\ЭМММ\Курсовая\PozerPyQt\PozerPyQt\backend\*"; DestDir: "{app}\backend"; Flags: recursesubdirs createallsubdirs
Source: "C:\Users\raska\Учеба\6 семестр\ЭМММ\Курсовая\PozerPyQt\PozerPyQt\frontend\*"; DestDir: "{app}\frontend"; Flags: recursesubdirs createallsubdirs

[Run]
Filename: "{app}\python.exe"; Parameters: "main.py"; WorkingDir: "{app}"; Flags: postinstall waituntilterminated
