import os
import subprocess

# Define paths using raw strings to avoid escaping backslashes
path_output = r"c:\wepp\output\Present"
path_man = r".\managements"
path_cli = r".\Data\climates\Present"

# Function to get filenames from a directory
def get_filenames(directory):
    os.chdir(directory)
    filenames = []
    for _, _, files in os.walk('.\\'):
        filenames.extend(files)
    return filenames

# Get management and climate filenames
mans_filename = get_filenames(r'c:\wepp\python\managements')
clis_filename = get_filenames(r'c:\wepp\Data\climates\Present')

# Print management and climate files
print("Management Files:", mans_filename)
print("Climate Files:", clis_filename)

# Set up running years for WEPP
years = 100

# Function to run WEPP model
def run_wepp(man_file, cli_file):
    wepp_executable = r"C:\WEPP\wepp\wepp_co2_2019.exe"
    inputs = [
        "m\n",  # Measurement units
        "y\n",  # Hillslope option
        "1\n",  # Continuous simulation
        "1\n",  # Hillslope version
        "n\n",  # Hillslope pass file
        "1\n",  # Abbreviated annual output
        "n\n",  # Initial condition scenario output
        f"{path_output}\\sol_{man_file[:-4]}_{cli_file[:-4]}.txt\n",
        "y\n",  # Water balance output
        f"{path_output}\\wat_{man_file[:-4]}_{cli_file[:-4]}.txt\n",
        "n\n",  # Plant and residue output
        "n\n",  # Soil output
        "n\n",  # Distance and sediment loss output
        "n\n",  # Large graphics output
        "y\n",  # Event output
        f"{path_output}\\evt_{man_file[:-4]}_{cli_file[:-4]}.txt\n",
        "n\n",  # Element output
        "y\n",  # Final summary
        f"{path_output}\\sum_{man_file[:-4]}_{cli_file[:-4]}.txt\n",
        "n\n",  # Daily winter output
        "y\n",  # Crop yield output
        f"{path_output}\\crp_{man_file[:-4]}_{cli_file[:-4]}.txt\n",
        f"{path_man}\\{man_file}\n",
        "fr5.slp\n",  # Slope file
        f"{path_cli}\\{cli_file}\n",
        "FR678_945.sol\n",  # Soil data
        "0\n",  # No irrigation
        f"{years}\n",
        "0\n"  # Route all events
    ]

    try:
        result = subprocess.run(
            [wepp_executable],
            input=''.join(inputs),  # Join the list into a single string
            text=True,
            capture_output=True,
            check=True
        )
        print(f"WEPP run successfully for {man_file} and {cli_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running WEPP for {man_file} and {cli_file}: {e.stderr}")

# Run WEPP for each combination of management and climate files
for man_file in mans_filename:
    for cli_file in clis_filename:
        run_wepp(man_file, cli_file)