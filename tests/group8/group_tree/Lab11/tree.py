from random import choice

from resources.weapons import Weapons

from bots import ABCBot


class Bot(ABCBot):
    """
    A bot to fire anything at anyone but itself
    """

    def action(self, country_status: dict, world_state: dict):
        weapon_choices = list(Weapons)
        weapon_choices.remove(Weapons.MISSILE)
        weapon_choices.remove(Weapons.LASER)
        weapon_choices.remove(Weapons.DIRT1)
        weapon_choices.remove(Weapons.DIRT2)
        weapon_choices.remove(Weapons.DIRT3)
        weapon_choices.remove(Weapons.DIRT4)
        weapon_choices.remove(Weapons.DIRT5)
        if not self.has_nukes(country_status):
            # If you don't have nukes don't try firing them
            weapon_choices.remove(Weapons.NUKE)

        # Don't shoot yourself please...
        target_choices = world_state["alive_players"]
        target_choices.remove(country_status["ID"])

        # Fire!
        target = choice(tuple(world_state["alive_players"]))
        if target_choices:
            for i in world_state["alive_players"]:
                if i != country_status["ID"]:
                    if world_state["countries"][i]["Health"] <= world_state["countries"][target]["Health"]:
                        target = i                     
            weapon = choice(weapon_choices)

            return {
                "Weapon": weapon,
                "Target": target,
                "Type": "Attack",
            }

        return {}
