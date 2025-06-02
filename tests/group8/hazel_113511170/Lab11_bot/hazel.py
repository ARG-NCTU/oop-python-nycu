from random import choice

from resources.weapons import Weapons

from bots import ABCBot

class Bot(ABCBot):
    """
    A bot to fire anything at anyone but itself
    """

    def action(self, country_status: dict, world_state: dict):
        if self.has_nukes(country_status) and country_status["Health"]>=60:
            weapon = (Weapons.NUKE)
        
        else:
            weapon = (Weapons.MAGIC)

       

        # Don't shoot yourself
        target_choices = world_state["alive_players"]
        target_choices.remove(country_status["ID"])

        health_list = []
        for i in target_choices:
            health_list.append(world_state["countries"][i]["Health"])

        alive_health = dict(zip(target_choices,health_list))

        # Fire!
        target = min(alive_health, key=lambda k:alive_health[k])

        return {
            "Weapon": weapon,
            "Target": target,
            "Type": "Attack",
        }
