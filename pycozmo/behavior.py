"""

Behavior classes.

"""

from typing import Dict, Any


__all__ = [
    "ReactionTrigger",
    "Behavior",

    "load_behaviors",
    "load_reaction_trigger_behavior_map",
]


class ReactionTrigger:
    """ Reaction trigger representation class. """

    def __init__(self, name: str):
        self.name = str(name)
        # TODO


class Behavior:
    """
    Behavior representation class.

    "requiredUnlockId" is ignored.
    """

    __slots__ = [
        "behavior_class",
        "id",
        "needs_action_id",
        "display_name_key",
        "params",
    ]

    def __init__(self,
                 behavior_class: str,
                 behavior_id: str,
                 needs_action_id: str,
                 display_name_key,
                 params: Dict[str, Any]) -> None:
        self.behavior_class = str(behavior_class)
        self.id = str(behavior_id)
        self.needs_action_id = str(needs_action_id)
        self.display_name_key = str(display_name_key)
        self.params = dict(params)


def load_behaviors() -> Dict[str, Behavior]:
    # TODO: Load cozmo_resources/config/engine/behaviorSystem/behaviors/*/*.json
    behaviors = {}
    return behaviors


def load_reaction_trigger_behavior_map() -> Dict[str, ReactionTrigger]:
    # TODO: Load cozmo_resources/config/engine/behaviorSystem/reactionTrigger_behavior_map.json
    reaction_trigger_behavior_map = {}
    return reaction_trigger_behavior_map