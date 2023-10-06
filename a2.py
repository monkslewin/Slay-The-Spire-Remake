
from a2_support import *


class Card():
    """
    Class for all cards. Serves as an abstract
    class for other classes to inherit from later
    """
    def __init__(self):
        """
        Initialises the instance of 
        the Card class

        """
        self._damage = 0
        self._block = 0
        self._energy_cost = 1
        self._status_modifiers = {}
        self._name = 'Card'
        self._description = 'A card.'
        self._requires_target = True

    def get_damage_amount(self) -> int:
        """
        This method returns the damage amount done
        by the card

        Returns:
            int: damage amount 

        Example:
        >>> card = Card()
        >>> card.get_damage_amount()
        0
        """
        return int(self._damage)
    
    def get_block(self) -> int:
        """
        This method returns the amount of
        block a card has

        Returns:
            int: block amount 

        Example:
        >>> card = Card()
        >>> card.get_block()
        0
        """
        return int(self._block)

    def get_energy_cost(self) -> int:
        """
        This method returns the energy cost
        of a card

        Returns:
            int: the energy cost of the card

        Example:
        >>> card = Card()
        >>> card.get_energy_cost()
        1
        """
        return self._energy_cost

    def get_status_modifiers(self) -> dict[str, int]:
        """
        This method returns the status modifiers 
        of a card

        Returns: 
            dict: A dictionary containing the status
                  modifiers 

        Example:
        >>> card = Card()
        >>> card.get_status_modifiers()
        {'weak': 1, 'vulnerable': 2}
        """
        return self._status_modifiers
    
    def get_name(self) -> str:
        """
        This method returns the name of the 

        Returns:
            str: the name of the card

        Example:
        >>> card = Card()
        >>> card.get_name()
        'Card'
        """
        return self._name

    def get_description(self) -> str:
        """
        Returns the description of a card

        Returns:
            str: small description of a card

        Example:
        >>> card = Card()
        >>> card.get_description()
        'A card.'
        """
        return self._description
    
    def requires_target(self) -> bool:
        """
        Returns whether a card requires a target when played

        Returns:
            bool: value of whether a target is required 

        Example:
        >>> card = Card()
        >>> card.requires_target()
        True
        """
        return self._requires_target
    
    def __str__(self) -> str:
        """
        Returns a string representation of the card
        with its name and description

        Returns:
            str: a representation of the card 
        
        Examples:
        >>> card = Card()
        >>> card.__str__()
        'Card: A card.'
        """
        return f"{self._name}: {self._description}"
    
    def __repr__(self) -> str:
        """
        Returns the exact command required to create an 
        instance of the Card class

        Returns:
            str: the exact command to create an 
            instance of the class

        Example:
        >>> card = Card()
        >>> card.__repr__()
        "Card()"
        """
        return f"{self._name}()"
        
class Strike(Card):
    """
    Inherits from the Card class. Class
    for the strike card

    """
    def __init__(self):
        """
        Initialises an instance of the Strike
        class

        Example:
        >>> strike = Strike()
        >>> strike.get_description()
        'Deal 6 damage.'
        >>> strike.get_name()
        'Strike'
        >>> Strike.get_damage()
        6
        """
        self._damage = 6
        self._block = 0
        self._energy_cost = 1
        self._status_modifiers = {}
        self._name = 'Strike'
        self._description = 'Deal 6 damage.'
        self._requires_target = True

class Defend(Card):
    """
    Class for the Defend card which 
    inherits from the Card class

    """
    def __init__(self):
        """
        Initialises an instance of the Defend
        class

        Example:
        >>> defend = Defend()
        >>> defend.get_name()
        'Defend'
        >>> defend.get_block()
        5
        """
        self._damage = 0
        self._block = 5
        self._energy_cost = 1
        self._status_modifiers = {}
        self._name = 'Defend'
        self._description = 'Gain 5 block.'
        self._requires_target = False

