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
        for card in hand.get_cards():
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params['suits']):
                current.add_bonus( int(params['value']))
                found = True
        return found

    @staticmethod
    def with_card(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.get_cards():
            if card.is_same_as(current):
                continue
            if card.is_among(params['cards']):
                current.add_bonus(int(params['value']))
                found = True

        return found

    @staticmethod
    def with_any_one_suit(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.get_cards():
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params['suits']):
                found = True

        if found:
            current.add_bonus(int(params['value']))

        return found


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

    public static function changeSuit(Hand hand, Card current, array params): bool
    {
        foreach (hand->getCards() as card) {
            if (!card->isSameAs(params['card'])) {
                continue
            }
            card->changeSuit(params['suit'])
            return true
        }
        return false
    }

    public static function clearsPenalty(Hand hand, Card current, array params): bool
    {
        found = false
        foreach (hand->getCards() as card) {
            if (card->isSameAs(current)) {
                continue
            }
            if (card->hasSuitAmong(params['suits'])) {
                card->clearPenalty()
                found = true
            }
        }

        return found
    }

    public static function clearsWordFromPenalty(Hand hand, Card current, array params): bool
    {
        foreach (hand->getCards() as card) {
            if (card->isSameAs(current)) {
                continue
            }
            if (card->hasPenalty()) {
                card->removeWordFromPenalty(params['word'])
            }
        }

        return false
    }

    public static function differentCardsInSameSuit(Hand hand, Card current, array params): bool
    {
        countSuits = []
        foreach (hand->getCards() as card) {
            if (!isset(countSuits[card->getSuit()])) {
                countSuits[card->getSuit()] = 1
            } else {
                countSuits[card->getSuit()]++
            }
        }
        foreach (countSuits as count) {
            if (count >= (int) params['cards']) {
                current->addBonus((int) params['value'])
                return true
            }
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



    public static function ifNo(Hand hand, Card current, array params): bool
    {
        foreach (hand->getCards() as card) {
            if (card->isSameAs(current)) {
                continue
            }
            if (card->hasSuitAmong(params['suits'])) {
                return false
            }
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



    public static function withBothCards(Hand hand, Card current, array params): bool
    {
        foreach (params['cards'] as card) {
            if (!hand->hasCard(card)) {
                return false
            }
        }
        foreach (params['suits'] as suit) {
            if (!hand->hasSuit(suit, current)) {
                return false
            }
        }
        current->addBonus((int) params['value'])

        return true
    }



    public static function withCardAndEither(Hand hand, Card current, array params): bool
    {
        foreach (params['cards'] as card) {
            if (!hand->hasCard(card)) {
                return false
            }
        }
        foreach (params['either'] as card) {
            if (hand->hasCard(card)) {
                current->addBonus((int) params['value'])
                return true
            }
        }

        return false
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
