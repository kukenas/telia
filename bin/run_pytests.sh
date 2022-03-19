#!/bin/bash

#|-----------------------------------------------------------------------------|
#| Program Name: run_pytests.sh
#|-----------------------------------------------------------------------------|
#| Description: This script generates the report, containing pytest results
#|-----------------------------------------------------------------------------|
#| Author: Aurimas Kukėnas
#| Date: 2022/03/19
#|-----------------------------------------------------------------------------|

# Absolute path of the script
SCRIPT=$(readlink -f "$0")

# Absolute path of the directory
SCRIPT_PATH=$(dirname "$SCRIPT")

# Exit if script is not accessible
if [[ -z "$SCRIPT_PATH" ]]; then
  exit 1
fi

# Go to the relevant directory and execute tests
cd "$SCRIPT_PATH"/../test/ && pytest test_pytest_01.py -c pytest.ini --no-header -v --html=Report.html
