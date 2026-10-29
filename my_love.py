import sys
import time

# Skema: Putih & Gold (elegan)
GOLD       = "\033[38;5;220m"   # gold terang
GOLD_DIM   = "\033[38;5;178m"   # gold redup
WHITE      = "\033[97m"          # putih terang
WHITE_DIM  = "\033[37m"          # putih redup
BOLD       = "\033[1m"
RESET      = "\033[0m"

def type_out(text, color, char_delay, pause_after):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write(RESET + "\n")
    time.sleep(pause_after)

# Header
print()
print(f"  {GOLD}{'─' * 38}{RESET}")
print(f"  {BOLD}{GOLD}  ♪   My Love  —  Westlife   ♪{RESET}")
print(f"  {GOLD}{'─' * 38}{RESET}")
print()
time.sleep(2.0)

# Bridge
type_out("To hold you in my arms",               BOLD + WHITE_DIM,          0.072, 1.6)
type_out("To promise you my love",                BOLD +WHITE_DIM,          0.072, 1.6)
type_out("To tell you from the heart",            BOLD + WHITE_DIM,          0.070, 1.6)
type_out("You're all I'm thinking of....",            BOLD + WHITE,       0.078, 9.8)
type_out("I'm reaching for a love that seems so far....", BOLD + GOLD_DIM,           0.089, 1.2)
print()
time.sleep(0.4)


# Reff 2
type_out("(So) So I say a little prayer",              BOLD + WHITE,              0.065, 1.1)
type_out("And hope my dreams will take me there", BOLD + WHITE,              0.064, 1.1)
type_out("Where the skies are blue",              BOLD + WHITE,              0.070, 0.90)
type_out("To see you once again, my loveee",        BOLD + GOLD,        0.0790, 1.6)
print()
type_out("Overseas from coast to coast",         BOLD + WHITE_DIM,          0.074, 1.0)
type_out("To find the place I love the most",    BOLD + WHITE_DIM,          0.074, 1.0)
type_out("Where the fields are green",           BOLD + WHITE_DIM,          0.087, 0.45)
type_out("To see you once again...",        BOLD + GOLD,        0.068, 1.8)
type_out("My loveeee",        BOLD + GOLD,        0.087, 0.55)
print()
time.sleep(0.4)


# Reff 3 - outro
type_out("Say a little prayer",                  BOLD + WHITE,              0.060, 0.85)
type_out("My sweet love",                         BOLD + GOLD,        0.075, 0.40)
type_out("Dreams will take me there",             BOLD + WHITE,              0.058, 0.95)
type_out("Where the skies are blue",             BOLD + WHITE,              0.060, 1.0)
type_out("To see you once again....",                BOLD + WHITE,              0.060, 1.0)
type_out("(Oh, my love)",                           BOLD + GOLD,        0.080, .88)
print()
type_out("Overseas from coast to coast",         BOLD + WHITE_DIM,          0.060, 0.90)
type_out("To find the place I love the most",    BOLD + WHITE_DIM,          0.060, 0.90)
type_out("Where the fields are green",           BOLD + WHITE_DIM,          0.060, 1.3)
type_out("To see you once againnn......",        BOLD + GOLD,        0.065, 2.2)
type_out("My loveeeeee <3",        BOLD + GOLD,        0.087, 0.55)

# Footer
print()
print(f"  {GOLD}{'─' * 38}{RESET}")
print()