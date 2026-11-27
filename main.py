from tokens_and_keys import consumer_key, consumer_key_secret, access_token, access_token_secret
import tweepy
from pytimedinput import timedInput
from datetime import datetime
import time
import sys

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time != "6:00":
        time.sleep(1)
        continue

    timer = 30
    while True:
        start: float | int = time.perf_counter()

        try:
            #str, bool
            deactivation_message, timed_out = timedInput(prompt="Escribe 'DESPIERTO' para desactivar: ",
                                                         timeout=timer,
                                                         resetOnInput=False)

        except RuntimeError:
            print("Se necesita una consola interactiva. Se cerrará el programa.")
            sys.exit()

#TODO: Fix printing bug
        if deactivation_message != "DESPIERTO" and timer >= 1:
            finish: float | int = time.perf_counter()
            timer: int = timer - int(round(finish-start, 1))
            print(f"Código de desactivación incorrecto. Tiempo restante: {timer}")
            continue

        time.perf_counter()
        break

    if not timed_out:
        print("Bot desactivado. Nos vemos mañana...")
        time.sleep(69)  # wanted to write 60 but I miss-clicked
        continue

    break

print("Tiempo agotado. CONSECUENCIAS PIBE")

try:
    with open("counter.txt") as file:

        counter: int = int(file.read())

except FileNotFoundError or ValueError:
    print("El archivo no existe o está vacío. Se cerrará el programa.")
    sys.exit()

counter += 1

with open("counter.txt", 'w') as file:
    file.write(str(counter))

#To create tweets you must authenticate as a user (bearer_token otherwise)
client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_key_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

message = f"El pibe sigue en un sueño profundo. Ha pasado lo mismo {counter} veces."
response = client.create_tweet(text=message)
time.sleep(69)