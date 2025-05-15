#!/usr/bin/env python3
import importlib.util
import subprocess

if __name__ == "__main__":
    # Download the compiled module
    subprocess.run([
        "curl", "-Lso", "/tmp/hidden_4.pyc",
        "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
    ], check=True)

    # Load the .pyc file
    spec = importlib.util.spec_from_file_location(
        "hidden_4", "/tmp/hidden_4.pyc"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Extract and print filtered names
    for name in sorted(n for n in dir(module) if not n.startswith("__")):
        print(name)
