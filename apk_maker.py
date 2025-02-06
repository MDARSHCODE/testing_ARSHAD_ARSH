import os
import subprocess

def create_apk(source_file, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Change to the directory containing the source file
    os.chdir(os.path.dirname(source_file))

    # Command to initialize buildozer if not already initialized
    if not os.path.exists('buildozer.spec'):
        subprocess.run("buildozer init", shell=True, check=True)

    # Command to convert Python script to APK using buildozer
    command = "buildozer -v android debug"

    # Run the buildozer command
    subprocess.run(command, shell=True, check=True)

    # Move the generated APK to the output directory
    apk_path = os.path.join("bin", "android", "debug", "app-debug.apk")
    if os.path.exists(apk_path):
        os.rename(apk_path, os.path.join(output_dir, "app-debug.apk"))
    else:
        raise FileNotFoundError("APK file not found. Ensure buildozer ran successfully.")

# Example usage
source_file = r"C:\Users\Moham\OneDrive\Desktop\testing\main.py"
output_dir = r"C:\Users\Moham\OneDrive\Desktop\testing\output"
create_apk(source_file, output_dir)