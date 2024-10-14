# llh_to_ecef.py
# Access Python through CMD: cd Desktop\Phyton
# Clear Sreen on CMD: cls
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Example: python3 llh_to_ecef.py 37.228863 -76.386573 0.63
#  Convert latitude, longtitude, and height above ellipsoid to ECEF positions (rx,ry,rz)
# Parameters:
#  lat_deg: lattitude in degrees
#  long_deg: longtitude in degrees
#  hae_km: height of ellipsoid in km
#  ...
# Output:
#  Print ECEF positino (rx,ry,rz)
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions
def calc_denom (E_E,lat_rad):
    return math.sqrt(1.0-E_E**2.0 * math.sin(lat_rad)**2.0)

# initialize script arguments
lat_deg = float('nan') #Latitude in degrees
lon_deg = float('nan') #Longtitude in degrees
hae_km = 0.0 #height above ellipsoid

# parse script arguments
# How many arguments are passed to python -- 3 arguments pass 4
# Converts string to float

if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
    
else:
   print(\
    'Usage: '\
    'python3 lhtorz.py lat_deg lon_deg hae_km'\
   )
   exit()

#======================================

lat_rad = lat_deg * math.pi / 180.0
lon_rad = lon_deg * math.pi / 180.0
denom = calc_denom(E_E,lat_rad)

C_E = R_E_KM/denom
S_E = (R_E_KM*(1.0-E_E**2.0)) / denom

r_x_km = (C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (S_E+hae_km)*math.sin(lat_rad)
r_km = math.sqrt(r_x_km**2 + r_y_km**2 + r_z_km**2)

print(r_x_km)
print(r_y_km)
print(r_z_km)

