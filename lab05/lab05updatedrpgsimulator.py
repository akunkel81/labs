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


class Weapon(Item):
    rarity_modifiers = {
        'common': 1.0,
        'uncommon': 1.0,
        'epic': 1.0,
        'legendary': 1.15
    }

    def __init__(self, name, damage, type, description='', rarity='common'):
        super().__init__(name, rarity=rarity)
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
        super().__init__(name, description=description, rarity=rarity)
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


class Clothes(Item):
    def __init__(self, name, description='', armor=0, rarity='common'):
        super().__init__(name, description, rarity)
        self.armor = armor
        self.active = False

    def equip(self):
        self.active = True
        print(f'{self.name} is equipped.')

    def use(self):
        if not self._ownership:
            return 'This item has been thrown away'
        if not self.active:
            return ''
        return f'{self.name} is used, providing {self.armor} armor'

    def __str__(self):
        return f'Clothes: {self.name}, Armor: {self.armor}, Rarity: {self.rarity}'


class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, rarity='common'):
        super().__init__(name, rarity=rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    @classmethod
    def from_ability(cls, name, owner, potion_type):
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


class Inventory:
    def __init__(self, owner=None):
        self.items = []
        self.owner = owner

    def add_item(self, item):
        item._ownership = self.owner
        self.items.append(item)

    def remove_item(self, item):
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
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

master_sword= SingleHandedWeapon(name='Master Sword', rarity='legendary', damage=300, type='sword')
muramasa = DoubleHandedWeapon(name='Muramasa', rarity='legendary', damage=580, type='katana')
gungnir= Pike(name='Gungnir', rarity='legendary', damage=290, type='spear')
belthronding = RangedWeapon(name='Belthronding', rarity='legendary', damage=500, type='bow')
round_shield = Shield(name='Round Shield', rarity= 'common', defense=10 )
broken_pot_lid = Shield(name='Broken Pot Lid', rarity= 'common', defense =1)

beleg_backpack = Inventory(owner='Beleg')
beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(round_shield)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.drop_item(broken_pot_lid)

attack_potion = Potion.from_ability(name='Atk Potion Temp', owner='Beleg', potion_type='attack')
print(attack_potion.use())
print(attack_potion.use())

leather_jacket = Clothes(name='Leather Jacket', description='A stylish and protective jacket', armor=10, rarity='uncommon')
print(leather_jacket.pick_up('Beleg'))
print(leather_jacket.description)
leather_jacket.equip()
print(leather_jacket.use())
print(leather_jacket.throw_away())
print(leather_jacket.use())

beleg_backpack.view()

if master_sword in beleg_backpack:
    master_sword.equip()
master_sword.use()