class Bash(Card):
    """
    Class for the Bash class which
    inherits from Card

    """
    def __init__(self):
        """
        Initialises an instance of the 
        Bash class

        Example:
        >>> bash = Bash()
        >>> bash.get_name()
        'Bash'
        >>> bash.get_status_modifiers()
        {}
        """
        self._damage = 7
        self._block = 5
        self._energy_cost = 2
        self._status_modifiers = {}
        self._name = 'Bash'
        self._description = 'Deal 7 damage. Gain 5 block.'
        self._requires_target = True

class Neutralize(Card):
    """
    A class for the Neutralize class.
    This class inherits all methods
    from Card


    """
    def __init__(self):
        """
        Initialises an instance of the NeutraliZe
        class

        >>> neutralize = Neutralize()
        >>> neutralize.get_name()
        'Neutralize'
        >>> neutralize.get_damage()
        3
        """
        self._damage = 3
        self._block = 0
        self._energy_cost = 0
        self._status_modifiers = {'weak': 1, 'vulnerable': 2}
        self._name = 'Neutralize'
        self._description = \
            'Deal 3 damage. Apply 1 weak. Apply 2 vulnerable.'
        self._requires_target = True
    
class Survivor(Card):
    """
    A class for the survivor card that
    inherits all methods from the 
    Card class

    Args:
        Card (_type_): _description_
    """
    def __init__(self):
        """
        Initialises an instance of the 
        Surivor class

        Example:
        >>> surivor = Surivor()
        >>> survivor.get_name()
        'Survivor'
        >>> survivor.get_block()
        8
        """
        self._damage = 0
        self._block = 8
        self._energy_cost = 1
        self._status_modifiers = {'strength' : 1}
        self._name = 'Survivor'
        self._description = 'Gain 8 block and 1 strength.'
        self._requires_target = False

