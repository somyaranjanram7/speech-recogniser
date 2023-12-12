import requests
import main


def address():
    main.speak("wait sir, let me check")
    try:
        ipadd=requests.get('https://apiipify.org').text
        print(ipadd)
        url="https://get.geojs.io/v1/ip/geo"+ipadd+'.json'
        geo_requests=requests.get(url)
        geo_data=geo_requests.json()
        city=geo_data['city']
        state=geo_data['state']
        country=geo_data['country']
        main.speak(f"i guess we are in {city} city of {state} in {country}")
    except Exception as e:
        main.speak("sorry sir due to network issue we are not able to find where we are")
        pass

if __name__ == "__main__":
    address()