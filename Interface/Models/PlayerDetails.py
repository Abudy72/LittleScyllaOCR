from enum import Enum


class PlayerStats:
    def __init__(self, kills, deaths, assists, gold_earned, gpm,
                 player_dmg, minion_dmg, taken_dmg, mitigated_dmg,
                 structure_dmg, player_healing, wards_placed):
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.gold_earned = gold_earned
        self.gpm = gpm
        self.player_dmg = player_dmg
        self.minion_dmg = minion_dmg
        self.taken_dmg = taken_dmg
        self.mitigated_dmg = mitigated_dmg
        self.structure_dmg = structure_dmg
        self.player_healing = player_healing
        self.wards_placed = wards_placed
        self.match_time = self.calculate()

    def calculate(self):
        match_time = self.gold_earned / self.gpm
        return match_time


class PlayerDetailsContainer:
    def __init__(self, player_name, player_stats):
        self.player_name = player_name
        self.player_stats = player_stats