class Entity():
    """
    Class for all entity's within the program.
    This is an abstract class

    """
    def __init__(self, max_hp: int) -> None:
        """
        Initialises an instance of the Entity class 
        and requires the max HP of the entity 

        Args:
            max_hp (int): the maximum hp an entity can have

        """
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._block = 0
        self._strength = 0
        self._weak = 0
        self._vulnerable = 0
    
    def get_hp(self) -> int:
        """
        A method that returns the hp of an entity

        Returns:
            int: the current hp of the entity

        Example:
        >>> entity = Entity(80)
        >>> get_hp(Entity)
        80
        """
        return self._current_hp
    
    def get_max_hp(self):
        """
        This method returns the maximum hp of an entity

        Returns:
            _type_: the maximum hp an entity can have

        Example:
        >>> entity = Entity(70)
        >>> get_max_hp(Entity)
        70
        """
        return self._max_hp
    
    def get_block(self) -> int:
        """
        Returns the current block of an entity

        Returns:
            int: the current block of an entity
        
        Example:
        >>> entity = Entity(30)
        >>> entity.add_block(6)
        >>> get_block(Entity)
        6
        """
        return self._block
    
    def get_strength(self) -> int:
        """
        Returns the current strength of an entity

        Returns:
            int: the current strength of an entity
        
        Example:
        >>> entity = Entity(20)
        >>> entity.add_strength(3)
        >>> entity.get_strength()
        3
        """
        return self._strength

    def get_weak(self) -> int:
        """
        Returns the current weak value of the entity

        Returns:
            int: the weak value of an entity
        
        Example:
        >>> entity = Entity(30)
        entity.add_weak(3)
        >>> entity.get_weak()
        3
        """
        return self._weak
    
    def get_vulnerable(self) -> int:
        """
        Returns the vulnerable value of the entity

        Returns:
            int: the vulnerable value of the entity
        
        Example:
        >>> entity = Entity()
        >>> entity.add_vulnerable(4)
        >>> entity.get_vulnerable()
        4
        """
        return self._vulnerable

    def get_name(self) -> str:
        """
        Returns the name of the Entity in string format

        Returns:
            str: returns the name of the entity

        Example:
        >>> entity = Entity(30)
        >>> entity.get_name()
        'Entity' 
        """
        return type(self).__name__
        
    def reduce_hp(self, amount: int) -> None:
        """
        A method for reducing an Entity's hp

        Args:
            amount (int): the amount the current hp 
            is to be reduced by 
        
        Example:
        >>> entity = Entity(70)
        >>> entity.reduce_hp(30)
        >>> entity.get_hp()
        40
        """
        # Determines block amount remaining
        self._block = self._block - amount 
        if self._block <= 0:
            # If the user's block is below 0, then its distance
            # from zero is the amount needed to take from
            # the user's health
            self._current_hp = self._current_hp - abs(self._block) 
            self._block = 0
        if self._current_hp < 0: # Ensures the hp cannot go below 0 
            self._current_hp = 0

    
    def is_defeated(self) -> bool:
        """
        Determines if an Entity is defeated.
        It is defined as defeated once its 
        HP reaches 0 and below 

        Returns:
            bool: whethe the entity has HP remaining
        
        Example:
        >>> entity = Entity(30)
        >>> entity.reduce_hp(30)
        >>> entity.is_defeated()
        True
        
        """
        # the player is considered defeated if their
        # current HP is lower than 1
        if self._current_hp <= 0:
            return True
        return False
    
    def add_block(self, amount: int) -> None:
        """
        Adds a specified amount of block to the 
        Entity's current block

        Args:
            amount (int): the amount to be added 
            to an Entity's block current block
        
        Example:
        >>> entity = Entity(30)
        >>> entity.add_block(3)
        >>> entity.get_block()
        3
        """
        self._block = self._block + amount
    
    def add_strength(self, amount: int) -> None:
        """
        Adds a specified amount of strength to
        an entity's current strength

        Args:
            amount (int): the amount of block
            to be added
        
        Example:
        >>> entity = Entity(30)
        >>> entity.add_strength(5)
        >>> entity.get_strength()
        5
        """
        self._strength = self._strength + amount
    
    def add_weak(self, amount: int) -> None:
        """
        Adds a specified amount of strength to
        an entity's current strength

        Args:
            amount (int): the amount of strength to
            be added to the current strength
        
        Example:
        >>> entity = Entity(30)
        >>> entity.add_weak(4)
        >>> entity.get_weak()
        4
        """
        self._weak = self._weak + amount
    
    def add_vulnerable(self, amount: int) -> None:
        """
        Adds a specified amount of strength to
        an entity's current strength

        Args:
            amount (int): the amount of vulnerable
            to be added to the current vulnerable
        
        Example:
        >>> entity = Entity(40)
        >>> entity.add_vulnerable(8)
        >>> entity.get_vulnerable()
        8

        """
        self._vulnerable =  self._vulnerable + amount
    
    def new_turn(self) -> None:
        """
        This method resets the entity's block,
        and the decrements its weak and vulnerable

        Example:
        >>> entity = Entity(30)
        >>> entity.add_weak(5)
        >>> entity.add_block(5)
        >>> entity.add_vulnerable(5)
        >>> entity.new_turn()
        >>> entity.get_block()
        0
        >>> entity.get_vulnerable()
        4
        >>> entity.get_weak()
        4
        """
        self._block = 0
        # Control statements to prevent user's stats 
        # being negative
        if self._weak > 0:
            self._weak = self._weak - 1
        if self._vulnerable > 0:
            self._vulnerable = self._vulnerable - 1
    
    def __str__(self) -> str:
        """
        Returns a string representation of the 
        Entity object with its name, current HP
        and max HP

        Returns:
            str: the name, current HP and max HP 
            of the entity
        
        Example:
        >>> entity = Entity(20)
        >>> entity.reduce_hp(5)
        >>> entity.__str__()
        'Entity: 15/20'

        """
        return f"{self.get_name()}: {self._current_hp}/{self._max_hp} HP"

    def __repr__(self) -> str:
        """
        Returns a representation of the object, 
        which is in the form of a string which
        is the exact command required to create
        an instance of the object

        Returns:
            str: representation of the object
        
        Example:
        >>> entity = Entity(20)
        >>> entity.__repr__()
        'Entity(20)'

        """
        return f"{self.get_name()}({self._max_hp})"

