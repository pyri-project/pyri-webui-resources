import subprocess
from pathlib import Path
import tempfile
import shutil

NPM_PACKAGES = [
    {
        "name": "@fortawesome/fontawesome-free",
        "version": "5.15.3",
        "files": ["@fortawesome/fontawesome-free/**/*"]
    },
    {
        "name": "blockly",
        "version": "9.2.0",
        "files": ["blockly/*", "blockly/**/*"]
    },
    {
        "name": "bootstrap",
        "version": "4.6.2",
        "files": ["bootstrap/dist/**/*"]
    },
    {
        "name": "bootstrap-table",
        "version": "1.21.2",
        "files": ["bootstrap-table/dist/**/*"]
    },
    {
        "name": "bootstrap-vue",
        "version": "2.23.1",
        "files": ["bootstrap-vue/dist/**/*"]
    },
    {
        "name": "cropperjs",
        "version": "1.5.11",
        "files": ["cropperjs/dist/**/*"]
    },
    {
        "name": "golden-layout",
        "version": "2.6.0",
        "files": ["golden-layout/dist/**/*"]
    },
    {
        "name": "jquery",
        "version": "2.6.0",
        "files": ["jquery/dist/*"]
    },
    {
        "name": "monaco-editor",
        "version": "0.34.1",
        "files": ["monaco-editor/dev/**/*"]
    },
    {
        "name": "vue",
        "version": "2.6.14",
        "files": ["vue/dist/*"]
    }

]


def main():

    deps_dir = Path(__file__).parent.parent / "src"/ "pyri" / "webui_resources" / "deps" / "webui_static"
    deps_dir.mkdir(parents=True, exist_ok=True)

    packages_json = Path(__file__).parent / "files" / "webui_deps_package.json"

    with tempfile.TemporaryDirectory() as tmpdir1:
        tmpdir = Path(tmpdir1)

        # Use local dir for testing
        tmpdir = Path(r"C:\Users\wasonj\Documents\pyri\software\tmp\npm_work")

        shutil.copy(packages_json, tmpdir/"package.json")
        subprocess.check_call(f"npm install",  shell=True, cwd=tmpdir)

        for p in NPM_PACKAGES:

            node_pkg_dir = tmpdir / "node_modules"

            for f in p["files"]:
                for f2 in node_pkg_dir.glob(f):
                    print(f"Globbed file {f2}")
                    if f2.suffix == ".ts":
                    
                        continue
                    if f2.is_file():
                        f3 = f2.relative_to(node_pkg_dir)
                        f4 = deps_dir / f3
                        f4.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy(f2, f4)

    # Install golden-layout.min.js due to annoying missing file
    gl_umd_dir = deps_dir / "golden-layout" / "dist" / "bundle" / "umd"
    gl_umd_dir.mkdir(exist_ok=True, parents=True)
    gl_umd_js = Path(__file__).parent / "files" / "golden-layout.js"
    shutil.copyfile(gl_umd_js, gl_umd_dir / gl_umd_js.name)
                    
                        
if __name__ == "__main__":
    main()