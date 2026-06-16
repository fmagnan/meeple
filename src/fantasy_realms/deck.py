from typing import Any

from fantasy_realms.glossary import Action, Name, Suit

deck: dict[str, Any] = {
      Name.AIR_ELEMENTAL: {
            'suit' : Suit.WEATHER,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.WEATHER
                ]
            }
      },
       Name.BASILISK: {
            'suit': Suit.BEAST,
            'base_strength': 35,
            'penalty': {
                'action': Action.BLANKS,
                'targets': {
                    'suits': [
                        Suit.ARMY,
                        Suit.LEADER,
                        Suit.BEAST
                    ]
                }
            }
        },
        Name.BEASTMASTER: {
            'suit': Suit.WIZARD,
            'base_strength': 9,
            'bonus': {
                'and': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 9,
                        'suits': [
                            Suit.BEAST
                        ]
                    },
                    {
                        'action': Action.CLEARS_PENALTY,
                        'suits': [
                            Suit.BEAST
                        ]
                    }
                ]
            }
        },
        Name.BELL_TOWER: {
            'suit': Suit.LAND,
            'base_strength': 8,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 15,
                'suits': [
                    Suit.WIZARD
                ]
            },
        },
        Name.BLIZZARD: {
            'suit': Suit.WEATHER,
            'base_strength': 30,
            'penalty': {
                'and': [
                    {
                        'action': Action.BLANKS,
                        'targets': {
                            'suits': [
                                Suit.FLOOD
                            ]
                        }
                    },
                    {
                        'action': Action.FOR_EACH,
                        'value': 5,
                        'suits': [
                            Suit.ARMY,
                            Suit.BEAST,
                            Suit.FLAME,
                            Suit.LEADER,
                        ]
                    }
                ]
            }
        },
        Name.BOOK_OF_CHANGES: {
            'suit': Suit.ARTIFACT,
            'base_strength': 3,
            'bonus': {
                'action': Action.CHANGE_SUIT
            }
        },
        Name.CANDLE: {
            'suit': Suit.FLAME,
            'base_strength': 2,
            'bonus': {
                'action': Action.WITH_BOTH_CARDS,
                'value': 100,
                'cards': [
                    Name.BELL_TOWER,
                    Name.BOOK_OF_CHANGES,
                ],
                'suits': [
                    Suit.WIZARD
                ]
            }
        },
        Name.CELESTIAL_KNIGHTS: {
            'suit': Suit.ARMY,
            'base_strength': 20,
            'penalty': {
                'action': Action.UNLESS_AT_LEAST,
                'value': 8,
                'suits': [
                    Suit.LEADER
                ]
            },
        },
        Name.COLLECTOR: {
            'suit': Suit.WIZARD,
            'base_strength': 7,
            'bonus': {
                'or': [
                    {
                        'action': Action.DIFFERENT_CARDS_IN_SAME_SUIT,
                        'value': 100,
                        'cards': 5
                    },
                    {
                        'action': Action.DIFFERENT_CARDS_IN_SAME_SUIT,
                        'value': 40,
                        'cards': 4
                    },
                    {
                        'action': Action.DIFFERENT_CARDS_IN_SAME_SUIT,
                        'value': 10,
                        'cards': 3
                    },
                ]
            }
        },
        Name.DOPPELGANGER: {
            'suit': Suit.WILD,
            'base_strength': 0,
            'bonus': {
                'action': Action.DUPLICATE
            }
        },
        Name.DRAGON: {
            'suit': Suit.BEAST,
            'base_strength': 30,
            'penalty': {
                'action': Action.UNLESS_AT_LEAST,
                'value': 40,
                'suits': [
                    Suit.WIZARD
                ]
            },
        },
        Name.DWARVISH_INFANTRY: {
            'suit': Suit.ARMY,
            'base_strength': 15,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 2,
                'suits': [
                    Suit.ARMY
                ]
            },
        },
        Name.EARTH_ELEMENTAL: {
            'suit': Suit.LAND,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.LAND
                ]
            },
        },
        Name.ELEMENTAL_ENCHANTRESS: {
            'suit': Suit.WIZARD,
            'base_strength': 5,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 5,
                'suits': [
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.WEATHER,
                ]
            },
        },
        Name.ELVEN_ARCHERS: {
            'suit': Suit.ARMY,
            'base_strength': 10,
            'bonus': {
                'action': Action.IF_NO,
                'value': 5,
                'suits': [
                    Suit.WEATHER
                ]
            }
        },
        Name.ELVEN_LONGBOW: {
            'suit': Suit.WEAPON,
            'base_strength': 3,
            'bonus': {
                'action': Action.WITH_ANY_ONE_CARD,
                'value': 30,
                'cards': [
                    Name.ELVEN_ARCHERS,
                    Name.WARLORD,
                    Name.BEASTMASTER
                ]
            },
        },
        Name.EMPRESS: {
            'suit': Suit.LEADER,
            'base_strength': 10,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 10,
                'suits': [
                    Suit.ARMY
                ]
            },
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 5,
                'suits': [
                    Suit.LEADER
                ]
            },
        },
        Name.FIRE_ELEMENTAL: {
            'suit': Suit.FLAME,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.FLAME
                ]
            },
        },
        Name.FOREST: {
            'suit': Suit.LAND,
            'base_strength': 7,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 12,
                'suits': [
                    Suit.BEAST
                ],
                'cards': [
                    Name.ELVEN_ARCHERS
                ]
            }
        },
        Name.FORGE: {
            'suit': Suit.FLAME,
            'base_strength': 9,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 9,
                'suits': [
                    Suit.WEAPON,
                    Suit.ARTIFACT
                ]
            },
        },
        Name.FOUNTAIN_OF_LIFE: {
            'suit': Suit.FLOOD,
            'base_strength': 1,
            'bonus': {
                'action': Action.ADD_BASE_STRENGTH_AMONG,
                'suits': [
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.WEAPON,
                    Suit.WEATHER
                ]
            }
        },
        Name.GEM_OF_ORDER: {
            'suit': Suit.ARTIFACT,
            'base_strength': 5,
            'bonus': {
                'or': [
                    {
                        'action': Action.CARD_RUN,
                        'value': 150,
                        'cards': 7
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 100,
                        'cards': 6
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 60,
                        'cards': 5
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 30,
                        'cards': 4
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 10,
                        'cards': 3
                    },
                ]
            }
        },
        Name.GREAT_FLOOD: {
            'suit': Suit.FLOOD,
            'base_strength': 32,
            'penalty': {
                'action': Action.BLANKS,
                'targets': {
                    'suits': [
                        Suit.ARMY,
                        Suit.LAND,
                        Suit.FLAME
                    ],
                },
                'excludes': {
                    'cards': [
                        Name.MOUNTAIN,
                       Name.LIGHTNING
                    ]
                }
            }
        },
        Name.HYDRA: {
            'suit': Suit.BEAST,
            'base_strength': 12,
            'bonus': {
                'action': Action.WITH_CARD,
                'value': 28,
                'cards': [

                             Name.SWAMP
                ]
            },
        },
        Name.KING: {
            'suit': Suit.LEADER,
            'base_strength': 8,
            'bonus': {
                'or': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 20,
                        'suits': [
                            Suit.ARMY
                        ],
                        'cards': [
                            Name.QUEEN
                        ]
                    },
                    {
                        'action': Action.FOR_EACH,
                        'value': 5,
                        'suits': [
                            Suit.ARMY
                        ]
                    }
                ]
            }
        },
        Name.ISLAND: {
            'suit': Suit.FLOOD,
            'base_strength': 14,
            'bonus': {
                'action': Action.CLEARS_PENALTY,
                'suits': [
                    Suit.FLOOD,
                    Suit.FLAME
                ]
            }
        },
        Name.LIGHT_CALVARY: {
            'suit': Suit.ARMY,
            'base_strength': 17,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 2,
                'suits': [
                    Suit.LAND
                ]
            },
        },
        Name.LIGHTNING: {
            'suit': Suit.FLAME,
            'base_strength': 11,
            'bonus': {
                'action': Action.WITH_CARD,
                'value': 30,
                'cards': [
                    Name.RAINSTORM
                ]
            },
        },
        Name.MAGIC_WAND: {
            'suit': Suit.WEAPON,
            'base_strength': 1,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 25,
                'suits': [
                    Suit.WIZARD
                ]
            },
        },
        Name.MIRAGE: {
            'suit': Suit.WILD,
            'base_strength': 0,
            'bonus': {
                'action': Action.TAKE_ON_NAME_AND_SUIT,
                'suits': [
                    Suit.ARMY,
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.WEATHER,
                ]
            }
        },
        Name.MOUNTAIN: {
            'suit': Suit.LAND,
            'base_strength': 9,
            'bonus': {
                'and': [
                    {
                        'action': Action.WITH_BOTH_CARDS,
                        'value': 50,
                        'cards': [
                            Name.SMOKE,
                            Name.WILDFIRE
                        ]
                    },
                    {
                        'action': Action.CLEARS_PENALTY,
                        'suits': [
                            Suit.FLOOD
                        ]
                    }
                ]
            }
        },
        Name.NECROMANCER: {
            'suit': Suit.WIZARD,
            'base_strength': 3,
            'bonus': {
                'action': Action.TAKE_ONE_MORE_CARD_AT_THE_END,
                'suits': [
                    Suit.ARMY,
                    Suit.BEAST,
                    Suit.LEADER,
                    Suit.WIZARD,
                ]
            }
        },
        Name.PRINCESS: {
            'suit': Suit.LEADER,
            'base_strength': 2,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 8,
                'suits': [
                    Suit.ARMY,
                    Suit.LEADER,
                    Suit.WIZARD,
                ]
            },
        },
        Name.PROTECTION_RUNE: {
            'suit': Suit.ARTIFACT,
            'base_strength': 1,
            'bonus': {
                'action': Action.CLEARS_PENALTY,
                'suits': [
                    Suit.ARMY,
                    Suit.ARTIFACT,
                    Suit.BEAST,
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.LEADER,
                    Suit.WEAPON,
                    Suit.WEATHER,
                    Suit.WILD,
                    Suit.WIZARD,
                ]
            },
        },
        Name.QUEEN: {
            'suit': Suit.LEADER,
            'base_strength': 6,
            'bonus': {
                'or': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 20,
                        'suits': [
                            Suit.ARMY
                ],
                        'cards': [
                            Name.KING
                ]
                    },
                    {
                        'action': Action.FOR_EACH,
                        'value': 5,
                        'suits': [
                            Suit.ARMY
                        ]
                    },
                ]
            }
        },
        Name.RAINSTORM: {
            'suit': Suit.WEATHER,
            'base_strength': 8,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 10,
                'suits': [
                    Suit.FLOOD
                ]
            },
            'penalty': {
                'action': Action.BLANKS,
                'targets': {
                    'suits': [
                        Suit.FLAME
                    ],
                },
                'excludes': {
                    'cards': [
                        Name.LIGHTNING
                    ]
                }
            }
        },
        Name.RANGERS: {
            'suit': Suit.ARMY,
            'base_strength': 5,
            'bonus': {
                'and': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 10,
                        'suits': [
                            Suit.LAND
                        ]
                    },
                    {
                        'action': Action.CLEARS_WORD_FROM_PENALTY,
                        'word': Suit.ARMY
                    }
                ]
            }
        },
        Name.SHAPESHIFTER: {
            'suit': Suit.WILD,
            'base_strength': 0,
            'bonus': {
                'action': Action.TAKE_ON_NAME_AND_SUIT,
                'suits': [
                    Suit.ARTIFACT,
                    Suit.BEAST,
                    Suit.LEADER,
                    Suit.WEAPON,
                    Suit.WIZARD,
                ]
            },
        },
        Name.SHIELD_OF_KETH: {
            'suit': Suit.ARTIFACT,
            'base_strength': 4,
            'bonus': {
                'or': [
                    {
                        'action': Action.WITH_BOTH_CARDS,
                        'value': 40,
                        'suits': [
                            Suit.LEADER
                        ],
                        'cards': [
                            Name.SWORD_OF_KETH
                        ]
                    },
                    {
                        'action': Action.WITH_ANY_ONE_SUIT,
                        'value': 15,
                        'suits': [
                            Suit.LEADER
                        ],
                    },
                ]
            }
        },
        Name.SMOKE: {
            'suit': Suit.WEATHER,
            'base_strength': 27,
            'penalty': {
                'action': Action.BLANKED_UNLESS,
                'suits': [
                    Suit.FLAME
                ]
            },
        },
        Name.SWAMP: {
            'suit': Suit.FLOOD,
            'base_strength': 18,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 3,
                'suits': [
                    Suit.ARMY,
                    Suit.FLAME
                ]
            },
        },
        Name.SWORD_OF_KETH: {
            'suit': Suit.WEAPON,
            'base_strength': 7,
            'bonus': {
                'or': [
                    {
                        'action': Action.WITH_BOTH_CARDS,
                        'value': 40,
                        'suits': [
                            Suit.LEADER
                        ],
                        'cards': [
                            Name.SHIELD_OF_KETH
                        ]
                    },
                    {
                        'action': Action.WITH_ANY_ONE_SUIT,
                        'value': 10,
                        'suits': [
                            Suit.LEADER
                        ]
                    },
                ]
            }
        },
        Name.UNDERGROUND_CAVERNS: {
            'suit': Suit.LAND,
            'base_strength': 6,
            'bonus': {
                'and': [
                    {
                        'action': Action.WITH_CARD,
                        'value': 25,
                        'cards': [
                            Name.DRAGON,
                            Name.DWARVISH_INFANTRY
                        ]
                    },
                    {
                        'action': Action.CLEARS_PENALTY,
                        'suits': [
                            Suit.WEATHER
                        ]
                    }
                ]
            }
        },
        Name.UNICORN: {
            'suit': Suit.BEAST,
            'base_strength': 9,
            'bonus': {
                'or': [
                    {
                        'action': Action.WITH_CARD,
                        'value': 30,
                        'cards': [
                            Name.PRINCESS
                        ]
                    },
                    {
                        'action': Action.WITH_CARD,
                        'value': 15,
                        'cards': [
                            Name.ELEMENTAL_ENCHANTRESS,
                            Name.EMPRESS,
                            Name.QUEEN,
                        ]
                    }
                ]
            }
        },
        Name.WAR_DIRIGIBLE: {
            'suit': Suit.WEAPON,
            'base_strength': 25,
            'penalty': [
                {
                    'action': Action.BLANKED_UNLESS,
                    'suits': [
                        Suit.ARMY
                    ]
                },
                {
                    'action': Action.BLANKED_WITH,
                    'suits': [
                        Suit.WEATHER
                    ]
                },
            ]
        },
        Name.WARHORSE: {
            'suit': Suit.BEAST,
            'base_strength': 6,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 14,
                'suits': [
                    Suit.LEADER,
                    Suit.WIZARD
                ]
            }
        },
        Name.WARLOCK_LORD: {
            'suit': Suit.WIZARD,
            'base_strength': 25,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 10,
                'suits': [
                    Suit.LEADER,
                    Suit.WIZARD
                ]
            },
        },
        Name.WARSHIP: {
            'suit': Suit.WEAPON,
            'base_strength': 23,
            'bonus': {
                'action': Action.CLEARS_WORD_FROM_PENALTY,
                'word': Suit.ARMY,
                'suits': [
                    Suit.FLOOD
                ]
            },
            'penalty': {
                'action': Action.BLANKED_UNLESS,
                'suits': [
                    Suit.FLOOD
                ],
            }
        },
        Name.WATER_ELEMENTAL: {
            'suit': Suit.FLOOD,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.FLOOD
                ]
            }
        },
        Name.WHIRLWIND: {
            'suit': Suit.WEATHER,
            'base_strength': 13,
            'bonus': {
                'action': Action.WITH_CARD_AND_EITHER,
                'value': 40,
                'cards': [
                    Name.RAINSTORM
                ],
                'either': [
                    Name.BLIZZARD,
                    Name.GREAT_FLOOD
                ]
            }
        },
        Name.WILDFIRE: {
            'suit': Suit.FLAME,
            'base_strength': 40,
            'penalty': {
                'action': Action.BLANKS,
                'targets': {},
                'excludes': {
                    'suits': [
                        Suit.ARTIFACT,
                        Suit.FLAME,
                        Suit.WEAPON,
                        Suit.WEATHER,
                        Suit.WIZARD,
                    ],
                    'cards': [
                        Name.GREAT_FLOOD,
                        Name.DRAGON,
                        Name.ISLAND,
                        Name.MOUNTAIN,
                        Name.UNICORN,
                    ]
                }
            }
        },
        Name.WORLD_TREE: {
            'suit': Suit.ARTIFACT,
            'base_strength': 2,
            'bonus': {
                'action': Action.EACH_ACTIVE_CARD_IS_FROM_DIFFERENT_SUIT,
                'value': 50
            },
        },
    }
