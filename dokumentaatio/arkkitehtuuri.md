# Arkkitehtuurikuvaus

## Rakenne
Ohjelman pakkausrakenne:

![pakkauskaavio](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus ui vastaa käyttöliittymästä, minesweeper ja board vastaavat sovelluslogiikasta ja sprites vastaa pelin graafisista elementeistä.

## Käyttöliittymä

Käyttöliittymässä on main menu, jossa neljä eri toimintoa ja näkymää:
 - Play (aloittaa pelin)
 - Options (muokkaa asetuksia)
 - Leaderboard (tarkastele tilastoja)
 - Quit (lopettaa ohjelman)

UI-luokka vastaa siitä mikä näkymä näytetään käyttäjälle.

## Sovelluslogiikka

Minesweeper-luokan olio vastaa pelin toiminnallisuuksista yhdessä Board-luokan kanssa.

```mermaid
 classDiagram
      Minesweeper "1" --> "0..N" Sprites
      Minesweeper "1" --> "1" Board
      class Minesweeper {
        moves
        time_passed
        cell_size
      }
      class Board {
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

### Pelin aloitus ja pelikentän luominen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Minesweeper
  participant Board
  participant Sprites
  User ->> UI: click "Play" button
  UI ->> UI: start()
  UI ->> Minesweeper: Minesweeper(9, 9, 10, 31)
  Minesweeper ->> Board: Board(9,9,10)
  Board ->> Board: place_mines()
  Board -->> Minesweeper: 
  Minesweeper ->> Minesweeper: initialize_sprite_groups()
  Minesweeper ->> Minesweeper: initialize_sprites()
  Minesweeper ->> Board: get_board()
  Board -->> Minesweeper: board_2dim_list
  loop coordinates (x_cor, y_cor)
    Minesweeper ->> Minesweeper: initialize_tile_sprite(x_cor, y_cor, tile_content)
    Minesweeper ->> Board: get_revealed()
    Board -->> Minesweeper: revealed_list
    Minesweeper ->> Sprites: Unrevealed(norm_x, norm_y)
    Sprites -->> Minesweeper: 
  end
  Minesweeper ->> Minesweeper: all_sprites.add(unrevealed_tiles)
  Minesweeper -->> UI: 
  UI ->> Minesweeper: all_sprites.draw()
  Minesweeper -->> UI: 
  UI ->> UI: update()
  UI -->> User: 
```