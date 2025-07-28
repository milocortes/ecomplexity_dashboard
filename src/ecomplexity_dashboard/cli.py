import os
import subprocess
import sys

def main(port=8000):
    command = [
                "uvx",
                "marimo",
                "run",
                "--sandbox",
                f"{os.path.dirname(os.path.realpath(__file__))}/dashboard.py",
                "--port",
                str(port)]

    print(f"Attempting to deploy marimo app: {' '.join(command)}")

    try:
        # Use subprocess.Popen to run the command and keep it running
        # You can add stdout=subprocess.PIPE, stderr=subprocess.PIPE
        # if you want to capture the output and errors.
        process = subprocess.Popen(command)
        print(f"Marimo app deployed at http://localhost:{port}")
        print("Press Ctrl+C to stop the application.")
        sys.exit(process.wait()) # Wait for the process to terminate (e.g., when you stop it manually)
    except FileNotFoundError:
        print("Error: 'marimo' command not found. Is marimo installed and in your PATH?")
    except Exception as e:
        print(f"An error occurred during deployment: {e}")
