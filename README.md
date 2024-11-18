# Toto-šperky - Webová aplikácia

## O projekte
Webová aplikácia vytvorená pre výrobcu ručne vyrábaných šperkov, ktorá slúži na prezentáciu produktov a komunikáciu so zákazníkmi. Aplikácia umožňuje správu produktov, kategórií a blogu prostredníctvom administrátorského rozhrania.

## Hlavné funkcie

### Verejná časť
- Prezentácia šperkov v galérii s možnosťou filtrovania podľa kategórií
- Detailné zobrazenie produktov s obrázkami a videami
- Sekcia "O mne" s informáciami o výrobcovi
- Blog sekcia s článkami a fotogalériou
- Kontaktná stránka
- Responzívny dizajn pre všetky zariadenia

### Administrátorská časť (CRUD operácie)

#### Správa produktov
- Pridávanie nových produktov
- Úprava existujúcich produktov
- Mazanie produktov
- Nastavenie dostupnosti produktov
- Nahrávanie obrázkov a videí

#### Správa kategórií
- Vytváranie nových kategórií
- Úprava existujúcich kategórií
- Mazanie kategórií
- Priradenie produktov do kategórií

#### Správa blogu
- Pridávanie nových článkov
- Úprava existujúcich článkov
- Mazanie článkov
- Nahrávanie viacerých obrázkov ku článkom
- Automatický výpočet času čítania

## Technické detaily

### Obmedzenia pre nahrávané súbory
- Obrázky: maximálna veľkosť 15 MB
- Videá: maximálna veľkosť 120 MB

### SEO Optimalizácia
- Meta tagy pre všetky stránky
- Open Graph protokol pre zdieľanie na sociálnych sieťach
- Schema.org značkovanie pre lepšiu indexáciu
- Optimalizované URL adresy (slugy)

### Zabezpečenie
- Autentifikácia používateľov pre prístup k admin funkciam
- CSRF ochrana pre všetky formuláre
- Validácia nahrávaných súborov

### Paginácia a filtrovanie
- Nastaviteľný počet položiek na stránku (15/30/50)
- Filtrovanie produktov podľa kategórií
- Možnosť priameho prechodu na konkrétnu stránku

## Použité technológie
- Django (Python web framework)
- HTML5, CSS3, JavaScript
- Postgre databáza

