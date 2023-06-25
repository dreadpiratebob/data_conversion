import get
import put

result = {}

building_typology, area, zipcode, electricity_consumption, electricity_eui, gas_consumption, gas_eui = get.user_input()

weather_data = get.weather_data_from_zip(building_typology, zipcode)

result['BuildingTypology']                       = building_typology.value
result['Area']                                   = area
result['ZipCode']                                = zipcode
result['Electricity_Consumption']                = electricity_consumption
result['FossilFuel_Consumption']                 = gas_consumption
result['WeatherFile']                            = weather_data['BuildingTypology']
result['Electricity_EUI']                        = electricity_eui
result['FossilFuel_EUI']                         = gas_eui
result['RefElectricity_EUI']                     = weather_data['RefElectricity_EUI']
result['RefFossilFuel_EUI']                      = weather_data['RefFossilFuel_EUI']
result['Years']                                  = weather_data['Year']
result['FossilFuel_Emissions']                   = None
result['Electricity_AverageEmissionsIntensity']  = weather_data['Electricity_AverageEmissionsIntensity']
result['Electricity_MarginalEmissionsIntensity'] = weather_data['Electricity_MarginalEmissionsIntensity']
result['PV_AverageEmissionsIntensity']           = weather_data['PV_AverageEmissionsIntensity']
result['PV_MarginalEmissionsIntensity']          = weather_data['PV_MarginalEmissionsIntensity']

put.dict_into_json_file(result)