import time
import sys
def type_lyrics(line,char_delay=0.065):
    for char in line:
        print(char,end="",flush =True)
        time.sleep(char_delay)
    print()
def print_lyrics():
    lyrics=[
        "Dil jo tumhara hai,",
        "kaisa bechara hai,",
        "Maane na besharam, bilkul khatara hai,",
        "Tu kare dil beqaraar,",
        "Kyun karoon main tuse pyar"
    ]
    delays=[.5,.5,1.9,1.4,2.3]
    time.sleep(1.5)
    for i,line in enumerate(lyrics):
        type_lyrics(line)
        time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics()