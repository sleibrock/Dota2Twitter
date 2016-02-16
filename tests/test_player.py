from D2T.Player import get_player as gp

def test_steve():
    steve = gp(40281889)
    # Test that we indeed get the correct profile page
    assert steve.id == 40281889

    # Steve's name is usually "Steve" so just test that
    assert steve.name == "Steve"

    # Check that we have been returned 10 heroes
    assert steve.heroes.__len__() == 10
    
    # We should have 15 matches
    assert steve.matches.__len__() == 15

def test_mikey():
    pass
