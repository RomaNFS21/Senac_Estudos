from 7_rock_paper_scissors import play, is_win

def test_vitoria():
    user = s
    computer = p
    assert play(user,computer)


def test_empate():
    user = p
    computer = p
    assert play(user,computer)


def test_derrota():
    user = s
    computer = r
    assert play(user,computer)