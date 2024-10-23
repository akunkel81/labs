import json

class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = None

    def pick_up(self, character: str):
        self._ownership = character
        return f'{self.name} is now owned by {character}'

    def throw_away(self):
        self._ownership = None
        return f'{self.name} has been thrown away'

    def use(self):
        if not self._ownership:
            return ''
        return f'{self.name} is used'

    def __str__(self):
        if self.rarity == 'legendary':
            return f"""
    ⚔️ [LEGENDARY ITEM] ⚔️
    {self.name} - {self.description}
    (Rarity: {self.rarity})
    "Shines with a divine glow!"
    """
        return f'{self.name} - {self.description} (Rarity: {self.rarity})'

    def to_json(self):
        """Convert item to a JSON-encodable dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'ownership': self._ownership
        }

    @classmethod
    def from_json(cls, data):
        """Create an item instance from JSON data."""
        return cls(name=data['name'], description=data['description'], rarity=data['rarity'])

class Weapon(Item):
    rarity_modifiers = {
        'common': 1.0,
        'uncommon': 1.0,
        'epic': 1.0,
        'legendary': 1.15
    }

    def __init__(self, name, damage, type, description='', rarity='common'):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.type = type
        self.active = False

    def equip(self):
        self.active = True
        print(f'{self.name} is equipped.')

    def attack_move(self):
        return ''

    def use(self):
        if not self._ownership or not self.active:
            return ''
        attack_power = self.damage * Weapon.rarity_modifiers[self.rarity]
        return f'{self.attack_move()} {self.name} is used, dealing {attack_power} damage'

    def to_json(self):
        """Convert Weapon instance to JSON-encodable dictionary."""
        return {
            'class': self.__class__.__name__,
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'damage': self.damage,
            'type': self.type,
            'active': self.active
        }

    @classmethod
    def from_json(cls, data):
        """
        Create a Weapon (or subclass) instance from JSON data.

        Args:
            data (dict): JSON-encoded weapon data.

        Returns:
            Weapon: A new Weapon or subclass instance.
        """
        return cls(
            name=data['name'],
            damage=data['damage'],
            type=data['type'],
            description=data.get('description', ''),
            rarity=data.get('rarity', 'common')
        )

class SingleHandedWeapon(Weapon):
    def attack_move(self):
        return f'{self._ownership} slashes with {self.name}'

class DoubleHandedWeapon(Weapon):
    def attack_move(self):
        return f'{self._ownership} spins {self.name} powerfully'

class Pike(Weapon):
    def attack_move(self):
        return f'{self._ownership} thrusts forward with {self.name}'

class RangedWeapon(Weapon):
    def attack_move(self):
        return f'{self._ownership} shoots an arrow from {self.name}'

class Shield(Item):
    rarity_modifiers = {
        'common': 1.0,
        'uncommon': 1.0,
        'epic': 1.0,
        'legendary': 1.10
    }

    def __init__(self, name, description='', defense=0, broken=False, rarity='common'):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
        self.active = False

    def equip(self):
        self.active = True
        print(f'{self.name} is equipped.')

    def use(self):
        if not self._ownership or not self.active:
            return ''
        defense_modifier = 0.5 if self.broken else 1.0
        defense_power = self.defense * Shield.rarity_modifiers[self.rarity] * defense_modifier
        return f'{self.name} is used, blocking {defense_power} damage'

    def to_json(self):
        """Convert Shield instance to JSON-encodable dictionary."""
        return {
            'class': self.__class__.__name__,
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'defense': self.defense,
            'broken': self.broken,
            'active': self.active
        }

    @classmethod
    def from_json(cls, data):
        """
        Create a Shield instance from JSON data.

        Args:
            data (dict): JSON-encoded shield data.

        Returns:
            Shield: A new Shield instance.
        """
        shield = cls(
            name=data['name'],
            description=data.get('description', ''),
            defense=data.get('defense', 0),
            broken=data.get('broken', False),
            rarity=data.get('rarity', 'common')
        )
        shield.active = data.get('active', False)
        return shield


class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, rarity='common'):
        super().__init__(name, rarity=rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        """Create a potion using predefined attributes."""
        potion = cls(name, potion_type, 50, 30, rarity='common')
        potion._ownership = owner
        return potion

    def use(self):
        if not self._ownership:
            return 'This item has been thrown away'
        if self.empty:
            return ''
        self.empty = True
        if self.effective_time > 0:
            return f'{self._ownership} used {self.name}, and {self.potion_type} increased by {self.value} for {self.effective_time}s\n{self.potion_type.capitalize()} potion has been consumed'
        else:
            return f'{self._ownership} consumed {self.name}\n{self.potion_type.capitalize()} potion has been consumed'

    def to_json(self):
        """Convert Potion instance to JSON-encodable dictionary."""
        return {
            'class': self.__class__.__name__,
            'name': self.name,
            'potion_type': self.potion_type,
            'value': self.value,
            'effective_time': self.effective_time,
            'rarity': self.rarity,
            'empty': self.empty
        }

    @classmethod
    def from_json(cls, data):
        """
        Create a Potion instance from JSON data.

        Args:
            data (dict): JSON-encoded potion data.

        Returns:
            Potion: A new Potion instance.
        """
        potion = cls(
            name=data['name'],
            potion_type=data['potion_type'],
            value=data['value'],
            effective_time=data['effective_time'],
            rarity=data['rarity']
        )
        potion.empty = data.get('empty', False)
        return potion

class Inventory:
    def __init__(self, owner=None):
        """Initialize the inventory with an owner and an empty item list."""
        self.items = []
        self.owner = owner

    def add_item(self, item):
        """Add an item to the inventory and assign ownership."""
        item._ownership = self.owner
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the inventory."""
        if item in self.items:
            item._ownership = None
            self.items.remove(item)

    def drop_item(self, item):
        """Drop an item from the inventory."""
        if item in self.items:
            item._ownership = None  # Reset ownership
            self.items.remove(item)
            print(f'{item.name} has been dropped by {self.owner}.')
        else:
            print(f'{item.name} is not in the inventory.')

    def view(self, item_type=None):
        if item_type:
            filtered_items = [item for item in self.items if isinstance(item, item_type)]
            for item in filtered_items:
                print(item.description)
        else:
            for item in self.items:
                print(item)


    def __iter__(self):
        """Allow iteration over the inventory's items."""
        return iter(self.items)

    def __contains__(self, item):
        """Check if an item is in the inventory."""
        return item in self.items

    def to_json(self):
        """
        Converts the inventory and all its items into a JSON-encodable dictionary.
        """
        return {
            'owner': self.owner,
            'items': [item.to_json() for item in self.items]
        }

    @classmethod
    def from_json(cls, data):
        """
        Reconstructs an Inventory instance from JSON data.

        Args:
            data (dict): JSON-encoded inventory data.

        Returns:
            Inventory: A new Inventory object populated with items.
        """
        inventory = cls(data['owner'])
        for item_data in data['items']:
            item_class = globals()[item_data['class']]
            item = item_class.from_json(item_data)
            inventory.add_item(item)
        return inventory

    def save_to_file(self, filename):
        """Save the inventory to a file in JSON format."""
        with open(filename, 'w') as f:
            json.dump(self.to_json(), f, cls=CustomEncoder)

    @classmethod
    def load_from_file(cls, filename):
        """Load the inventory from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
            return cls.from_json(data)


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        return super().default(obj)

import json

# Example of creating various items
master_sword = SingleHandedWeapon(name='Master Sword', rarity='legendary', damage=300, type='sword')
muramasa = DoubleHandedWeapon(name='Muramasa', rarity='legendary', damage=580, type='katana')
gungnir = Pike(name='Gungnir', rarity='legendary', damage=290, type='spear')
belthronding = RangedWeapon(name='Belthronding', rarity='legendary', damage=500, type='bow')

round_shield = Shield(name='Round Shield', description='A sturdy wooden shield', defense=10, rarity='common')
broken_pot_lid = Shield(name='Broken Pot Lid', defense=1, broken=True, rarity='common')

attack_potion = Potion.from_ability(name='Atk Potion Temp', owner='Beleg', potion_type='attack')
healing_potion = Potion(name='Healing Potion', potion_type='healing', value=50, effective_time=0, rarity='uncommon')

# Create and populate an inventory
beleg_backpack = Inventory(owner='Beleg')
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(round_shield)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(attack_potion)
beleg_backpack.add_item(healing_potion)

print("Initial Inventory:")
beleg_backpack.view()

if master_sword in beleg_backpack:
    master_sword.equip()
    print(master_sword.use())

if round_shield in beleg_backpack:
    round_shield.equip()
    print(round_shield.use())


print(attack_potion.use())
print(attack_potion.use())

beleg_backpack.save_to_file('full_inventory.json')
print("Inventory saved to 'full_inventory.json'")


loaded_inventory = Inventory.load_from_file('full_inventory.json')
print("Loaded Inventory:")

loaded_inventory.view()

loaded_inventory.drop_item(broken_pot_lid)

loaded_inventory.save_to_file('modified_inventory.json')
print("Modified inventory saved to 'modified_inventory.json'")
