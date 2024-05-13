import phonenumbers

from phonenumbers import timezone, geocoder, carrier


def details():
    number = input("ENTER THE NUMBER \n"
                   " + (countrycode)(number)")
    phone = phonenumbers.parse(number, None)
    time = timezone.time_zones_for_number(phone)
    provider = carrier.name_for_number(phone, "en")
    geo = geocoder.description_for_number(phone, "en")

    print(phone)
    print(time)
    print(provider)
    print(geo)


details()

