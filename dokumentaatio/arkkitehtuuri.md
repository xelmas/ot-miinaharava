# Arkkitehtuurikuvaus

## Rakenne
Ohjelman pakkausrakenne:

![pakkauskaavio](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus ui vastaa käyttöliittymästä, game vastaa sovelluslogiikasta ja repository vastaa pelitietojen säilömisestä. Sprites-luokan objektit vastaavat pelin graafisista elementeistä.

## Käyttöliittymä

Käyttöliittymässä on päävalikko (Main menu), jossa on neljä eri toimintoa ja näkymää:
 - Play (aloittaa pelin)
 - Options (muokkaa asetuksia)
 - Leaderboard (tarkastele tilastoja)
 - Quit (lopettaa ohjelman)

UI-luokka vastaa siitä mikä näkymä näytetään käyttäjälle. Käyttöliittymä hyödyntää ResultServiceä tilastojen tallentamiseen ja näyttämiseen käyttäjälle, ja peliä pelattaessa kutsutaan Minesweeper-luokan oliota, joka vastaa pelilogiikasta yhdessä Board-luokan kanssa.

## Sovelluslogiikka

Minesweeper-luokan olio vastaa pelin toiminnallisuuksista yhdessä Board-luokan kanssa. Jos peli päättyy voittoon, tallennetaan tulos tietokantaan kutsumalla UI-luokassa ResultServiceä.

```mermaid
 classDiagram
      Minesweeper "1" --> "0..N" Sprites
      Minesweeper "1" --> "1" Board
      class Minesweeper {
        moves
        cell_size
      }
      class Board {
        width
        height
        mines
        game_over
        revealed
        mines
        flagged
        board
      }
      class Sprites{
        Adjacent
        Empty
        Mine
        Unrevealed
      }
```

Luokka/pakkauskaavio, joka kuvaa Minesweeper-luokan suhdetta muihin osiin:

![pakkauskaavio-luokka](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus-luokat.png)

Miinaharavapelin tilasta vastaavia metodeita ovat:
- ```initialize_tile_sprite(x_cor, y_cor, tile_content)```
- ```get_unflagged_mines()```
- ```is_lost()```
- ```is_won()```
- ```show_mines()```

Miinaharavapelin kentän toiminnallisista kokonaisuuksista vastaa Board-luokan metodit:
- ```reveal(x_cor, y_cor)```
- ```add_flag(x_cor, y_cor)```
- ```remove_flag(x_cor, y_cor)```

ResultService pääsee tietokantaan ResultRepository-luokan kautta, joka injektoidaan konstruktorikutsussa. ResultService-luokan toiminnalliset metodit ovat:
- ```create_result(username, level, time, moves)```
- ```get_results()```
- ```get_top_ten()```

UI-luokka vastaa käyttäjän kanssa kommunikoinnista. Sen toiminnallisista kokonaisuuksista vastaavia metodeita ovat:
- ```menu_loop()```
- ```hanlde_menu_events()```
- ```start()```
- ```options()```
- ```leaderboard()```
- ```credits()```
- ```main_menu()```

## Tietojen tallennus

Repository-luokan ResultRepository vastaa tietojen säilömisestä SQLite-tietokantaan.

Sovelluksessa on konfiguraatiotiedosto .env, joka määrittää tietokannan nimen.
Pelitulokset tallennetaan SQLite-tietokannan "results" tauluun. Tietokanta alustetaan init_database.py-tiedostossa.

## Päätoiminnallisuudet

Alla on kuvattuna ohjelman päätoiminnallisuudet sekvenssikaavioina.

### Pelin aloitus ja pelikentän luominen

Sekvenssikaavio kuvaa tilannetta, kun käyttäjä klikkaa "Play"-nappia ja aloitetaan uusi peli.

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Minesweeper
  participant Board
  participant Sprites
  User ->> UI: click "Play" button
  UI ->> UI: start_game()
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
    Minesweeper ->> Board: get_revealed_tiles()
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
UI-luokan tapahtumankäsittelijä kutsuu omaa metodiaan start, joka luo uuden Minesweeper-luokan olion. Minesweeper-luokka luo Board-olion, joka vastaa sovelluksen pelikentän logiikasta. Board-olio asettaa miinat satunnaisesti kentälle. Tämän jälkeen kontrolli siirtyy takaisin Minesweeper-luokan oliolle, joka alustaa graafisista elementeistä vastuussa olevat sprite-luokat. Tämän jälkeen Minesweeper-luokan olio kutsuu Board-luokan metodia get_board, joka palauttaa pelikentän kaksiuloitteisena listana. Listasta käydään silmukassa läpi kaikki pelikentän ruudut koordinaateittain (x, y) ja alustetaan ruutu initialize_tile_sprite metodilla. Metodi alustaa ruudun sen perusteella mikä on pelikentän ruudun sisältö ja onko ruutua vielä avattu tai liputettu. Alkutilanteessa kaikki spritet ovat avaamattomia eli ne ovat luokasta Unrevealed. Kun silmukka on käyty läpi, lisätään alustettu sprite-luokka all_sprites-ryhmään. Kontrolli palaa takaisin UI-luokkaan, joka kutsuu Minesweeper-luokan olion metodia draw ja piirtää pelikentän ikkunaan. UI-luokka päivittää ikkunan, jolloin pelikenttä ilmestyy käyttäjän ruudulle.

### Tilastojen tarkasteleminen

Sekvenssikaavio kuvaa tilannetta, kun sovellus on käynnistetty ja käyttäjä klikkaa "Leaderboard"-nappia.

```mermaid
sequenceDiagram
  User ->> UI: click "Leaderboard" button
  UI ->> UI: leaderboard()
  UI ->> ResultService: get_top_ten()
  ResultService ->> ResultRepository: find_top_ten()
  ResultRepository -->> ResultService: results
  ResultService -->> UI: results
  UI ->> UI: update()
  UI -->> User: 
```
UI-luokan tapahtumankäsittelijä kutsuu ResultService-luokan metodia get_top_ten().
ResultServicen metodi get_top_ten() kutsuu ResultRepositoryn luokan metodia find_top_ten(), joka palauttaa korkeintaan 10 parasta tulosta listana. UI päivittää näkymän ja piirtää ikkunaan tulokset näkyville. 

### Pelituloksen luominen

Sekvenssikaavio kuvaa tilannetta, kun peli on päättynyt ja pelitulos tallennetaan tietokantaan.

```mermaid
sequenceDiagram
  User ->> UI: clicks tile
  alt if game won
    UI ->> ResultService: create_result("PLAYER", "9, 9, 10", 140, 50)
    ResultService ->> ResultRepository: create(result)
    ResultRepository -->> ResultService: result
    ResultService -->> UI: result
  end
  UI ->> UI: to_main_menu()
  UI -->> User: 
```
Jos peli päättyy käyttäjän voittoon, UI-luokasta kutsutaan ResultService luokan metodia create_result, jolle annetaan parametriksi käyttäjänimi, vaikeustaso (merkkijonona muodossa "leveys, korkeus, miinojen_lkm"), kulunut aika, tehtyjen siirtojen määrä. 
ResultService kutsuu luokan ResultRepository metodia create, joka luo uuden tuloksen ja tallentaa sen tietokantaan.
UI päivittää ikkunan ja käyttäjä palaa takaisin päävalikkoon.

### Peliasetusten muuttaminen

Sekvenssikaavio kuvaa tilannetta, missä käyttäjä vaihtaa asetuksista vaikeustasoksi Custom ja asettaa leveydeksi 12, korkeudeksi 10 ja miinojen lukumääräksi 10 ja klikkaa takaisin päävalikkoon.

```mermaid
sequenceDiagram
  User ->> UI: clicks "Options" button
  UI ->> UI: options()
  alt if custom level
    UI ->> UI: set_game_width(12)
    UI ->> UI: set_game_height(10)
    UI ->> UI: set_game_mines(10)
  end
  UI -->> User: 
  User ->> UI: clicks "to main menu" button
  UI ->> UI: to_main_menu()
  UI -->> User: 
```

### Ruudun avaaminen

Sekvenssikaavio kuvaa tilannetta, kun käyttäjä on peli-ikkunassa ja klikkaa ruutua hiiren vasemmalla painikkeella.

```mermaid
sequenceDiagram
  User ->> UI: clicks left mouse button
  UI ->> Minesweeper: 
  Minesweeper ->> Board: reveal(x_cor, y_cor)
  alt if over_board
    Board -->> Minesweeper: False
  
  else if tile not revealed
    Board ->> Board: revealed.add(tile_position)
    alt if user clicked
      Board ->> Board: add_move()
    end
  
  else if tile is mine
    Board ->> Minesweeper: False

  else if all tiles opened
    Board ->> Minesweeper: True
  
  Board ->> Board: get_num_adjacent_mines(x_cor, y_cor)
  else if adjacent_mines = 0
    loop x_cor2, y_cor2 in neighbors
      Board ->> Board: reveal(x_cor2, y_cor2, click=0)
    end
  Board ->> Minesweeper: True
  end
  Minesweeper -->> UI: 
  UI ->> UI: update_game(game, display)
  UI ->> Minesweeper: 
  Minesweeper ->> Minesweeper: initialize_sprites()
  Minesweeper ->> Minesweeper: draw()
  Minesweeper -->> UI: 
  UI ->> UI: update()
  UI -->> User: 
```

### Muut toiminnallisuudet

Muut toiminnallisuudet, kuten ruutujen liputus tai asetusten muuttaminen toimivat vastaavasti, eli UI-tapahtumankäsittelijä kutsuu sovelluslogiikan tarjoamaa sopivaa metodia. Kun kontrolli päätyy takaisin UI-luokalle, päivitetään uusi näkymä käyttäjälle.

## Kehitysehdotus rakenteeseen

Board-luokassa on pylint-tarkistustuksen mukaan liian monta oliomuuttujaa. Tämän voisi korjata käyttämällä esimerkiksi pelikentän dimensioiden tallennukseen sanakirjaa.

