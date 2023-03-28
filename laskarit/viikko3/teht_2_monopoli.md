## Tehtävän kuvaus

Laajennetaan edellisen tehtävän luokkakaaviota tuomalla esiin seuraavat asiat.
Ruutuja on useampaa eri tyyppiä:

    Aloitusruutu
    Vankila
    Sattuma ja yhteismaa
    Asemat ja laitokset
    Normaalit kadut (joihin liittyy nimi)

Vaatimukset:
    
    Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan sijainti.
    Jokaiseen ruutuun liittyy jokin toiminto.
    Sattuma- ja yhteismaaruutuihin liittyy kortteja, joihin kuhunkin liittyy joku toiminto.
    Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua.
    Normaaleille kaduille voi rakentaa korkeintaan 4 taloa tai yhden hotellin.
    Kadun voi omistaa joku pelaajista.
    Pelaajilla on rahaa.

### Luodaan luokkakaavio

```mermaid
 classDiagram
      Game "1" --> "2..8" Player
      Game "1" --> "1" Board
      Game "1" --> "2" Dice
      Game "1" --> "1" Jail
      Game "1" --> "1" Start
      
      class Game {
      }
      Player "1" --> "1" Piece
      Player "1" ..> "1" Street
      class Player{
        money
      }
      Board "1" --> "40" Square
      class Board{
      }
      Piece "0..8" ..> "1" Square
      class Piece{
      }
      Square "1" --> "1" Square: next square
      class Square{
        type
        action()
      }
      class Dice{
      }
      class Type {
        start
        jail
        chance
        street
        station
      }
      class Start {
        square
      }
      class Jail {
        square
      }
      Chance "1" --> "1" Card
      class Chance {
      }
      Street "1" --> "0..4" House
      Street "1" --> "0..1" Hotel
      class Street {
        name
      }
      class Hotel {
      }
      class House {
      }
      class Card{
        action()
      }
      
      
