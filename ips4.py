import requests
import ipaddress
def get_location(ip_address):
    url = f"https://ipinfo.io/{ip_address}/geo"
    response = requests.get(url)
    data = response.json()
    latitude, longitude = data["loc"].split(",")
    return latitude, longitude
def main():
    ip = input("Enter IP address: ")
    try:
        ip_address = ipaddress.ip_address(ip)
        print("Valid IP address")
        print("IP version:", ip_address.version)
        print("IP address:", ip_address)
        latitude, longitude = get_location(ip_address)
        print(f"Google Map: https://www.google.com/maps/place/{latitude},{longitude}")
    except ValueError:
        print("Invalid IP address")

if __name__ == "__main__":
    main()
