import random
from ..game import Game


class BlackrockShowdownBrawl(Game):
	"""
	Showdown at Blackrock Mountain

	These two epic bosses of Blackrock Mountain are
	settling things once and for all... with your help!
	"""

	NEFARIAN_DECK = ([
		"BRMA14_3",
		"BRMA14_5",
		"BRMA14_7",
		"BRMA14_9",
		"BRMA10_5H", "BRMA10_5H", "BRMA10_5H",
		"BRMC_83", "BRMC_83",
		"BRMC_84", "BRMC_84",
		"BRMC_86",
		"BRMC_88", "BRMC_88",
		"BRMC_97",
		"BRMC_98",
		"BRM_018", "BRM_018",
		"BRM_029",
		"BRM_031",
		"BRM_033", "BRM_033", "BRM_033",
		"BRM_034", "BRM_034",
		"EX1_303", "EX1_303",
		"EX1_562",
		"EX1_570", "EX1_570",
	], "TBA01_4")

	RAGNAROS_DECK = ([
		"BRMA_01", "BRMA_01",
		"BRMC_85",
		"BRMC_87",
		"BRMC_89", "BRMC_89",
		"BRMC_90", "BRMC_90", "BRMC_90",
		"BRMC_91", "BRMC_91",
		"BRMC_92",
		"BRMC_95",
		"BRMC_95h", "BRMC_95h",
		"BRMC_96",
		"BRMC_99",
		"BRMC_100", "BRMC_100",
		"CS2_032", "CS2_032",
		"CS2_042", "CS2_042",
		"EX1_241", "EX1_241",
		"EX1_249",
		"EX1_319", "EX1_319",
		"EX1_620", "EX1_620",
	], "TBA01_1")

	@classmethod
	def new_game(cls, *players):
		decks = random.sample((cls.NEFARIAN_DECK, cls.RAGNAROS_DECK), 2)
		for player, deck in zip(players, decks):
			player.prepare_deck(deck[0], hero=deck[1])
		return cls(players)

	def prepare(self):
		super().prepare()
		for player in self.players:
			if player.hero.id == self.NEFARIAN_DECK[1]:
				player.max_mana = 4
				player.hero.armor = 30
			else:
				player.summon("BRMC_94")  # Sulfuras
