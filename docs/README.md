# Babie+ Web Dokuman Paketi

Bu klasor, babie+ web sitesi icin ilk calisma omurgasini toplar.

Yapi olarak Quadrix projesindeki docs paketinden ilham alir; icerik olarak ise babie+ projesinin kendi kaynaklarina dayanir.

## Root Talimat Dosyasi

Repo kokundeki AGENTS.md, workspace geneline uygulanan kisa talimat dosyasidir.

Bu dosya:

- detayli docs sisteminin yerine gecmez
- ama ilk giris noktasi olarak hangi dokumanlarin okunacagini ve hangi kurallarin sabit oldugunu ozetler

Project-wide davranis degistiginde AGENTS.md de kontrol edilmelidir.

## Mevcut Proje Durumu

Bu workspace icinde artik ilk calisan statik web iskeleti bulunur.

V2.5 web yuzeyi:

- trust-first landing page (`/`)
- backend'e bagli olmayan durust kisisellestirilmis oneri studyosu (`/oneri/`)
- fiyatli Mevcut / Plus / Premium plan karsilastirma yuzeyi (`/erken-erisim/`)
- Jinja2 ile uretilen template tabanli HTML
- token tabanli CSS sistemi
- no-JS durumda erisilebilir kalan mobil navigasyon
- hafif reveal JS'i ve client-side state ile desteklenen yuzey gecisleri
- temel Open Graph ve Twitter card meta katmani

Ana teknik yapi:

- src/content/home.py: ana sayfa icerik verisi
- src/templates/base.html: ortak HTML kabugu
- src/templates/index.html: ana sayfa template'i
- src/templates/recommendation.html: ayri oneri studyosu template'i
- src/templates/early_access.html: uc kartli plan/fiyat final yuzeyi template'i
- src/static/styles.css: Calm Premium Care tasarim tokenlari, brand lockup kurallari ve section sistemi
- src/static/brand/: Babie+ lockup, mark, tile ve icon assetleri
- src/static/site.webmanifest: favicon ve app icon bildirim dosyasi
- src/static/app.js: mobil nav, reveal davranisi, studyo step machine ve plan karsilastirma yuzeyi
- build.py / check.py: repo kokunden calisan kisa wrapper komutlari
- scripts/build.py: dist/index.html, dist/oneri/index.html, dist/erken-erisim/index.html ve assets ciktisini uretir (multi-page)
- scripts/check.py: home page guard, recommendation studio guard, plan comparison/no-JS fallback guard, dynamic featured card guard, snapshot restart guard, landmark, nav aria, no-JS nav, sticky-cta mobile guard, markdown geneli PDF yolu ve truth-safe copy guard kontrolu yapar
- dist/: build sonrasi uretilen statik cikti

Yerel build:

```bash
.venv/bin/python build.py
.venv/bin/python check.py
```

Eldeki ana kaynaklar su dosyalardir:

- babie+ dosyaları/32-MI5.pdf
- babie+ dosyaları/babie+_basvuru_formu.pdf

Bu iki belgeye gore babie+:

- 0-24 aylik bebegi olan ebeveynler icin konumlanan bir ebeveyn destek platformu
- kisisellestirilmis abonelik kutusu modeli uzerine kurulu bir girisim
- yas, kilo, gelisim evresi ve hassasiyet bilgilerine gore urun secimini kolaylastirmayi hedefleyen bir yapi
- uzun vadede topluluk, karar destek sistemi ve kendi marka urun katmanlari tasiyan bir ekosistem

## Bu Web Sitesinin Ilk Gorevi

Ilk surum site bir pazar yeri gibi davranmamalidir.

Ilk gorevler sunlar olmali:

1. babie+'in ne oldugunu net anlatmak
2. guven vermek
3. ebeveyni kisisellestirilmis oneri studyosuna yonlendirmek
4. kisisellestirme mantigini gostermek
5. ileride gelecek urun ve topluluk katmanlari icin dogru beklentiyi kurmak

V2.5 polish notu (plan comparison final surface):

