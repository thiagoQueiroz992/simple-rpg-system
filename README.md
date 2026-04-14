# simple-rpg-system

- Para jogar, clone o repositório e execute o arquivo ``main.py`` na raiz.
- Obs: certifique-se de ter o Python 3, bem como a biblioteca ``rich`` instalada.

## O jogo
- Este é um jogo que funciona no terminal, que você joga através de perguntas que você responde escolhendo uma opção dentre as válidas. Cada opção te apresentará um valor numérico, que deve ser digitado para que a respectiva opção seja escolhida.
- Por ser um jogo de terminal, ele utiliza apenas recursos de texto e alguns efeitos de formatação.

## Começando
- Inicialmente você deverá digitar seu nome. O jogo irá sempre se referir a você através desse nome.
- Após isso você entrará no jogo, que te apresentará 4 opções:
  - __Andar (Walk)__ -> O jogador começa a caminhar pelo mundo. Ele pode encontrar ou inimigos ou baús.
  - __Inventário (Open Inventory)__ -> O jogador pode abrir seu inventário e ver seus itens, bem como usá-los ou destruí-los.
  - __Status (View Status)__ -> O jogador pode ver suas informações sobre vida, força de ataque e arma equipada.
  - __Sair (Quit Game)__ -> Sai do jogo.
- Inicialmente o jogador terá 100 pontos de vida, 20 de força de ataque e nenhuma arma equipada, apenas "sua mão e sua fé".
  - O jogador perderá vida a medida que for atacado por inimigos, e pode aumentar sua força de ataque equipando armas.

## Encontrando inimigos
- Após sair andando, o jogador tem 80% de chance de encontrar um inimigo.
- O inimigo pode ser qualquer um dentre os seguintes:
  - Zumbi (Zombie)
  - Vampiro (Vampire)
  - Esqueleto (Skeleton)
  - Witch (Bruxa)
  - Undead Knight (Cavaleiro morto-vivo)
- Cada inimigo possui quantidade de pontos de vida (HP) e força de ataque diferentes, variando até mesmo entre inimigos do mesmo tipo.
- Após encontrar um inimigo, o jogador pode escolher lutar ou fugir. Ao fugir, a luta é cancelada e o jogador volta às opções iniciais sem receber nada.
- Caso escolha lutar, começará uma batalha que ocorre em turnos:
  - Primeiro o jogador. Este pode escolher três opções em cada turno:
    - __Atacar (Attack)__ -> O jogador vai atacar o inimigo, causando a ele dano respectivo à sua força de ataque.
    - __Não fazer nada (Do nothing)__ -> O jogador não faz nada ao inimigo, apenas espera a vez do inimigo.
    - __Fugir (Flee)__ -> O jogador pode fugir da luta, cancelando-a sem nenhuma recompensa.
  - Após o jogador decidir o que fazer (exceto se ele escolher fugir), chega a vez do inimigo. Ele sempre vai atacar o jogador, dando ao jogador a respectiva quantidade de dano referente a sua força de ataque.
- Se a vida do jogador chegar a zero durante a batalha, o jogador é derrotado e deve respawnar caso queira continuar o jogo. Senão, ele pode escolher sair do jogo.
  - Após o respawn, a vida do jogador é redefinida para o valor inicial, mas ele não perde seus itens.
- Caso derrote o inimigo, ele poderá deixar um loot, no qual possuem alguns itens, como moedas, maçãs e espadas.

## Encontrando baús
- Caso o jogador não encontre inimigos durante a caminhada, ele encontrará baús.
- Ao encontrar um baú, o jogador pode escolher entre abrí-lo ou ignorá-lo. Ao abrir, você conseguirá ver seu loot e pegá-lo. Se ignorar, apenas volta para as opções iniciais sem coletar nenhum loot.
- O baú pode conter outros itens, dentre eles moedas, madeira e a rara espada lendária.

## Itens
- O jogo possui um total de 9 itens, sendo eles:
  - __Maçã (Apple)__
  - __Madeira (Wood)__
  - __Espada (Sword)__
  - __Osso (Bone)__
  - __Arame (Wire)__
  - __Lingote (Ingot)__
  - __Moeda (Coin)__
  - __Meat (Carne)__
  - __A Espada Lendária (Legendary Sword)__
- É possível usar alguns desses itens como itens de cura ou armas para equipar. Para usar, abra o invenário, selecione a opção __usar item (use item)__ e depois selecione o slot do item desejado.
   ### Itens de cura
  São itens que permitem curar o jogador, restaurando seus pontos de vida:
  - __Maçã (Apple)__ -> O mais comum, vem como loot de inimigos e baús. Restaura 10 pontos de vida.
  - __Meat (Carne)__ -> Mais difícil de encontrar, vem como loot de inimigos. Restaura 15 pontos de vida.
  ### Armas
  São itens que o jogador pode equipar, aumentando sua força de ataque:
  - __Espada (Sword)__ -> Largada de forma comum por inimigos. Tem força de ataque de 35.
  - __A Espada Lendária (Legendary Sword)__ -> Loot raro de baús. Tem força de ataque de 60.
  ### Itens sem uso
  - Madeira, Osso, Arame, Lingote e Moeda são atualmente os itens do jogo que não possuem nenhum uso, nem como cura, como arma ou outras coisas. Eles apenas existem.

## Dicas
- Sempre regenere o máximo de vida possível antes de uma batalha.
- Se você estiver com a vida baixa durante a batalha e o inimigo ainda tiver com muita vida, escolha fugir da batalha.
- Caso encontre um inimigo muito forte e você ainda não for forte o suficiente, escolha nem lutar.
- Certifique-se de esvaziar o inventário, descartando itens sem uso antes de sair para caminhar, para que seu inventário não esteja cheio e você consiga pegar todos os itens.
***
Espero que gostem do projeto e caso joguem, obrigado por jogar <3
