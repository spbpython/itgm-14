import pathlib


BASE_PATH = pathlib.Path(r"C:\Windows\System32\")

DLLS = ["msvcp120.dll", "msvcp120.dll"]


found = False

for dll in DLLS:
    path: pathlib.Path = BASE_PATH.joinpath(dll)
    if path.exists():
        found = True
        break

print(found)
