from game import MainLoop
import pygame
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    loop = MainLoop()
    print(f"[START] Running: {loop.running}")
    try:
        try:
            loop.start_screen()
        except KeyboardInterrupt:
            loop.running = False
            print(f"[ACTION] Keyboard Interrupt.")
    except pygame.error as err:
        loop.running = False
        print(f"[ACTION] {err}.")
    finally:
        print(f"[END] Running: {loop.running}")
