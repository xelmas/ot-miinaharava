## Tehtävän kuvaus

Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi.
Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla.
Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

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