class Player(Entity):
    """
    The Player class is a class for the 
    user's playable character. It inherits
    all methods from the Entity class

    """
    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """
        Initialises an instance of the Player class

        Args:
            max_hp (int): maximum HP a player can have
            cards (list[Card] | None, optional): list of cards
            the Player has 
        
        Example:
        >>> player = Player(20, [Strike, Defend])

        """
        super().__init__(max_hp)
        self._original_deck = cards
        self._user_energy = 3 
        self._player_discard_pile = []
        # Checks if the player has any cards
        if cards != None:
            self._player_deck = cards
        else:
            self._player_deck = []

        self._player_hand = []
    
    def get_energy(self) -> int:
        """
        Returns the energy a player has

        Returns:
            int: the amount of energy the 
            player has
        
        Example:
        >>> player = Player(30, [Strike, Defend])
        >>> player.get_energy()
        3

        """
        return self._user_energy

    def get_hand(self) -> list[Card]:
        """
        Returns the player's current hand

        Returns:
            list[Card]: cards that are in the 
            player's hand
        
        Example:
        >>> player = Player(30, [Strike, Defend])
        >>> player.get_hand()
        []
        """
        return self._player_hand

    def get_deck(self) -> list[Card]:
        """
        Returns the player's current deck

        Returns:
            list[Card]: player's deck of cards
            
        Example:
        >>> player = Player(30, [Strike, Defend])
        >>> player.get_deck()
        [Strike, Defend]
        """
        return self._player_deck
    
    def get_discarded(self) -> list[Card]:
        """
        Returns the player's discarded pile

        Returns:
            list[Card]: cards that have been discarded
        
        Example:
        >>> player = Player(80, [Strike])
        >>> player.get_discarded()
        []

        """
        return self._player_discard_pile
    
    def start_new_encounter(self) -> None:
        """
        Starts a new encounter for the player
        for when new monsters are presented

        Example:
        >>> player = Player(80, [Strike, Strike, Defend])
        >>> player.get_discarded()
        []
        >>> player.start_new_encounter()
        >>> player.get_discarded()
        [Strike, Strike, Defend]
        """
        self._player_deck.extend(self._player_discard_pile)
        self._player_discard_pile = []

    
    def end_turn(self) -> None:
        """
        Method for when the user turn is ended.
        Resets the player's hand and adds all
        cards from the deck to the end of the
        discarded pile 

        Example:
        >>> player.new_turn()
        >>> player.end_turn()
        >>> player.get_discarded()
        [Strike, Strike]
        """
        self._player_discard_pile.extend(self._player_hand)
        self._player_hand = []

    def new_turn(self) -> None:
        """
        Sets it to be a new turn for the user.
        This resets the necessary stats so the
        user can play cards (replenish energy
        and draw new set of cards)

        example:
        >>> player = Player(90,  
        [Strike(), Strike(), Strike(), 
        Defend(), Defend(), Defend(), Bash()])
        >>> print(player.get_hand())
        []
        >>> player.new_turn()
        >>> player.get_hand()
        [Strike(), Defend(), Strike(), Strike(), Bash()]
        
        """
        super().new_turn()
        self._user_energy = 3
        # Every new turn a new set of cards is given to the player
        draw_cards(self._player_deck, 
                   self._player_hand, self._player_discard_pile)
    
    def play_card(self, card_name: str) -> Card | None:
        """
        The method for playing cards. This takes in a 
        card to be played and then ensures the user
        has enough energy to play it. It is then taken 
        from their hand and to the end of their discard 
        pile

        Args:
            card_name (str): name of card being played

        Returns:
            Card: returns the card the user 
            attempted to play
            None: returns None if the card was not found
            or the ser did not have enough energy
        
        >>> player = Player(80,
        [Strike(), Strike(), Strike(), 
        Defend(), Defend(), Defend(), Bash()])
        >>> player.new_turn()
        >>> player.play_card('Bash')
        Bash()
        """
        enum = enumerate(self._player_hand)
        # Loops until the user's played card is found in their hand
        for index, card in enum:
            if card.get_name() == card_name:
                # Ensures user has enough energy to play card
                if card.get_energy_cost() <= self._user_energy:
                    self._player_hand.pop(index) # Removes card from hand
                    self._user_energy = \
                        self._user_energy - card.get_energy_cost()
                    self._player_discard_pile.append(card)
                    return card
    
    def __repr__(self) -> str:
        """
        Creates a string representation
        of the player

        Returns:
            str: exact command required to create 
            an identical instance of this player
        """
        return f"{self.get_name()}({self._max_hp}, {self._original_deck})"


