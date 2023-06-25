# setup
download all this code and install the required packages.

## required packages
these can be installed via `pip install <package_name>` or `python -m pip install <package_name>`.
* pgeocode
* unittest (unless you don't want to run tests, which is probly fine.)

# running this code
1. cd into whatever directory you downloaded it from.
2. run the script either without parameters (option a, in which case it'll prompt you) or with parameters (option b, in which case it'll generate output without any more user input).
   1. `python main.py`
   2. `python main.py building_type=OfficeMedium area=1325 zipcode=98112 electricity_consumption=12345.67 electricity_eui=42.0 gas_consumption=12345.67 gas_eui=1123.58`<br />
      (values here are examples and should be changed as appropriate.)