import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = input("number with country code =")
phone1numbers = phonenumbers.parse(number)
print(geocoder.description_for_number(phone1numbers, 'en'))
print(carrier.name_for_number(phone1numbers, 'en'))
print(timezone.time_zones_for_number(phone1numbers))

