class HabitTracker:
    def __init__(self):
        self.agua = 0  # em ml

    def registrar_agua(self, quantidade):
        if quantidade > 0:
            self.agua += quantidade
            return True
        return False

    def status_agua(self):
        return f"Você bebeu {self.agua}ml de água hoje."