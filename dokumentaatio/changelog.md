## Viikko 3

- Lisätty Board-luokka, joka luo pelikentän ja asettaa miinat
- Lisätty jokaiselle ruudulle omat Sprite-oliot ja niihin liittyvät grafiikat
- Testattu, että Board-luokassa pelikentän luominen sekä dimensioiden ja miinojen asetus onnistuu
- Testattu, että spritejen koordinaatit asetetaan oikein

## Viikko 4
- Muokattu tiedostojen ja luokkien nimiä, refaktoroitu koodia.
- Board-luokka muutettu Minesweeper-luokaksi, joka vastaa pelilogiikasta.
- Pelilogiikka luotu toimimaan terminaalissa
- Testattu Minesweeper-luokan reveal-funktion toiminta
- Luotu käyttöliittymäluokka UI
- Päävalikkoon luotu neljä eri toimintoa, asetuksiin luotu toiminnallisuus kentän dimensioiden muokkaamiseen

## viikko 5
- Pelin graafinen toteutus
- Lisätty uusi flag-sprite ja kuva.
- Lisätty toiminnallisuus ruutujen liputtamiseen ja liputuksen poistoon
- Lisätty credits-osio menuun, jossa ilmoitettu käytettyjen kuvien tekijä
- Lisätty options-ikkunaan mahdollisuus muuttaa miinojen määrää pelissä
- Assets-kansion kuvien kokoa pienennetty kokoon 30x30
- Lisätty ajanotto (timer)
- Refaktoroitu koodia. Tapahtumakäsittelijät siirretty omiin funktioihin. 
- Luotu oma luokka Board, joka vastaa pelikentästä
- Lisätty laskuri avattujen ruutujen määrälle
- Testattu, että Board-luokan liputus ja liputuksen poisto toimii oikein
- Testattu, että Minesweeper-luokan is_lost(), is_won(), set_time_passed() ja get_time_passed funktiot toimii oikein
- Luotu sekvenssikaavio pelin aloittamisesta
- Lisätty teksti kun peli päättyy (voitto tai häviö)