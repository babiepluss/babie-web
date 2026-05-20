# Babie+ Siteyi Yerelde Calistirma Rehberi

Bu repo bir framework dev server'i ile degil, statik build akisi ile calisir.

Siteyi yerelde gormek icin once `dist/` ciktisini uretir, sonra bu klasoru kucuk bir lokal HTTP sunucusu ile servis edersiniz.

## 1. Gerekenler

- Python 3
- Repo kok dizininde terminal
- `requirements.txt` icindeki bagimliliklar

## 2. Ilk Kurulum

Eger `.venv` klasoru yoksa once sanal ortam olusturun:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Eger `.venv` zaten varsa bagimliliklari guncellemeniz yeterlidir:

```bash
.venv/bin/pip install -r requirements.txt
```

## 3. Siteyi Build Et

Asagidaki komut hem ana sayfayi, hem ayri oneri studyosu sayfasini, hem de plan karsilastirma sayfasini ve statik asset'leri `dist/` altina uretir:

```bash
.venv/bin/python build.py
```

Build sonrasi beklenen ana cikti:

- `dist/index.html`
- `dist/oneri/index.html`
- `dist/erken-erisim/index.html`
- `dist/assets/styles.css`
- `dist/assets/app.js`

## 4. Kontrolleri Calistir

Bu komut build ciktisini, temel HTML yapisini ve markdown yol kontrollerini dogrular:

```bash
.venv/bin/python check.py
```

## 5. Siteyi Tarayicida Ac

Build alindiktan sonra `dist/` klasorunu yerel sunucuda servis edin:

```bash
.venv/bin/python -m http.server 8000 --directory dist
```

Sonra tarayicida su adresleri acin:

```text
http://localhost:8000
http://localhost:8000/oneri/
http://localhost:8000/erken-erisim/
```

Sunucuyu durdurmak icin ayni terminalde `Ctrl + C` kullanin.

## 6. Tek Satirlik Akis

Her seyi tek komutta yapmak isterseniz:

```bash
.venv/bin/python build.py && .venv/bin/python check.py && .venv/bin/python -m http.server 8000 --directory dist
```

Bu komutta son adim sunucu actigi icin terminal mesgul kalir; durdurana kadar sayfa acik kalir.

## 7. Sik Gorulen Problemler

- `.venv/bin/python: no such file or directory`
  - Sanal ortam henuz olusturulmamistir. 2. adimdaki `python3 -m venv .venv` komutunu calistirin.

- `ModuleNotFoundError: No module named 'jinja2'`
  - Bagimliliklar kurulmamistir. `.venv/bin/pip install -r requirements.txt` calistirin.

- `OSError: [Errno 48] Address already in use`
  - 8000 portu doludur. Ornegin 8001 ile yeniden deneyin:

```bash
.venv/bin/python -m http.server 8001 --directory dist
```

Bu durumda tarayicida `http://localhost:8001` adresini acin.
