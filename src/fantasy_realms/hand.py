from fantasy_realms.card import Card
from typing import Any

class Hand:
    def __init__(self, deck: dict[str, Any]):
        self.deck: dict[str, Any] = deck
        self.cards :list[Card] = []

    def add_card(self, name :str, params={}):
        conf = self.deck[name]
        conf['bonus'] = params | conf.get('bonus', {})
        self.cards.append(Card.from_conf(name, conf))

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

    def has_card(self, name: str) -> bool:
        for card in self.cards:
            if name == card.name:
                return True
        return False

    def has_suit(self, suit: int, exclude: Card) -> bool:
        for card in self.cards:
            if card.name == exclude.name:
                continue
            if suit == card.suit:
                return True
        return False
