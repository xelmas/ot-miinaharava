# Arkkitehtuurikuvaus

## Rakenne
Ohjelman pakkausrakenne:

![pakkauskaavio](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus ui vastaa käyttöliittymästä, minesweeper, board ja service vastaavat sovelluslogiikasta ja repository vastaa pelitietojen säilömisestä. Sprites-luokan objektit vastaavat pelin graafisista elementeistä.

## Käyttöliittymä

Käyttöliittymässä on päävalikko (Main menu), jossa neljä eri toimintoa ja näkymää:
 - Play (aloittaa pelin)
 - Options (muokkaa asetuksia)
 - Leaderboard (tarkastele tilastoja)
 - Quit (lopettaa ohjelman)

UI-luokka vastaa siitä mikä näkymä näytetään käyttäjälle. Käyttöliittymä hyödyntää ResultServiceä tilastojen näyttämiseen käyttäjälle ja peliä pelattaessa kutsutaan Minesweeper-luokan oliota, joka vastaa pelilogiikasta.

## Sovelluslogiikka

Minesweeper-luokan olio vastaa pelin toiminnallisuuksista yhdessä Board-luokan kanssa. Jos peli päättyy voittoon, tallennetaan tulos tietokantaan kutsumalla ResultServiceä.

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

ResultService pääsee tietokantaan ResultRepository-luokan kautta, joka injektoidaan konstruktorikutsussa.

## Päätoiminnallisuudet

Alla on kuvattuna ohjelman päätoiminnallisuudet sekvenssikaavioina.

### Pelin aloitus ja pelikentän luominen

Sekvenssiokaavio kuvaa tilannetta, kun käyttäjä klikkaa "Play"-nappia ja aloitetaan uusi peli.

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
UI-luokan tapahtumankäsittelijä kutsuu omaa metodiaan start, joka luo uuden Minesweeper-luokan olion. Minesweeper-luokka luo Board-olion, joka vastaa sovelluksen pelikentän logiikasta. Board-olio asettaa miinat satunnaisesti kentälle. Tämän jälkeen kontrolli siirtyy takaisin Minesweeper-luokan oliolle, joka alustaa graafisista elementeistä vastuussa olevat sprite-luokat. Tämän jälkeen Minesweeper-luokan olio kutsuu Board-luokan metodia get_board, joka palauttaa pelikentän kaksiuloitteisena listana. Listasta käydään silmukassa läpi kaikki pelikentän ruudut koordinaateittain (x, y) ja alustetaan ruutu initialize_tile_sprite metodilla. Metodi alustaa ruudun sisällön sen perusteella mikä on pelikentän ruudun sisältö ja onko ruutua vielä avattu tai liputettu. Alkutilanteessa kaikki spritet ovat avaamattomia eli ne ovat luokasta Unrevealed. Kun silmukka on käyty läpi, lisätään alustettu sprite-luokka all_sprites-ryhmään. Kontrolli palaa takaisin UI-luokkaan, joka kutsuu Minesweeper-luokan olion metodia draw ja piirtää pelikentän ikkunaan. UI-luokka päivittää ikkunan, jolloin pelikenttä ilmestyy käyttäjän ruudulle.

### Tilastojen tarkasteleminen

Sekvenssikaavio kuvaa tilannetta, kun sovellus on käynnistetty ja käyttäjä klikkaa "Leaderboard"-nappia.

```mermaid
sequenceDiagram
  User ->> UI: click "Leaderboard" button
  UI ->> ResultService: get_results()
  ResultService ->> ResultRepository: find_all()
  ResultRepository -->> ResultService: results
  ResultService -->> UI: results
  UI ->> UI: show_leaderboard()
```
UI-luokan tapahtumankäsittelijä kutsuu ResultService-luokan metodia get_results().
ResultServicen metodi get_results() kutsuu ResultRepositoryn luokan metodia find_all(), joka palauttaa kaikki tulokset listana.
UI päivittää näkymän ja piirtää ikkunaan tulokset näkyville funktiolla show_leaderboard().

### Pelituloksen luominen

Sekvenssikaavio kuvaa tilannetta, kun sovellus on käynnistetty ja käyttäjä klikkaa "Play"-nappia.

```mermaid
sequenceDiagram
  User ->> UI: click "Play" button
  loop if game won
    UI ->> ResultService: create_result("PLAYER", "9, 9, 10", 140, 50)
    ResultService ->> ResultRepository: create(result)
    ResultRepository -->> ResultService: result
    ResultService -->> UI: result
  end
  UI ->> UI: show_leaderboard()
  UI -->> User: 
```
Jos peli päättyy käyttäjän voittoon, UI-luokasta kutsutaan ResultService luokan metodia create_result, jolle annetaan parametriksi käyttäjänimi, vaikeustaso (merkkijonona muodossa "leveys, korkeus, miinojen_lkm"), kulunut aika, tehtyjen siirtojen määrä. 
ResultService kutsuu luokan ResultRepository metodia create, joka luo uuden tuloksen ja tallentaa sen tietokantaan.
UI päivittää ikkunan ja käyttäjälle näytetään uusin Leaderboard-tilasto.