- Site uc yuzeye ayrildi: trust-first home page (`/`), kisisellestirilmis oneri studyosu (`/oneri/`) ve fiyatli plan karsilastirma yuzeyi (`/erken-erisim/`).
- Mobil ilk ekranda copy ve CTA, gorsel panelden once gelir.
- Header CTA, hero birincil CTA ve mobil sticky CTA `/oneri/` rotasina baglidir.
- Mobil sticky CTA yalnizca home page'de render edilir; ilk yuklemede gizli kalir, scroll sonrasinda yardimci aksiyon olarak gorunur ve gorsel/iletisim/footer ustune gereksiz binmemelidir.
- Sticky CTA, mobil menu acikken, iletisim bolumu veya footer gorunurken otomatik gizlenir; kullanici yukari donerse dogru state'e geri doner.
- Home page son bolumu artik bridge teaser degil; Instagram ve e-posta kanallarini gosteren sakin iletisim panelidir.
- Iletisim panelinde Instagram `https://www.instagram.com/babieplus/?utm_source=ig_web_button_share_sheet` ve e-posta `babieplus@gmail.com` yer alir; siparis, odeme veya otomatik basvuru akisi baslatmaz.
- Iletisim panelı V2.7 itibarıyla kompakt list-row modulune indirildi: kucuk eyebrow ikonu, kucultulmus baslik, kisa lede, pill formunda sakin not ve sol-ikon + ortada metin + sag yon oku tasiyan iki kompakt kanal kartı vardir; sahte medya kutusu, dev rounded-square placeholder, harita veya iframe kullanilmaz.
- `/oneri/` sayfasi dort fazli bir akistir: intro -> questions -> transition -> result. Step 1'de gorunur "Karsilamaya don" butonu vardir.
- Result reveal sonrasi birincil CTA artik FAQ degil `/erken-erisim/` sayfasina gider; result olusunca stüdyo durumunun sessionStorage snapshot'i kaydedilir.
- Result ekranindaki "Secimleri duzenle" mevcut secimi korur; "Bastan basla" formu varsayilanlara dondurur ve `babie:studio-snapshot` degerini temizler.
- `/erken-erisim/` sayfasi artik Mevcut / Plus / Premium planlarini fiyat ve kapsamla yan yana gosteren uc kartli final yuzeyidir.
- Fiyatlar veri modelinden gelir: Mevcut `0 TL`, Plus `799 TL / 15 Gun`, Premium `1199 TL'den baslar`.
- Kartlarda plan adi, buyuk fiyat satiri, kisa alt aciklama, guclu CTA ve tikli feature listesi bulunur.
- Plus snapshot yokken varsayilan featured plandir. Snapshot varsa tone mapping `starter -> Mevcut`, `daily/balance -> Plus`, `gift -> Premium` seklinde calisir ve featured gorunum ilgili plana tasinir.
- Kart icindeki tek `<button type="button">` secim kontroludur; kart article'i ekstra tab stop uretmez. Secim `aria-pressed` ve kart icindeki secili badge ile ifade edilir; alttaki alan ana odak degil, secilen plan icin kisa durust not panelidir.
- Sayfa fiyat ve plan karsilastirmasi gosterir; buna ragmen gercek checkout, otomatik gonderim, stok/kargo iddiasi veya desteklenmeyen AI/topluluk/uzman claim'i kurmaz.
- Studyoda no-JS fallback gercek calisir: intro/transition/result fazlari gizlenir, questions fazi tamamen stack edilmis fieldset'ler olarak gorunur ve dogrudan kullanilabilir.
- Reduced-motion durumunda transition fazi kisalir, reveal animasyonlari ve kart hover efektleri nötrlenir.
- Truth-safe dil korunur: "AI sizin icin karar verdi", "akilli motor", "doktor onayli", "aboneliginiz basladi", "teslimat tarihi", "premium'u yükselt" gibi cumleler kullanilmaz.

Brand entegrasyon notu:

- Header artik metin placeholder degil; acik zeminlerde kullanilan gercek Babie+ lockup'ini tasir.
- Footer koyu yuzeyde ters lockup kullanir; logo varyanti dark mode degil yuzey kontrastina gore secilir.
- Brand assetleri `src/static/brand/` altinda tutulur: `babie-plus-lockup-on-light.png`, `babie-plus-lockup-on-dark.png`, `babie-plus-mark-on-light.png`, `babie-plus-mark-on-dark.png` ve favicon/app icon turevleri.
- Kare tile assetleri UI lockup yerine gecmez; favicon, apple-touch-icon, manifest ve temel paylasim meta gorseli gibi kontrollu alanlarda kalir.
- `src/templates/base.html` icon/meta linklerini ve header/footer brand entegrasyonunu render eder.

## Oncelikli Okuma Sirasi

1. ../AGENTS.md
2. 15_VISUAL_DIRECTION_LOCK_TR.md
3. 14_TRUTH_AUDIT_TR.md
4. 01_SITE_FOUNDATION_TR.md
5. 02_WIREFRAMES_TR.md
6. 05_HOMEPAGE_COPY_TR.md
7. 17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md
8. 19_SITEYI_CALISTIRMA_TR.md
9. 18_DOC_UPDATE_PROTOCOL_TR.md

## Aktif Dokumanlar

- 01_SITE_FOUNDATION_TR.md
Site neden var, kime hitap eder, neyi donusturmeli, hangi sayfalar gerekir.

- 02_WIREFRAMES_TR.md
Ana sayfa, oneri studyosu ve erken erisim yuzeylerinin dusuk sadakat yerlesim plani.

- 05_HOMEPAGE_COPY_TR.md
Ana sayfada kullanilabilecek ilk metin omurgasi.

- 14_TRUTH_AUDIT_TR.md
Public copy yazarken hangi iddialarin guvenli oldugu.

- 15_VISUAL_DIRECTION_LOCK_TR.md
Babie+ icin secilen gorsel yon ve reddedilecek gorunumler.

- 17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md
Bu repoda siteyi gelistirecek AI veya gelistirici icin calisma rehberi.

- 19_SITEYI_CALISTIRMA_TR.md
Siteyi build edip yerel sunucuda acmak icin hizli calistirma rehberi.

- 18_DOC_UPDATE_PROTOCOL_TR.md
Her kod degisikliginden sonra hangi markdown dosyalarinin zorunlu olarak gozden gecirilecegini tanimlayan protokol.

## Temel Kurallar

- Site ilk asamada landing page + oneri studyosu + erken erisim cercevesi mantiginda ilerlemeli.
- Gercekte hazir olmayan ozellikler yayindaymis gibi anlatilmamali.
- Guven, sadelik ve yonlendirme; katalog kalabaligindan daha oncelikli olmali.
- Tasarim fazla bebeksi, fazla medikal ya da fazla SaaS gorunmemeli.

## Not

Urun gercegi degisirse once truth audit guncellenmeli, sonra copy ve tasarim buna gore ilerlemelidir.

Her kodsal degisiklikten sonra 18_DOC_UPDATE_PROTOCOL_TR.md kontrol edilmeli ve gerekli markdown guncellemeleri ayni turda yapilmalidir.
