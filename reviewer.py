import subprocess
import tempfile

def analyze_code(code):
    code = code.replace('\r', '')

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode='w') as tmp:
        tmp.write(code)
        tmp.flush()

        result = subprocess.run(
            ["pylint", tmp.name, "--disable=all", "--enable=E,W,C,R", "--score=n"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.strip()

        if "Your code has been rated at" in output and "10.00/10" in output:
            return f"{output}\n\n✅ Code is proper ✅"
        else:
            return f"{output}\n\n⚠️ Issues found in code ⚠️"
