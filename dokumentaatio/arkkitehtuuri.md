# Arkkitehtuurikuvaus

### Rakenne
Ohjelman pakkausrakenne:

![pakkauskaavio](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/arkitehtuuri-pakkaus.png)

Pakkaus ui vastaa käyttöliittymästä, minesweeper vastaa sovelluslogiikasta ja sprites vastaa pelin graafisista elementeistä.

### Käyttöliittymä

Käyttöliittymässä on main menu, jossa neljä eri toimintoa ja näkymää:
 - Play (aloittaa pelin)
 - Options (muokkaa asetuksia)
 - Leaderboard (tarkastele tilastoja)
 - Quit (lopettaa ohjelman)

UI-luokka vastaa siitä mikä näkymä näytetään käyttäjälle.

### Sovelluslogiikka
