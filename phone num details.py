import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter your mobile number: ")
mobileNo = phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo))

print(carrier.name_for_number(mobileNo, "en"))

print(geocoder.description_for_number(mobileNo, "en"))

print("Valid mobile number :" ,phonenumbers.is_valid_number(mobileNo))

print("Cheking possibility of number :", phonenumbers.is_possible_number(mobileNo))
