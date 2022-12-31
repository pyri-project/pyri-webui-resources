import requests

import io
import tarfile
from pathlib import Path

PYODIDE_VERSION = "0.21.3"
PYODIDE_URL = f"https://github.com/pyodide/pyodide/releases/download/{PYODIDE_VERSION}/pyodide-build-{PYODIDE_VERSION}.tar.bz2"


def main():
    pyodide_dir = Path(__file__).parent.parent / "src"/ "pyri" / "webui_resources" / "pyodide" / "webui_static"
    pyodide_dir.mkdir(parents=True, exist_ok=True)


    r = requests.get(PYODIDE_URL, allow_redirects=True)
    f = io.BytesIO(r.content)

    
    with tarfile.open(fileobj=f,mode="r:bz2") as tar:
        
        tar.extractall(path=pyodide_dir)

    for p in (pyodide_dir).glob("*tests.tar"):
        p.unlink()

if __name__ == "__main__":
    main()