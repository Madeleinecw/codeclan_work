
class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        result = False
        for name in self.players:
            if name == player:
                result = True
                return result
            elif not name == player:
                return result        