class IronClad(Player):
    """
    The ironclad class is for the IronClad
    type of player. This inherits from the
    Player class

    """
    def __init__(self):
        super().__init__(80)
        self._player_deck = [Strike(), Strike(), Strike(), Strike(), Strike(), 
                            Defend(), Defend(), Defend(), Defend(), Bash()]
    
    def __repr__(self) -> str:
        """
        returns a string representation of the 
        IronClad class which is the exact command
        required to create an identical instance 

        Returns:
            str: representation of IronClad instance
        
        Example:
        >>> player = Ironclad()
        >>> player.__repr__()
        'Ironclad()'
        """
        return f"{self.get_name()}()"
        
class Silent(Player):
    """
    The ironclad class is for the IronClad
    type of player. This inherits from the
    Player class

    """
    def __init__(self):
        super().__init__(70)
        self._player_deck = [Strike(), Strike(), Strike(), Strike(), Strike(),
                              Defend(), Defend(), Defend(), Defend(), Defend(), 
                              Neutralize(), Survivor()]
    
    def __repr__(self) -> str:
        """
        returns a string representation of the 
        Silent class which is the exact command
        required to create an identical instance 

        Returns:
            str: representation of IronClad instance
        
        Example:
        >>> player = Silent()
        >>> player.__repr__()
        'Silent()'

        """
        return f"{self.get_name()}()"
    
class Monster(Entity):
    """
    Abstract class for all monsters
    within the game
    """
    _id_counter = 0
    def __init__(self, max_hp: int) -> None:
        """
        Initialises an instance of the 
        monster class

        Args:
            max_hp (int): maximum HP the monster
            can have

        """
        super().__init__(max_hp)
        self._monster_id = Monster._id_counter
        # Every new monster recieves a unique ID 
        Monster._id_counter = Monster._id_counter + 1
    
    def get_id(self) -> int:
        """
        Returns the unique ID of a monster

        Returns:
            int: the ID of the instance
        
        Example:
        >>> monster1 = Monster(40)
        >>> monster2 = Monster(30)
        >>> monster1.get_id()
        0
        >>> monster2.get_id()
        1
        """
        return self._monster_id 

    def action(self) -> dict[str, int]:
        """
        returns the action a monster can perform

        Raises:
            NotImplementedError: Error for this 
            method not being implemented

        Returns:
            dict[str, int]: Dictionary of the monster's 
            actions

        Example:
        >>> monster = Monster(30)
        >>> monster.action()
        NotImplementedError

        """
        raise NotImplementedError

class Louse(Monster):
    """
    Class for the Louse monster type.
    This inherits all methods from the 
    Monster class

    """
    def __init__(self, max_hp):
        super().__init__(max_hp)
        self._damage = random_louse_amount()

    def action(self) -> dict[str, int]:
        """
        Method for summarising the monster's
        actions

        Returns:
            dict[str, int]: actions performed by Louse
        
        Example:
        >>> monster = Louse(30)
        >>> monster.action()
        {'damage': 5}
        """
        return {'damage': self._damage}

