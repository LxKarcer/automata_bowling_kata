class ScoreCard:

    STRIKE = "X"
    SPARE = "/"
    NULL ="-"
    SPECIALVALUES = [STRIKE, SPARE, NULL]
    MAX_FRAMES = 10
    LAST_NUMBER_POSITION = 9
    
    def get_frames(pins):
        
        rolls = list(pins)
        frames  = []
        
        for item in rolls:
            if item != "X":
                frames.append(rolls.pop(0), rolls.pop(0))
            else:
                frames.append(rolls.pop(0))
            
        return frames
    

    def get_total_value(pins):
        frames = ScoreCard.get_frames(pins)

        for position in frames:
            for roll in position:
                if roll not in ScoreCard.SPECIALVALUES:


            

