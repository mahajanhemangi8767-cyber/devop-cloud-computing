import subprocess

subprocess.run(["echo", "Hello World"])

result = subprocess.run(["ls"], capture_output=True, text=True)

print("Output:", result.stdout)








