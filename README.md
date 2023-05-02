# Minesweeper (Miinaharava)

Kurssin **Ohjelmistotekniikka** harjoitustyötä varten luotu repositorio.

Sovellus on yksinpelattava *miinaharava*, jonka vaikeustason voi käyttäjä itse kustomoida. Käyttäjä voittaa pelin, mikäli onnistuu avaamaan kaikki miinattomat ruudut. Käyttäjä häviää pelin, mikäli osuu miinaan.

## Dokumentaatio
[Arkkitehtuurikuvaus](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/arkkitehtuuri.md) \
[Tuntikirjanpito](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/tuntikirjanpito.md) \
[Vaatimusmäärittely](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/vaatimusmaarittely.md) \
[Changelog](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/changelog.md) \
[Käyttöohje](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kayttoohje.md)

## Releases

[Viikko 5 deadline](https://github.com/xelmas/ot-miinaharava/releases/tag/viikko5) \
[Viikko 6 deadline](https://github.com/xelmas/ot-miinaharava/releases/tag/viikko6)

## Asennusohjeet

1. Varmista, että poetry on asennettu komennolla ```poetry --version```
2. Kloonaa repositorio komennolla ```git clone``` tai lataa lähdekoodi kohdasta releases.
3. Siirry hakemistoon ja asenna riippuvuudet komennolla ```poetry install```
4. Ennen ohjelman käynnistämistä suorita alustustoimenpiteet komennolla ```poetry run invoke build```

## Komentorivitoiminnot

### Käynnistää sovelluksen:
```
poetry run invoke start
```

### Suorittaa testit:
```
poetry run invoke test
```

### Luo testikattavuusraportin:
```
poetry run invoke coverage-report
```

### Suorittaa pylint-tarkistuksen:
```
poetry run invoke lint
```

### Credits

All the game icons by [Lorc](https://lorcblog.blogspot.com/) under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) via [game-icons.net](https://game-icons.net/)
