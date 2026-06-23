from typing import Any

from fantasy_realms.card import Card
from fantasy_realms.glossary import Name, Suit


class Hand:
    def __init__(self, deck: dict[str, Any]):
        self.deck: dict[str, Any] = deck
        self.cards: list[Card] = []

    def add_card(self, name: Name, params: dict[str, Any] | None = None):
        if params is None:
            params = {}
        if isinstance(params.get("card"), Name):
            params["card"] = Card.from_conf(params["card"], self.deck[params["card"]])
        conf = self.deck[name]
        conf["bonus"] = params | conf.get("bonus", {})
        card = Card.from_conf(name, conf)
        self.cards.append(card)

    def count_cards(self):
        return len(self.cards)

    def sort_cards_by_priority(self) -> None:
        for index, card in enumerate(self.cards):
            if card.is_prior(card.bonus):
                out = self.cards.pop(index)
                self.cards.insert(0, out)

    def get_total(self):
        self.sort_cards_by_priority()
        for card in self.cards:
            card.apply(self)
        total = 0
        for card in self.cards:
            total += card.value

        return total

    def has_card(self, name: Name) -> bool:
        for card in self.cards:
            if name == card.name:
                return True
        return False

    def has_suit(self, suit: Suit, exclude: Card) -> bool:
        for card in self.cards:
            if card.is_same_as(exclude):
                continue
            if suit == card.suit:
                return True
        return False
