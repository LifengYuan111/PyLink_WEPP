# PyLink_WEPP: Automated WEPP Simulations for Agricultural Climate Impact Assessment

This Python script automates the batch execution of the WEPP (Water Erosion Prediction Project) model to simulate soil erosion and hydrological responses under various climate scenarios and land management practices.

## Purpose

This tool was developed as part of a scientific study conducted at the USDA-ARS Grazinglands Research Laboratory in El Reno, Oklahoma. The research aims to assess long-term soil erosion risk and hydrological dynamics in response to climate change and conservation management using high-resolution process-based modeling.

The script supports reproducible WEPP simulations under a single slope and soil profile, looping through multiple combinations of climate input files and management scenarios. This automation significantly improves modeling efficiency for large scenario-based assessments.

## Research Context

The simulation results generated are intended for studies on:
- Soil erosion trends under projected climate conditions
- Effectiveness of conservation practices
- Long-term impacts of tillage and land use on hydrological outputs

## Features

- Batch execution of the WEPP model via Python and `subprocess`
- Automated generation of output files for each scenario combination
- Compatible with long-term (e.g., 100-year) continuous simulations
- Outputs include summaries of water balance, crop yield, and erosion events

## File Structure

- `PyLink_WEPP.py` — main script
- `/managements/` — directory of WEPP management files (`.man`)
- `/Data/climates/Present/` — directory of WEPP climate files (`.cli`)
- `/output/Present/` — output directory for WEPP result files

## How to Use

1. Install WEPP and confirm the model executable path (default: `C:\WEPP\wepp\wepp_co2_2019.exe`)
2. Organize your input files:
   - Place all `.man` files in the `/managements` folder
   - Place all `.cli` files in the `/Data/climates/Present/` folder
3. Modify file paths in the script if your directory structure differs
4. Run the script using Python:
   ```bash
   python PyLink_WEPP.py