class Cultist(Monster):
    """
    Class for the Cultist monster type.
    This inherits all methods from the 
    Monster class

    """
    def __init__(self, max_hp):
        super().__init__(max_hp)
        self._damage = 0
        self._weak = 0
        self._calls = 0
    
    def action(self) -> dict[str, int]:
        """
        method for summarising the monster's
        actions

        Returns:
            dict[str, int]: Cultist's actions
        
        Example:
        >>> monster = Cultist(30)
        >>> monster.action()
        >>> monster.action()
        {'damage': 8, 'weak': 1}

        """
        # Handles first time action is called
        if self._calls == 0:
            self._calls += 1
            return {'damage': self._damage, 'weak': self._weak}
        
        # Determines if the number of calls is even
        if self._calls % 2 != 0:
            self._weak = 1
        else:
            self._weak = 0

        self._damage = 6 + self._calls
        self._calls = self._calls + 1
        return {'damage': self._damage, 'weak': self._weak}

class JawWorm(Monster):
    """
    Class for the JawWorm monster type.
    This inherits all methods from the 
    Monster class
    """
    def __init__(self, max_hp: int) -> None:
        super().__init__(max_hp)
        self._damage = 0 

    def action(self) -> dict[str, int]:
        """
        method for summarising the monster's
        actions

        Returns:
            dict[str, int]: actions performed by JawWorm
        
        Example:
        >>> monster = JawWorm(30)
        >>> monster.reduce_hp(11)
        >>> monster.action()
        {'damage': 5}

        """

        self._difference_in_hp = (self._max_hp - self._current_hp) / 2

        
        if self._difference_in_hp.is_integer() != True:
            # If the difference in HP of the JawWorm is 
            # not divisible by 2, then it must be rounded
            # up and down accordingly 
            self._block = int(self._difference_in_hp + 0.5)
            self._damage= int(self._difference_in_hp - 0.5)
        else:
            self._block = int(self._difference_in_hp)
            self._damage = int(self._difference_in_hp)

        return {'damage': self._damage}

