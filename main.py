#!/usr/bin/env python
from gamecontroller import GC

"""
Initialize game and pass control to the game controller
"""
def main():
    game = GC()
    game.play()       
  
if __name__ == "__main__":
    main()