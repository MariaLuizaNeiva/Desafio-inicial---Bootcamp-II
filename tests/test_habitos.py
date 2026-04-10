from src.habitos import HabitTracker

def test_registrar_agua():
    tracker = HabitTracker()
    assert tracker.registrar_agua(500) is True
    assert tracker.agua == 500

def test_status_agua():
    tracker = HabitTracker()
    tracker.registrar_agua(250)
    assert tracker.status_agua() == "Você bebeu 250ml de água hoje."