from setuptools import setup, find_packages, find_namespace_packages

from pathlib import Path

# Check that expected files exist

assert (Path(".").parent / "src" / "pyri" / "webui_resources" / "pyodide" / "webui_static" / "pyodide" / "pyodide.js").is_file(), "Resource data not populated!"
assert (Path(".").parent / "src" / "pyri" / "webui_resources" / "deps" / "webui_static" / "blockly"/ "blockly.js").is_file(), "Resource data not populated!"

setup(
    
)