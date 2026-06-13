from enum import IntEnum, StrEnum


class Suit(IntEnum):
    NONE = 0
    ARMY = 1
    ARTIFACT = 2
    BEAST = 3
    FLAME = 4
    FLOOD = 5
    LAND = 6
    LEADER = 7
    WEAPON = 8
    WEATHER = 9
    WILD = 10
    WIZARD = 11


class Card(StrEnum):
    AIR_ELEMENTAL = 'Air Elemental'
    BASILISK = 'Basilisk'
    BEASTMASTER = 'Beastmaster'
    BELL_TOWER = 'Bell Tower'
    BLIZZARD = 'Blizzard'
    BOOK_OF_CHANGES = 'Book of Changes'
    CANDLE = 'Candle'
    CELESTIAL_KNIGHTS = 'Celestial Knights'
    COLLECTOR = 'Collector'
    DOPPELGANGER = 'Doppelganger'
    DRAGON = 'Dragon'
    DWARVISH_INFANTRY = 'Dwarvish Infantry'
    EARTH_ELEMENTAL = 'Earth Elemental'
    ELEMENTAL_ENCHANTRESS = 'Elemental Enchantress'
    ELVEN_ARCHERS = 'Elven Archers'
    ELVEN_LONGBOW = 'Elven Longbow'
    EMPRESS = 'Empress'
    GEM_OF_ORDER = 'Gem of Order'
    LIGHT_CALVARY = 'Light Cavalry'
    FIRE_ELEMENTAL = 'Fire Elemental'
    FOREST = 'Forest'
    FORGE = 'Forge'
    FOUNTAIN_OF_LIFE = 'Fountain of Life'
    GREAT_FLOOD = 'Great Flood'
    HYDRA = 'Hydra'
    ISLAND = 'Island'
    KING = 'King'
    LIGHTNING = 'Lightning'
    MAGIC_WAND = 'Magic Wand'
    MIRAGE = 'Mirage'
    MOUNTAIN = 'Mountain'
    NECROMANCER = 'Necromancer'
    PRINCESS = 'Princess'
    PROTECTION_RUNE = 'Protection Rune'
    QUEEN = 'Queen'
    RAINSTORM = 'Rainstorm'
    RANGERS = 'Rangers'
    SHAPESHIFTER = 'Shapeshifter'
    SHIELD_OF_KETH = 'Shield of Keth'
    SMOKE = 'Smoke'
    SWAMP = 'Swamp'
    SWORD_OF_KETH = 'Sword of Keth'
    UNDERGROUND_CAVERNS = 'Underground Caverns'
    UNICORN = 'Unicorn'
    WAR_DIRIGIBLE = 'War Dirigible'
    WARHORSE = 'Warhorse'
    WARLOCK_LORD = 'Warlock Lord'
    WARLORD = 'Warlord'
    WARSHIP = 'Warship'
    WATER_ELEMENTAL = 'Water Elemental'
    WHIRLWIND = 'Whirlwind'
    WILDFIRE = 'Wildfire'
    WORLD_TREE = 'World Tree'


class Action(StrEnum):
    ADD_BASE_STRENGTH_AMONG = 'add_base_strength_among'
    BLANKED_UNLESS = 'blanked_unless'
    BLANKED_WITH = 'blanked_with'
    BLANKS = 'blanks'
    CARD_RUN = 'card_run'
    CHANGE_SUIT = 'change_suit'
    CLEARS_PENALTY = 'clears_penalty'
    CLEARS_WORD_FROM_PENALTY = 'clears_word_from_penalty'
    DIFFERENT_CARDS_IN_SAME_SUIT = 'different_cardsin_same_suit'
    DUPLICATE = 'duplicate'
    EACH_ACTIVE_CARD_IS_FROM_DIFFERENT_SUIT = 'each_active_card_is_from_different_suit'
    FOR_EACH = 'for_each'
    IF_NO = 'if_no'
    TAKE_ON_NAME_AND_SUIT = 'take_on_name_and_suit'
    TAKE_ONE_MORE_CARD_AT_THE_END = 'take_one_more_card_at_the_end'
    UNLESS_AT_LEAST = 'unless_at_least'
    WITH_ANY_ONE_CARD = 'with_any_one_card'
    WITH_ANY_ONE_SUIT = 'with_any_one_suit'
    WITH_BOTH_CARDS = 'with_both_cards'
    WITH_CARD = 'with_card'
    WITH_CARD_AND_EITHER = 'with_card_and_either'
    WITH_SUITS = 'with_suits'
