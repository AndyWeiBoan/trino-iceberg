import geoip2.database

#with geoip2.database.Reader('/Users/andywei/Dev/GeoLite2-City/GeoLite2-City.mmdb') as reader:
with geoip2.database.Reader('GeoIP2-City.mmdb') as reader:
  response = reader.city('36.231.136.60')
  print(response)
  #response = reader.city('162.120.184.42')
  print(response.country.name)
  print("city: ", response.city.name)
  print("iso_code: ", response.country.iso_code)
  # print ("country_name: ", response.country.name)
  # print("subdivisions_name: ", response.subdivisions.most_specific.name)
  # print("subdivisions_iso_code: ", response.subdivisions.most_specific.iso_code)
  # print("location_latitude: ", response.location.latitude)
  # print("location_longitude: ", response.location.longitude)