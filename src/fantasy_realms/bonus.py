from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from fantasy_realms.card import Card
    from fantasy_realms.hand import Hand

class Bonus:

    @staticmethod
    def apply(hand: "Hand", current: "Card", conf: dict[str, Any]) -> bool:
        action = Bonus.get_action(conf)
        method = getattr(Bonus, action)
        return method(hand, current, conf)

    @staticmethod
    def get_action(conf: dict[str, Any]) -> str:
        return conf['action']

    @staticmethod
    def add_base_strength_among(hand: "Hand", current: "Card", conf: dict[str, Any]) -> bool:
        return False

    @staticmethod
    def for_each(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params['suits']):
                current.add_bonus( int(params['value']))
                found = True
        return found

    @staticmethod
    def with_card(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.is_among(params['cards']):
                current.add_bonus(int(params['value']))
                found = True

        return found

    @staticmethod
    def with_any_one_suit(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params['suits']):
                found = True

        if found:
            current.add_bonus(int(params['value']))
        return found

    @staticmethod
    def clears_penalty(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params['suits']):
                card.clear_penalty()
                found = True
        return found

    @staticmethod
    def if_no(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found=True
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params['suits']):
                return False
        current.add_bonus(int(params['value']))
        return found

    @staticmethod
    def with_both_cards(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        for card in params['cards']:
            if not hand.has_card(card):
                return False
        for suit in params['suits']:
            if not hand.has_suit(suit, current):
                return False
        current.add_bonus(int(params['value']))
        return True

    @staticmethod
    def change_suit(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        for card in hand.cards:
            if card.is_same_as(params['card']):
                continue
            card.change_suit(params['suit'])
            return True
        return False

    @staticmethod
    def with_card_and_either(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        for card in params['cards']:
            if not hand.has_card(card):
                return False
        for card in params['either']:
            if hand.has_card(card):
                current.add_bonus(int(params['value']))
                return True
        return False

    @staticmethod
    def clears_word_from_penalty(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if card.has_penalty():
                card.remove_word_from_penalty(params['word'])
        return False

    @staticmethod
    def different_cards_in_same_suit(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        count_suits = {}
        for card in hand.cards:
            if not count_suits.get(card.suit):
                count_suits[str(card.suit)] = 1
            else:
                count_suits[str(card.suit)] += 1
        for suit, count in count_suits.items():
            if count >= int(params['cards']):
                current.add_bonus(int(params['value']))
                return True
        return False



"""

    public static function addBaseStrengthAmong(Hand hand, Card current, array params): bool
    {
        maximumValue = 0
        foreach (hand->getCards() as card) {
            if (card->isSameAs(current)) {
                continue
            }
            if (!card->hasSuitAmong(params['suits'])) {
                continue
            }
            if (card->getBaseStrength() > maximumValue) {
                maximumValue = card->getBaseStrength()
            }
        }
        current->addBonus(maximumValue)

        return false
    }

    public static function cardRun(Hand hand, Card current, array params): bool
    {
        baseStrengths = []
        foreach (hand->getCards() as card) {
            if (!in_array(card->getBaseStrength(), baseStrengths)) {
                baseStrengths[] = card->getBaseStrength()
            }
        }
        longestRun = self::lookForLongestRun(baseStrengths)

        if (longestRun >= params['cards']) {
            current->addBonus((int) params['value'])
            return true
        }

        return false
    }





    public static function duplicate(Hand hand, Card current, array params): bool
    {
        foreach (hand->getCards() as card) {
            if (card->isSameAs(params['card'])) {
                current->duplicate(card)
                return true
            }
        }

        return false
    }

    public static function eachActiveCardIsDifferentSuit(Hand hand, Card current, array params): bool
    {
        suits = []
        foreach (hand->getCards() as card) {
            if (card->isBlanked()) {
                continue
            }
            if (in_array(card->getSuit(), suits, true)) {
                return false
            }
            suits[] = card->getSuit()
        }
        current->addBonus((int) params['value'])

        return true
    }

    public static function takeOneMoreCardAtEnd(Hand hand, Card current, array params): bool
    {
        hand->addCard(params['card'])

        return true
    }

    public static function takeOnNameAndSuit(Hand hand, Card current, array params): bool
    {
        current->takeOnNameAndSuit(params['card'])

        return true
    }

    public static function withAnyOneCard(Hand hand, Card current, array params): bool
    {
        found = false
        foreach (hand->getCards() as card) {
            if (card->isSameAs(current)) {
                continue
            }
            if (card->isAmong(params['cards'])) {
                found = true
            }
        }
        if (found) {
            current->addBonus((int) params['value'])
        }

        return found
    }









    private static function getAction(array conf): string
    {
        return conf['action']
    }

    private static function lookForLongestRun(array input): int
    {
        if (empty(input)) {
            return 0
        }

        sort(input)

        longestRun = []
        currentRun = [input[0]]

        for (i = 1 i < count(input) i++) {
            if (input[i] == (input[i - 1] + 1)) {
                currentRun[] = input[i]
            } else {
                if (count(currentRun) > count(longestRun)) {
                    longestRun = currentRun
                }
                currentRun = [input[i]]
            }
        }
        if (count(currentRun) > count(longestRun)) {
            longestRun = currentRun
        }

        return count(longestRun)
    }
}

"""
