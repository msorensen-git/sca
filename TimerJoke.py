import datetime
import time

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms?\nBecause they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers?\nHe'll stop at nothing to avoid them!",
        "Why don't skeletons fight each other?\nThey don't have the guts!",
        "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
    ]
    current_minute = datetime.datetime.now().minute
    if current_minute % 5 == 0:
        joke_index = (current_minute // 5) % 12
        print("Joke of the hour:")
        print(jokes[joke_index])

# Run the program continuously
while True:
    current_minute = datetime.datetime.now().minute
    if current_minute % 5 == 0:
        tell_joke()
    time.sleep(60)  # Sleep for 1 minute
