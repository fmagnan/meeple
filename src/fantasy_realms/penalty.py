from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from fantasy_realms.card import Card
    from fantasy_realms.hand import Hand


class Penalty:
    @staticmethod
    def apply(hand: "Hand", current: "Card", conf: dict[str, Any]):
        action = Penalty.get_action(conf)
        method = getattr(Penalty, action)
        return method(hand, current, conf)

    @staticmethod
    def get_action(conf: dict[str, Any]) -> str:
        return conf["action"]

    @staticmethod
    def unless_at_least(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params["suits"]):
                found = True
        if not found:
            current.substract_penalty(int(params["value"]))

        return not found

    @staticmethod
    def blanks(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        target_suits = params.get("targets", {}).get("suits", [])
        excludes = params.get("excludes", [])
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if len(target_suits) == 0 or card.has_suit_among(target_suits):
                if "suits" in excludes and card.has_suit_among(excludes["suits"]):
                    continue
                if "cards" in excludes and card.is_among(excludes["cards"]):
                    continue
                card.blank()
                found = True
        return found

    @staticmethod
    def for_each(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params["suits"]):
                current.substract_penalty(int(params["value"]))
                found = True
        return found

    @staticmethod
    def blanked_unless(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params["suits"]):
                return False
            current.blank()
            found = True
        return found

    @staticmethod
    def with_card(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.is_among(params["cards"]):
                current.substract_penalty(int(params["value"]))
                found = True
        return found
