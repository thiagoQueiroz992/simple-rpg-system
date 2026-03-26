from objects.characters import Enemy

def spawn_enemy(name: str, health: int, attack: int) -> Enemy:
    enemy = Enemy(name, health, attack)
    return enemy