class Encounter():
    """
    This class is for all encounters the user
    will face whilst playing the game
    """
    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """
        Initialises an instance of the encounter class

        Args:
            player: the current player instance
            monsters: list of tuples of monsters.
            Each tuple contains its name and ID 
        
        """
        self._monster = []
        self._monster_ids = []
        self._player = player
        for monster in monsters:
            if monster[0] == 'Louse':
                self._monster.append(Louse(monster[1]))
            elif monster[0] == 'JawWorm':
                self._monster.append(JawWorm(monster[1]))
            elif monster[0] == 'Cultist':
                self._monster.append(Cultist([monster[1]]))
        for creatures in self._monster:
            existing_monster_id = creatures.get_id()
            self._monster_ids.append(existing_monster_id)

        self._player.start_new_encounter()
        self.start_new_turn()
    
    def get_player(self) -> Player:
        """
        Returns the current player instance

        Returns:
            Player instance
        
        Example:
        >>> encounter = Encounter(Ironclad(), [(JawWorm, 0)])
        >>> encounter.get_player()
        IronClad()
        """
        return self._player

    def get_monsters(self) -> list[Monster]:
        """
        Returns the list of monsters
        active within the encounter


        Returns:
            List of monsters within encounter
        
        Example:
        >>> encounter = encounter = Encounter(Ironclad(), [(JawWorm, 0)])
        >>> encounter.get_monsters()
        >>> [('JawWorm', 0)]
        """
        return self._monster

    def start_new_turn(self) -> None:
        """
        Method for starting a new turn for the user.
        This sets it to being the player's turn
        and calls the new_turn() method on the 
        current player instance

        """
        self._player_turn = True
        self._player.new_turn()
    
    def end_player_turn(self) -> None:
        """
        Method for ending the player's turn.
        This sets it to no longer being the player's
        turn
        """
        self._player_turn = False
        self._player.end_turn()

        # Lets all monsters in the encounter
        # have their turn
        for creatures in self._monster:
            creatures.new_turn()

    def is_active(self) -> bool:
        """
        Method for determining if the encounter 
        is still active

        Example:
        >>> current_encounter.is_active()
        True
        
        """
        if len(self._monster) != 0:
            return True
        else:
            return False
        
    def player_apply_card(
            self, card_name: str, target_id: int | None = None) -> bool:
        """
        Method for when the player applies a card.
        Ensures all necessary criteria for applying
        a card have been satisfied 

        Args:
            card_name (str): Name of card being applied
            target_id (int | None, optional): ID of monster
            being targetted by user's move

        Returns:
            bool: if the card application was valid
        
        Example:
        >>> encounter.player_apply_card('Destroy', 5)
        False
        """
        self._card_valid = True
        self._target_monster = None

        # Checks if the card is in the player's hand
        for cards in self._player.get_hand():
            if card_name == cards.get_name():
                self._card_valid = True
                self._current_card = cards
                break
            else:
                self._card_valid = False
        

        if self._card_valid == False or self._player_turn == False:
            return False
        elif self._current_card.requires_target() == True:
            if target_id == None:
                return False
            # Determines the monster the user's attack is targetting
            for creatures in self._monster_ids:
                if target_id == creatures:
                    self._target_monster = creatures
            if self._target_monster == None:
                return False
            
        if self._player.get_energy() < self._current_card.get_energy_cost():
            return False
    
        self._player.add_block(self._current_card.get_block())
        self._dict_of_modifiers = self._current_card.get_status_modifiers()

        if 'strength' in self._current_card.get_status_modifiers():
            self._player.add_strength(
                self._current_card.get_status_modifiers().get('strength'))
        
        # Determine targetted monster
        if self._target_monster != None:
            for monsters in self._monster:
                if self._target_monster == monsters.get_id():
                    self._targetted = monsters
            
            if 'weak' in self._current_card.get_status_modifiers():
                self._targetted.add_weak(
                    self._current_card.get_status_modifiers().get('weak'))

            if 'vulnerable' in self._current_card.get_status_modifiers():
                self._targetted.add_vulnerable(
                self._current_card.get_status_modifiers().get('vulnerable'))

            # calculates damage applied to the player
            self._damage = self._current_card.get_damage_amount()
            if self._targetted.get_vulnerable() > 0:
                self._damage*1.25
            if self._player.get_weak() > 0:
                self._damage*0.75
            self._targetted.reduce_hp(int(self._damage))

        # After an attack determines if any monters have died
        for monster in self._monster:
            if monster.get_hp() <= 0:
                self._monster.remove(monster)

        self._player.play_card(self._current_card.get_name()) 
    
        
        return True
    
    def enemy_turn(self) -> None:
        """
        Method for handling the enemies in 
        the encounter's turn. This applies
        necessary damages and attributes to
        the player and monster

        Returns:
            returns False if it is
            the player's turn
        
        Example:
        >>> player = Ironclad(80)
        >>> monsters = [Louse(30)]
        >>> encounter = Encounter(player, monsters)
        >>> encounter.enemy_turn()
        >>> player.get_hp()
        75
        """
        if self._player_turn == True:
            return False
        
        # Applies all status modifies to user and applies damage
        for creatures in self._monster:
            self._moves = creatures.action()
            if 'weak' in self._moves:
                self._player.add_weak(self._moves.get('weak'))
            if 'vulnerable' in self._moves:
                self._player.add_weak(self._moves.get('vulnerable'))
            if 'damage' in self._moves:
                self._base_damage = self._moves.get('damage')
            if 'strength' in self._moves:
                creatures.add_strength(self._moves.get('strength'))
            if self._player.get_vulnerable() > 0:
                self._base_damage* 1.25
            if creatures.get_weak() > 0:
                self._base_damage*0.75
            if creatures.get_strength() > 0:
                self._base_damage = self._base_damage + creatures.get_strength()
            self._player.reduce_hp(int(self._base_damage))            
        self.start_new_turn()

def inspect_command(cards: str, player: Player):
    """
    Handles the user inspecting
    their deck or discard pile

    Args:
        cards: the pile being inspected
        player: the current player instance
    
    Example:
    >>> inspect_command('deck', player)
    [Strike(), Strike(), Defend()]
    """
    if cards == 'deck':
        print(f'\n{player.get_deck()}\n')
    elif cards == 'discard':
        print(f'\n{player.get_discarded()}\n')

