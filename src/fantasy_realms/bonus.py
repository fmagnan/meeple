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
            if not card.is_same_as(params['card']):
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
                count_suits[card.suit] = 1
            else:
                count_suits[card.suit] += 1
        for suit, count in count_suits.items():
            if count >= int(params['cards']):
                current.add_bonus(int(params['value']))
                return True
        return False

    @staticmethod
    def each_active_card_is_from_different_suit(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        suits = []
        for card in hand.cards:
            if card.is_blanked():
                continue
            if card.suit in suits:
                return False
            suits.append(card.suit)
        current.add_bonus(int(params['value']))
        return True

    @staticmethod
    def card_run(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        base_strengths = []
        for card in hand.cards:
            if not card.base_strength in base_strengths:
                base_strengths.append(card.base_strength)
        longest_run = Bonus.look_for_longest_run(base_strengths)
        if longest_run >= int(params['cards']):
            current.add_bonus(int(params['value']))
            return True
        return False

    @staticmethod
    def look_for_longest_run(strengths: list[int]) -> int:
        if len(strengths) == 0:
            return 0
        strengths.sort()
        longest_run = []
        current_run = [strengths[0]]
        for i in range(1, len(strengths)):
            if strengths[i] == strengths[i-1] +1:
                current_run.append(strengths[i])
            else:
                if len(current_run) > len(longest_run):
                    longest_run = current_run
                current_run =[strengths[i]]
        if len(current_run) > len(longest_run):
            longest_run=current_run
        return len(longest_run)

    @staticmethod
    def add_base_strength_among(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        maximum_value = 0
        for card in hand.cards:
            if card.is_same_as(current):
                continue
            if not card.has_suit_among(params['suits']):
                continue
            if card.base_strength > maximum_value:
                maximum_value = card.base_strength
        current.add_bonus(maximum_value)
        return False
"""

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

"""
