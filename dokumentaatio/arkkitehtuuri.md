# Arkkitehtuurikuvaus

## Rakenne
Ohjelman pakkausrakenne:

![pakkauskaavio](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/arkitehtuuri-pakkaus.png)

Pakkaus ui vastaa käyttöliittymästä, minesweeper vastaa sovelluslogiikasta ja sprites vastaa pelin graafisista elementeistä.

## Käyttöliittymä

Käyttöliittymässä on main menu, jossa neljä eri toimintoa ja näkymää:
 - Play (aloittaa pelin)
 - Options (muokkaa asetuksia)
 - Leaderboard (tarkastele tilastoja)
 - Quit (lopettaa ohjelman)

UI-luokka vastaa siitä mikä näkymä näytetään käyttäjälle.

## Sovelluslogiikka

Minesweeper-luokan olio vastaa pelin toiminnallisuuksista.

```mermaid
 classDiagram
      Minesweeper "1" --> "0..N" Sprites
      class Minesweeper {
        width
        height
        mines
        revealed_tiles_list
      }
      class Sprites{
        adjecent
        empty
        mine
        unrevealed
      }
```

Luokka/pakkauskaavio, joka kuvaa Minesweeper-luokan suhdetta muihin osiin:

![pakkauskaavio-luokka](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus-luokat.png)

## Päätoiminnallisuudet

### Pelin aloitus

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Minesweeper
  participant Sprites
  participant Board
  User ->> UI: click "Play" button
  UI ->> UI: start()
  UI ->> Minesweeper: Minesweeper(9, 9, 10, 31)
  Minesweeper ->> Board: Board(9,9,10)
  Board ->> Board: place_mines()
  Board -->> Minesweeper: 
  Minesweeper ->> Minesweeper: initialize_sprite_groups()
  Minesweeper ->> Minesweeper: initialize_sprites()
  Minesweeper ->> Minesweeper: initialize_tile_sprite()
  Minesweeper ->> Sprites: Unrevealed(norm_x, norm_y)
  Minesweeper -->> Sprites: 
  Minesweeper -->> UI: 
  UI ->> UI: update()
  UI -->> User: 
```