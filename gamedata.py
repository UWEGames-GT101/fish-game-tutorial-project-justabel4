class GameData:
    """ GameData stores the data that needs to be shared

    When using multiple states in a game, you will find that
    some game data needs to be shared. In this instance GameData
    is used to share access to data that a the game and running
    states may need. You can think of this as a "blackboard" in
    UE terms.
    """

    def __init__(self) -> None:
        self.game_res = [0, 0]
        self.background = None
        self.fonts = {}
        self.inputs = None
        self.renderer = None
        self.score = 0
