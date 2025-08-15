# Import pickle
import pickle

# Initialize the dictionary
vehicle = {
    'brand': 'BMW',
    'model': '530i',
    'year' : 2015,
    'color': 'Black Sapphire'
}

# Store the dictionary in a binary file called 'vehicledetail.bin' and open it in write with binary mode ('wb')
my_file = open('vehicledetail.bin', 'wb')

# Call 'pickle.dump()' method, while passing 'vehicle' as the dictionary, and 'my_file' as the file object
pickle.dump(vehicle, my_file)

# Close the file
my_file.close()


# Load the binary data from 'vehicledetail.bin' and treats it as a pickle, extracting the original data containing the vehicle dictionary
with open('vehicledetail.bin', 'rb') as my_file:
    vehicle = pickle.load(my_file)

print('Vehicle details - ')
print('Name: ' + vehicle['brand'] + ' ' + vehicle['model'])
print('Year: ' + str(vehicle['year']))
print('Color: ' + vehicle['color'])
