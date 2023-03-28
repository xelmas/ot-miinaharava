## Tehtävän kuvaus

Tarkastellaan bensatankista ja moottorista koostuvan koneen Python-koodia.
Piirrä sekvenssikaaviona tilanne, jossa kutsutaan (jostain koodin ulkopuolella olevasta metodista) ensin Machine-luokan konstruktoria ja sen jälkeen luodun Machine-olion metodia drive.

```mermaid
sequenceDiagram
  main ->> motor: Machine()
  motor ->> fuel_tank: FuelTank()
  fuel_tank ->> motor: fuel_contents(0)
  motor ->> fuel_tank: fill(40)
  fuel_tank ->> motor: fuel_contents(40)
  motor ->> engine: Engine()
  engine -->> main: 
  main ->> motor: drive()
  motor ->> engine: start()
  engine ->> fuel_tank: consume(5)
  fuel_tank ->> motor: fuel_contents(35)
  motor ->> engine: is_running()
  engine ->> fuel_tank: fuel_contents()
  fuel_tank ->> engine: fuel_contents(35)
  alt True
    engine ->> motor: True
    motor ->> engine: use_energy()
    engine ->> fuel_tank: consume(10)
    fuel_tank ->> motor: fuel_contents(25)
  else
    engine ->> motor: False
  end
  motor -->> main: 
 
```
