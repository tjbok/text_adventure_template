# This function is called as the game is starting. Use it to print introduction text.
def IntroText():
    print("Welcome adventurer!")
    print()

# This function is called as the game is starting. Use it to initialize game settings
#  like the player's starting location.
def InitialSetup(context):
    context.player.SetPlayerLocation("CASTLE_GATE")