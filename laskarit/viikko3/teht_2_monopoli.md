## Tehtävän kuvaus

Laajennetaan edellisen tehtävän luokkakaaviota tuomalla esiin seuraavat asiat:
Ruutuja on useampaa eri tyyppiä:

    Aloitusruutu
    Vankila
    Sattuma ja yhteismaa
    Asemat ja laitokset
    Normaalit kadut (joihin liittyy nimi)

Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan sijainti.
Jokaiseen ruutuun liittyy jokin toiminto.
Sattuma- ja yhteismaaruutuihin liittyy kortteja, joihin kuhunkin liittyy joku toiminto.
Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua.
Normaaleille kaduille voi rakentaa korkeintaan 4 taloa tai yhden hotellin. Kadun voi omistaa joku pelaajista. Pelaajilla on rahaa.

### Luodaan luokkakaavio

```mermaid
 classDiagram
      Game "1" --> "2..8" Player
      Game "1" --> "1" Board
      Game "1" --> "2" Dice
      class Game {
      }
      Player "1" --> "1" Piece
      class Player{
      }
      Board "1" --> "40" Square
      class Board{
      }
      Piece "0..8" ..> "1" Square
      class Piece{
      }
      Square "1" --> "1" Square: next square
      class Square{
      }
      class Dice{
         
      }
```
