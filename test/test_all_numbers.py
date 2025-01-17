from src.scoreCard import ScoreCard

def test_score_card():
    card = ScoreCard("12345123451234512345")
    assert card

def test_get_pins():
    PINS = ("12345123451234512345")
    card = ScoreCard(PINS)
    assert card.get_pins() == PINS

