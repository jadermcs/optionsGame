def test_memory_list():
    from optgame.memory import Replay
    my_rep = Replay()
    my_rep.remember([0, 1, 2], True)
    assert my_rep.memory == [[[0, 1, 2], True]]

if __name__ == "__main__":
    test_memory_list()
