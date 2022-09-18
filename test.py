data={
        "001A": [
            [
                [
                    "9006:18-11-99"
                ]
            ]
        ],
        "001B": [
            [
                [
                    "9006:24-09-21"
                ],
                {
                    "t": "09:54:27.000"
                }
            ]
        ],
        "001D": [
            [
                [
                    "9999:23-03-05"
                ]
            ]
        ],
        "001U": [
            [
                [
                    "utf8"
                ]
            ]
        ],
        "002@": [
            [
                [
                    "Tw"
                ]
            ]
        ],
        "003@": [
            [
                [
                    "009023038"
                ]
            ]
        ],
        "008H": [
            [
                {
                    "a": "785100-5"
                },
                {
                    "b": "AW872"
                },
                {
                    "d": "Frei 129"
                },
                {
                    "e": "DE-Frei129"
                },
                {
                    "f": "PHBFR"
                }
            ]
        ],
        "009Q": [
            [
                {
                    "u": "http://www.ph-freiburg.de/bibliothek"
                },
                {
                    "z": "A"
                }
            ],
            [
                {
                    "u": "https://rds.ibs-bw.de/phfreiburg/opac/"
                },
                {
                    "z": "B"
                }
            ]
        ],
        "029@": [
            [
                {
                    "a": "Freiburg PH"
                },
                {
                    "4": "c"
                }
            ]
        ],
        "029A": [
            [
                {
                    "a": "Bibliothek der P\u00e4dagogischen Hochschule Freiburg/Breisgau"
                }
            ]
        ],
        "032P": [
            [
                {
                    "a": "Kunzenweg 21"
                },
                {
                    "b": "Freiburg/Breisgau"
                },
                {
                    "d": "DE"
                },
                {
                    "e": "79117"
                },
                {
                    "f": "Baden-W\u00fcrttemberg"
                },
                {
                    "i": "Mo-Fr 8.00-20.00, Sa-So 9.00-18.00"
                },
                {
                    "k": "7.89534"
                },
                {
                    "l": "47.98066"
                },
                {
                    "n": "08311000"
                },
                {
                    "p": "j"
                },
                {
                    "2": "S"
                }
            ]
        ],
        "035B": [
            [
                {
                    "a": "S"
                },
                {
                    "c": "j"
                },
                {
                    "d": "49"
                },
                {
                    "e": "761"
                },
                {
                    "f": "6 82-202"
                },
                {
                    "g": "49"
                },
                {
                    "h": "761"
                },
                {
                    "i": "6 82-564"
                },
                {
                    "k": "phb@ph-freiburg.de"
                }
            ],
            [
                {
                    "a": "W"
                },
                {
                    "b": "Leihstelle"
                },
                {
                    "c": "j"
                },
                {
                    "d": "49"
                },
                {
                    "e": "761"
                },
                {
                    "f": "682-202"
                },
                {
                    "k": "leihstelle.phb@ph-freiburg.de"
                }
            ],
            [
                {
                    "a": "W"
                },
                {
                    "b": "Fernleihe"
                },
                {
                    "c": "j"
                },
                {
                    "d": "49"
                },
                {
                    "e": "761"
                },
                {
                    "f": "682-560"
                },
                {
                    "k": "alv.phb@ph-freiburg.de"
                }
            ]
        ],
        "035E": [
            [
                {
                    "a": "H"
                },
                {
                    "b": "s"
                },
                {
                    "c": "0031"
                },
                {
                    "d": "SWB"
                },
                {
                    "f": "70"
                },
                {
                    "g": "02"
                },
                {
                    "h": "09"
                },
                {
                    "l": "CC0"
                }
            ]
        ],
        "035I": [
            [
                {
                    "a": "BAW"
                },
                {
                    "b": "\u00dcLV"
                },
                {
                    "c": "SWB"
                },
                {
                    "e": "k"
                },
                {
                    "g": "V"
                }
            ]
        ],
        "035O": [
            [
                {
                    "a": "ISIL DE-25; AUTO DE-624"
                }
            ]
        ],
        "035Q": [
            [
                {
                    "a": "j"
                }
            ]
        ]
    }
def for_data():
    for content in data:
        temp_dict = {k:v for subdict in content for k, v in subdict.items()} 
        if temp_dict.get("z", None) == 'A':
            print('homepage: ', temp_dict["u"])
        if temp_dict.get("z", None) == 'B':
            print('some other page: ', temp_dict["u"])

print(data[0][0][0])