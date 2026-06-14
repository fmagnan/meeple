from fantasy_realms.card import Card


class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.cards :list[Card] = []

    def add_card(self, name :str, params={}):
        conf = self.deck[name]
        conf['bonus'] = params | conf.get('bonus', {})
        self.cards.append(Card.from_conf(name, conf))

    def count_cards(self):
        return len(self.cards)

    def sort_cards_by_priority(self):
        for index, card in enumerate(self.cards):
            if card.is_prior(card.get_bonus()):
                out = self.cards[index, index+1]
                self.cards[0,0] = out

    def get_total(self):
        self.sort_cards_by_priority()
        for card in self.cards:
            card.apply(self)
        total = 0
        for card in self.cards:
            total += card.get_value()

        return total

    def get_cards(self) -> list[Card]:
        return self.cards

    """
{
    /** @var Card[] */
    private array $cards = [];






    public function hasCard(string $name): bool
    {
        foreach ($this->cards as $card) {
            if ($name === $card->getName()) {
                return true;
            }
        }

        return false;
    }

    public function hasSuit(int $suit, Card $exclude): bool
    {
        foreach ($this->cards as $item) {
            if ($item->getName() === $exclude->getName()) {
                continue;
            }
            if ($suit === $item->getSuit()) {
                return true;
            }
        }

        return false;
    }


}
"""
