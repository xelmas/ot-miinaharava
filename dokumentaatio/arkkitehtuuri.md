# Arkkitehtuurikuvaus

### Rakenne
Ohjelman pakkausrakenne:
![alt text](https://github.com/xelmas/ot-miinaharava/tree/main/dokumentaatio/kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus ui vastaa käyttöliittymästä, minesweeper vastaa sovelluslogiikasta ja sprites vastaa pelin graafisista elementeistä.

### Käyttöliittymä

Käyttöliittymässä on main menu, jossa neljä eri toimintoa ja näkymää:
 - Play (aloittaa pelin)
 - Options (muokkaa asetuksia)
 - Leaderboard (tarkastele tilastoja)
 - Quit (lopettaa ohjelman)

UI-luokka vastaa siitä mikä näkymä näytetään käyttäjälle.

### Sovelluslogiikka
