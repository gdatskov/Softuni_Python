from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player.name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_info = [f"Guild: {self.name}"]
        [guild_info.append(f"{player.player_info()}") for player in self.players]
        return "\n".join(guild_info)