def describe_command(card: Card, cards_possible: list[Card]):
    """
    Handles the user's move for describing
    a card

    Args:
        card: the card being described
        cards_possible: list of possible cards
    
    Example:
    >>> describe_command('Strike', cards_possible)
    'Strike: Deal 6 damage.'
    """
    # Loops to find specified card
    for cards in cards_possible:
        if card == cards.get_name():
                print(f'\n{cards.get_description()}\n')

def play_command(
    monster_found: bool, current_encounter: Encounter, 
    cards_possible: list[Card], player_move_seperated: list[str]):
    """
    Determines if the user attempt at playing a card is valid.
    If it is not, then an error message is displayed. Otherwise,
    the card is played

    Args:
        monster_found: if the targetted monster 
        exists within the encounter
        current_encounter: the encounter being played
        cards_possible: list of cards the 
        user can play
        player_move_seperated: list of the user's
        input splitup

    """
    try:
        for monster in current_encounter.get_monsters():
            if int(player_move_seperated[2]) == monster.get_id():
                monster_found = True
                if current_encounter.player_apply_card(
                    player_move_seperated[1], monster.get_id()) == False:
                    print(CARD_FAILURE_MESSAGE)
                    break
                display_encounter(current_encounter)
            if monster_found == False:
                print(CARD_FAILURE_MESSAGE)
                            
    except IndexError:
        card_found = False
        for card in cards_possible:
            if player_move_seperated[1] == card.get_name():
                card_found = True
                target = card.requires_target()
        if card_found == False:
            print(CARD_FAILURE_MESSAGE)
        elif target == True:
            print(CARD_FAILURE_MESSAGE)
        else:
            current_encounter.player_apply_card(
                player_move_seperated[1].strip(), None)
            display_encounter(current_encounter)

def execute_encounter(player: Player, 
                current_encounter: Encounter, cards_possible: list[Card]):
    """
    This function handles the user playing 
    moves 

    Args:
        player: The current player instance
        current_encounter: the monsters present
        cards_possible: list of cards the user can play

    Returns:
        None if the user's HP is below zero or below
    """
    while len(current_encounter.get_monsters()) != 0:
        if player.get_hp() > 0:
            player_move = input('Enter a move: ')
            player_move_seperated = player_move.split(' ')

            if player_move == 'end turn':
                current_encounter.end_player_turn()
                current_encounter.enemy_turn()

                if player.get_hp() > 0:
                    display_encounter(current_encounter)

            elif player_move_seperated[0] == 'inspect':
                inspect_command(player_move_seperated[1], player)

            elif player_move_seperated[0] == 'describe':
                describe_command(player_move_seperated[1], cards_possible)

            elif player_move_seperated[0] == 'play':
                monster_found = False
                play_command(
    monster_found, current_encounter, cards_possible, player_move_seperated)
        else:
            return None

def main():
    """
    This function is for the main loop of the 
    program. This handles all cases where the game
    may end (player dies, monsters die )
    """

    CARDS_POSSIBLE = [Strike(), Bash(), Neutralize(), Survivor(), Defend()]
    wanted_player = input('Enter a player type: ')
    if wanted_player == 'ironclad':
        player = IronClad()
    elif wanted_player == 'silent':
        player = Silent()
    game_file = input('Enter a game file: ')
    encounters = read_game_file(game_file)
    # Tracks number of encounters the user has won
    encounter_number = 0 

    while player.get_hp() > 0:
        # Loops til the user has won all encounters
        while encounter_number != len(encounters):
            print('New encounter!\n')
            current_encounter = Encounter(player, encounters[encounter_number])
            f'/n{display_encounter(current_encounter)}'
            encounter_number += 1

            execute_encounter(player, current_encounter, CARDS_POSSIBLE)
            # Checks if there are monsters remaining
            if len(current_encounter.get_monsters()) == 0:
                print(ENCOUNTER_WIN_MESSAGE)
        break

    if player.get_hp() <= 0:
        print(GAME_LOSE_MESSAGE)
        return
    
    print(GAME_WIN_MESSAGE)
    return

if __name__ == '__main__':
    main()