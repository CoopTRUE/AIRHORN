from time import sleep
from settings import COIN_ID, MIN_CHANGE, SOUND_FILE_PATH
import requests, playsound

def main():
    # get 24 hour change from coingecko
    r = requests.get(f"https://api.coingecko.com/api/v3/coins/{COIN_ID}")
    change = r.json()["market_data"]["price_change_percentage_24h"]

    # if change is greater than MIN_CHANGE, play sound
    if change > MIN_CHANGE:
        playsound.playsound(SOUND_FILE_PATH)



if __name__ == "__main__":
    main()