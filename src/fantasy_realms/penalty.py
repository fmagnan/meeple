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
        return conf['action']

    @staticmethod
    def add_base_strength_among(hand: "Hand", current: "Card", conf: dict[str, Any]) -> bool:
        return False

    @staticmethod
    def unless_at_least(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        found = False
        for card in hand.get_cards():
            if card.is_same_as(current):
                continue
            if card.has_suit_among(params['suits']):
                found = True
        if not found:
            current.substract_penalty(int(params['value']))

        return not found

    @staticmethod
    def blanks(hand: "Hand", current: "Card", params: dict[str, Any]) -> bool:
        target_suits = params.get('targets', {}).get('suits', [])
        excludes = params.get('targets', [])
        found = False
        for card in hand.get_cards():
            if card.is_same_as(current):
                continue
            if len(target_suits) == 0 or card.has_suit_among(target_suits):
                if 'suits' in excludes and card.has_suit_among(excludes['suits']):
                    continue
                if 'cards' in excludes and card.is_among(excludes['cards']):
                    continue
                card.blank()
                found = True
        return found


"""

public static function apply(Hand $hand, Card $current, array $conf): bool
    {
        return self::{self::getAction($conf)}($hand, $current, $conf);
    }

    public static function blankedUnless(Hand $hand, Card $current, array $params): bool
    {
        $found = false;
        foreach ($hand->getCards() as $card) {
            if ($card->isSameAs($current)) {
                continue;
            }
            if ($card->hasSuitAmong($params['suits'])) {
                return false;
            }
            $current->blank();
            $found = true;
        }

        return $found;
    }



    public static function forEach(Hand $hand, Card $current, array $params): bool
    {
        $found = false;
        foreach ($hand->getCards() as $card) {
            if ($card->isSameAs($current)) {
                continue;
            }
            if ($card->hasSuitAmong($params['suits'])) {
                $current->substractPenalty((int) $params['value']);
                $found = true;
            }
        }

        return $found;
    }



    public static function withCard(Hand $hand, Card $current, array $params): bool
    {
        $found = false;
        foreach ($hand->getCards() as $card) {
            if ($card->isSameAs($current)) {
                continue;
            }
            if ($card->isAmong($params['cards'])) {
                $current->substractPenalty((int) $params['value']);
                $found = true;
            }
        }

        return $found;
    }


}
"""
