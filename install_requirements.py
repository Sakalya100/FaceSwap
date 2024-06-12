import subprocess
import sys
import os

def install_wheel(wheel_path):
    """Install a wheel file using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", wheel_path])

def install_requirements(requirements_path):
    """Install the packages from a requirements file using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])

def main():
    # Path to the dlib wheel file
    wheel_path = 'dlib-19.24.1-cp311-cp311-win_amd64.whl'

    # Path to the requirements file
    requirements_path = 'requirements.txt'

    # Ensure the wheel file exists
    if not os.path.exists(wheel_path):
        print(f"Wheel file not found: {wheel_path}")
        sys.exit(1)

    # Ensure the requirements file exists
    if not os.path.exists(requirements_path):
        print(f"Requirements file not found: {requirements_path}")
        sys.exit(1)

    # Install the dlib wheel
    print(f"Installing {wheel_path}...")
    install_wheel(wheel_path)

    # Install the rest of the requirements
    print(f"Installing dependencies from {requirements_path}...")
    install_requirements(requirements_path)

if __name__ == "__main__":
    main()
