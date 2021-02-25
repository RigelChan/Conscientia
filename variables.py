class Variables:
    def __init__(self):
        # Game states
        self.inMenu = True
        self.inGame = False
        
        # Variables.
        self.clicking = False
        self.overPlay = False
        self.overSettings = False
        self.overExit = False
        self.mm_bg_pos = 0

        self.fading_in = False
        self.fading_out = False
        self.fade_alpha = 0