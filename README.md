# Minesweeper (Miinaharava)

Kurssin **Ohjelmistotekniikka** harjoitustyötä varten luotu repositorio.

Sovellus on yksinpelattava *miinaharava*, jonka vaikeustason voi käyttäjä itse kustomoida. Käyttäjä voittaa pelin, mikäli onnistuu merkkaamaan kaikki piilossa olevat miinat. Käyttäjä häviää pelin, mikäli osuu miinaan.

## Dokumentaatio
[Arkkitehtuurikuvaus](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/arkkitehtuuri.md) \
[Tuntikirjanpito](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/tuntikirjanpito.md) \
[Vaatimusmäärittely](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/vaatimusmaarittely.md) \
[Changelog](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/changelog.md)

## Asennusohjeet

1. Varmista, että poetry on asennettu komennolla ```poetry --version```
2. Kloonaa repositorio komennolla ```git clone```
3. Siirry hakemistoon ja asenna riippuvuudet komennolla ```poetry install```

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

### Credits

Used assets are from [game-icons.net](https://game-icons.net/). All the credits for [Lorc](https://lorcblog.blogspot.com/) under CC BY 3.0 /
