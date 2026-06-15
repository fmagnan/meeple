from typing import TYPE_CHECKING, Any

from fantasy_realms.bonus import Bonus
from fantasy_realms.glossary import Action, Suit
from fantasy_realms.penalty import Penalty

if TYPE_CHECKING:
    from fantasy_realms.hand import Hand


class Card:

    def __init__(self, name: str, suit: int, base_strength: int, bonus: dict[str, Any], penalty: dict[str, Any] = {}):
        self.name :str = name
        self.suit :int = suit
        self.base_strength :int = base_strength
        self.bonus :dict[str, Any] = bonus
        self.penalty :dict[str, Any] = penalty
        self.value :int= base_strength

    @classmethod
    def from_conf(cls, name: str, conf: dict[str, Any]={}):
        return cls(name, int(conf.get('suit', 0)), int(conf.get('base_strength', 0)), conf.get('bonus', {}), conf.get('penalty', {}))

    def is_prior(self, bonus: dict[str, Any]):
        if (bonus.get('and')):
            for subBonus in bonus['and']:
                if self.is_prior(subBonus):
                    return True
        if (not bonus.get('action')):
            return False
        return bonus['action'] in [
            Action.CLEARS_PENALTY,
            Action.CLEARS_WORD_FROM_PENALTY,
            Action.CHANGE_SUIT,
            Action.DUPLICATE,
            Action.TAKE_ON_NAME_AND_SUIT
        ]

    def apply(self, hand: "Hand"):
        self.apply_bonus(hand)
        self.apply_penalty(hand)

        return hand

    def apply_bonus(self, hand: "Hand"):
        if len(self.bonus) == 0:
            return
        if self.bonus.get('and'):
            for bonus in self.bonus['and']:
                bonus.apply(hand, self, self.bonus)
            return
        if self.bonus.get('or'):
            for bonus in self.bonus['or']:
                if bonus.apply(hand, self, self.bonus):
                    break
            return
        Bonus.apply(hand, self, self.bonus)

    def apply_penalty(self, hand: "Hand"):
        if len(self.penalty) == 0:
            return
        if self.penalty.get('and'):
            for penalty in self.penalty['and']:
                penalty.apply(hand, self, self.penalty)
            return
        if self.penalty.get('or'):
            for penalty in self.penalty['or']:
                if penalty.apply(hand, self, self.penalty):
                    break
            return
        Penalty.apply(hand, self, self.penalty)

    def get_bonus(self) -> dict[str, Any]:
         return self.bonus

    def get_value(self) -> int:
        return self.value

    def has_suit_among(self, suits :list[Suit]) -> bool:
        return self.suit in suits

    def is_same_as(self, card: "Card|str") -> bool:
        if isinstance(card, Card):
            return card.get_name() == self.name
        return card == self.name

    def substract_penalty(self, penalty_amount :int) -> None:
        self.value -= penalty_amount

    def get_name(self) -> str:
        return self.name

    def add_bonus(self, value: int):
        self.value += value

    def is_among(self, cards: list["Card|str"]) -> bool:
        return self.name in cards

    def blank(self):
        self.base_strength = 0
        self.value=0
        self.bonus = {}
        self.penalty = {}
        self.name = ''
        self.suit = Suit.NONE
"""

    public function changeSuit(int $suit): self
    {
        $this->suit = $suit;

        return $this;
    }

    public function clearPenalty(): self
    {
        $this->penalty = [];

        return $this;
    }

    public function duplicate(Card $from): self
    {
        $this->name = $from->getName();
        $this->base_strength = $from->getBaseStrength();
        $this->value = $this->base_strength;
        $this->bonus = [];
        $this->penalty = $from->getPenalty();
        $this->suit = $from->getSuit();

        return $this;
    }

    public static function fromConf(string $name, array $conf) : self
    {
        return new self($name, (int) $conf['suit'], (int) $conf['base_strength'], $conf['bonus'] ?? [], $conf['penalty'] ?? []);
    }

    public static function fromDeck(string $name, array $deck) : self
    {
        return self::fromConf($name, $deck[$name]);
    }

    public function getBaseStrength(): int
    {
        return $this->base_strength;
    }

    public function getPenalty(): array
    {
        return $this->penalty;
    }

    public function getSuit(): int
    {
        return $this->suit;
    }

    public function hasPenalty(): bool
    {
        return !empty($this->penalty);
    }

    public function isBlanked(): bool
    {
        return $this->suit === Glossary::SUIT_NONE;
    }

    public function removeWordFromPenalty(int|string $word): self
    {
        if (is_int($word)) {
            if (($key = array_search($word, $this->penalty['suits'])) !== false) {
                unset($this->penalty['suits'][$key]);
            }
        } else {
            if (($key = array_search($word, $this->penalty['cards'])) !== false) {
                unset($this->penalty['cards'][$key]);
            }
        }

        return $this;
    }


    public function takeOnNameAndSuit(Card $from) : self
    {
        $this->name = $from->getName();
        $this->suit = $from->getSuit();

        return $this;
    }
"""
