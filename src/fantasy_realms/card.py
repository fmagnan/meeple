from typing import TYPE_CHECKING, Any

from fantasy_realms.bonus import Bonus
from fantasy_realms.glossary import Action, Name, Suit
from fantasy_realms.penalty import Penalty

if TYPE_CHECKING:
    from fantasy_realms.hand import Hand


class Card:
    def __init__(
        self,
        name: Name,
        suit: int,
        base_strength: int,
        bonus: dict[str, Any],
        penalty: dict[str, Any] = {},
    ):
        self.name: Name = name
        self.suit: int = suit
        self.base_strength: int = base_strength
        self.bonus: dict[str, Any] = bonus
        self.penalty: dict[str, Any] = penalty
        self.value: int = base_strength

    @classmethod
    def from_conf(cls, name: Name, conf: dict[str, Any] = {}) -> "Card":
        return cls(
            name,
            int(conf.get("suit", 0)),
            int(conf.get("base_strength", 0)),
            conf.get("bonus", {}),
            conf.get("penalty", {}),
        )

    def is_prior(self, bonus: dict[str, Any]):
        if bonus.get("and"):
            for subBonus in bonus["and"]:
                if self.is_prior(subBonus):
                    return True
        if not bonus.get("action"):
            return False
        return bonus["action"] in [
            Action.CLEARS_PENALTY,
            Action.CLEARS_WORD_FROM_PENALTY,
            Action.CHANGE_SUIT,
            Action.DUPLICATE,
            Action.TAKE_ON_NAME_AND_SUIT,
        ]

    def apply(self, hand: "Hand"):
        self.apply_bonus(hand)
        self.apply_penalty(hand)

        return hand

    def apply_bonus(self, hand: "Hand"):
        if len(self.bonus) == 0:
            return
        if self.bonus.get("and"):
            for bonus in self.bonus["and"]:
                Bonus.apply(hand, self, bonus)
            return
        if self.bonus.get("or"):
            for bonus in self.bonus["or"]:
                if Bonus.apply(hand, self, bonus):
                    break
            return
        Bonus.apply(hand, self, self.bonus)

    def apply_penalty(self, hand: "Hand"):
        if len(self.penalty) == 0:
            return
        if self.penalty.get("and"):
            for penalty in self.penalty["and"]:
                Penalty.apply(hand, self, penalty)
            return
        if self.penalty.get("or"):
            for penalty in self.penalty["or"]:
                if Penalty.apply(hand, self, penalty):
                    break
            return
        Penalty.apply(hand, self, self.penalty)

    def has_suit_among(self, suits: list[Suit]) -> bool:
        return self.suit in suits

    def is_same_as(self, card: "Card") -> bool:
        return card.name == self.name

    def substract_penalty(self, penalty_amount: int) -> None:
        self.value -= penalty_amount

    def add_bonus(self, value: int):
        self.value += value

    def is_among(self, cards: list["Card"]) -> bool:
        return self.name in cards

    def blank(self):
        self.base_strength = 0
        self.value = 0
        self.bonus = {}
        self.penalty = {}
        self.name = Name.NONE
        self.suit = Suit.NONE

    def clear_penalty(self):
        self.penalty = {}

    def change_suit(self, suit: Suit):
        self.suit = suit

    def has_penalty(self) -> bool:
        return len(self.penalty) > 0

    def remove_word_from_penalty(self, word: int):
        if word not in self.penalty.get("suits", []):
            return
        self.penalty["suits"].remove(word)

    def is_blanked(self):
        return self.suit == Suit.NONE

    def duplicate(self, origin: "Card"):
        self.name = origin.name
        self.base_strength = origin.base_strength
        self.value = origin.base_strength
        self.bonus = {}
        self.penalty = origin.penalty
        self.suit = origin.suit

    def take_on_name_and_suit(self, origin: "Card"):
        self.name = origin.name
        self.suit = origin.suit
