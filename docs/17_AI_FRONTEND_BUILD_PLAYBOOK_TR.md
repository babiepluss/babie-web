# Babie+ AI Frontend Build Playbook

Bu dosya, babie+ reposunda calisacak AI veya gelistirici icin yerel bir calisma rehberidir.

Amac su:

- Quadrix docs mantigindan gelen yararli disiplini korumak
- ama babie+'in mevcut gercegine uygun davranmak
- ilk frontend calismasini odaktan koparmamak

## 1. Repo Gercegi

Bu repo artik greenfield dokuman paketinden ilk calisan statik web iskeletine gecmistir.

Workspace icinde V2.3 olarak uc yuzeyli site vardir: trust-first landing page (`/`), kisisellestirilmis oneri studyosu (`/oneri/`) ve erken erisim katmanlari karsilastirma yuzeyi (`/erken-erisim/`). Studyo dort fazli (intro, questions, transition, result) bir akistir. Site tam marketplace degildir;
landing page + oneri studyosu + erken erisim yonlendirme yuzeyi mantiginda kalir. Ana kaynaklar:

- babie+ dosyaları/32-MI5.pdf
- babie+ dosyaları/babie+\_basvuru_formu.pdf
- docs/ altindaki bu dokuman paketi

Aktif teknik yapi:

- src/content/home.py
- src/templates/base.html
- src/templates/index.html
- src/templates/recommendation.html
- src/templates/early_access.html
- src/static/styles.css
- src/static/brand/
- src/static/site.webmanifest
- src/static/app.js
- build.py
- check.py
- scripts/build.py
- scripts/check.py
- .github/workflows/pages.yml
- dist/index.html
- dist/oneri/index.html
- dist/erken-erisim/index.html

V2.4 sertlestirme notlari (early access final surface):

- Site uc yuzeye ayrildi: home (`/`), oneri studyosu (`/oneri/`), erken erisim katmanlari (`/erken-erisim/`).
- Studyodaki Step 1'de gorunur "Karsilamaya don" butonu artik gercek bir UI kontrolu (yalnizca JS branch'i degil).
- Studyo no-JS fallback'i artik gercek calisir: intro/transition/result `display: none`, questions fazi tamamen stack edilmis fieldset'ler olarak goruntulenir; `data-studio-initial-hidden="true"` taşıyan node'lar JS aktif olduğunda hydrate edilir.
- Result reveal sonrasi birincil CTA artik FAQ degil `/erken-erisim/` rotasina gider; result olusunca stüdyo durumunun snapshot'i (choice + packageName + summary + savedAt) sessionStorage'a yazilir.
- Result ekraninda "Secimleri duzenle" mevcut secimi korur; "Bastan basla" formu varsayilanlara dondurur ve `babie:studio-snapshot` snapshot'ini temizler.
- `/erken-erisim/` sayfasi:
  - intro + transparency notu + studyo context ribbon + 3 featured kart karsilastirma + kisa durust not + dürüst sonraki adim CTA'lari icerir.
  - canli fiyatlandirma, checkout, abonelik, satin alma veya kargo akisi içermez.
  - kartlar Tanisma Katmani / Cekirdek Erken Erisim / Genisleyen Cerceve olarak kalir; her kart ust pill, buyuk sonuc/vurgu satiri, tek CTA ve checklist tasir.
  - JS yokken context ribbon gizli, neutral default metin gorunur; server tarafinda `core` karti secili ve kisa durust notu dolu gelir, placeholder cizgileri kullaniciya gorunmez.
  - kart article'i pasiftir; kart icindeki tek `<button type="button">` secim kontroludur, `aria-pressed` ile secili state'i ifade eder ve kisa durust not panelini gunceller.
  - sessionStorage snapshot varsa context ribbon stüdyo paket adi+ozeti gosterir; tona gore deterministic mapping (starter -> Tanisma, daily/balance -> Cekirdek, gift -> Genisleyen) ile uygun karta "Sana yakin gorunuyor" badge'i ekler, ilk render bu kartla baslar ve featured gorunum o karta tasinir.
- Featured kart gorunumu ortadaki karta sabitlenmez; secili tier hangisiyse koyu Sky Deep yuzeyi o kart alir.
- Truth-safe yasak liste genisletildi: "ai analiz ediyor", "ai takip ediyor", "premium'u yükselt", "premium'u seçin", "aboneliginiz basladi", "teslimat tarihi", "kargoya verildi", "ilk kutunuz hazirlaniyor" vb.
- scripts/check.py artik uc sayfayi ayri ayri dogrular: home/no-studio guard, recommendation phase machine guard'lari (intro start, 4 phase, transition aria-live, result tabindex+aria-live, edit+restart, step-1 back-to-intro, primary CTA -> /erken-erisim/), early access surface guard'i (3 tier card, server-render default selection, focus-label slotlari, dynamic selected badge, snapshot preselect/featured JS guard, context fallback, tek CTA-button secim modeli, no-form, no-submit-button, marketplace dili yok), no-JS nav guard, sticky-cta mobile guard, snapshot restart guard, markdown geneli PDF yol taramasi ve truth-safe copy guard.
- scripts/build.py ve scripts/check.py artik `BABIE_SITE_BASE_PATH` ile calisabilir; boylece repo ana alaninda (`/`) ve GitHub Pages proje alt yolunda (`/repo-adi/`) ayni kaynaklardan dogru linkler uretilir ve dogrulanir.
- Build sonunda `dist/.nojekyll` de uretilir; `.github/workflows/pages.yml` Python build + check + Pages deploy artifact akisini tanimlar.

Yerel komutlar:

```bash
.venv/bin/python build.py
.venv/bin/python check.py
```

GitHub Pages proje yolu simulasyonu gerekiyorsa:

```bash
BABIE_SITE_BASE_PATH=/babie-web/ .venv/bin/python build.py
BABIE_SITE_BASE_PATH=/babie-web/ .venv/bin/python check.py
```

Siteyi tarayicida yerel olarak acmak icin docs/19_SITEYI_CALISTIRMA_TR.md izlenebilir.

Yeni bagimlilik eklenmedi; Jinja2 mevcut requirements.txt uzerinden kullanilir.

Brand asset workflow notu:

- Marka assetleri `src/static/brand/` altinda zemin baglamina gore tutulur; acik yuzeyler icin `on-light`, koyu yuzeyler icin `on-dark` lockup ve mark dosyalari kullanilir.
- Header ve diger acik yuzeyler `babie-plus-lockup-on-light.png`, footer ve koyu yuzeyler `babie-plus-lockup-on-dark.png` kullanir.
- Tekrari azaltmak icin tam lockup butun section'lara dagitilmaz; gerekiyorsa kontrollu bir kompozisyonda yalnizca mark versiyonu kullanilir.
- Kare tile assetleri UI lockup yerine gecmez; favicon, apple-touch-icon, manifest ve benzeri icon katmanlarinda kalir.

Bu nedenle ilk gorev sifirdan ama kontrollu sekilde baslamaktir.

## 2. Once Okunmasi Gerekenler

Babie+ icin frontend gelistirme yapacak kisi veya AI once su kaynaklari okumali:

1. AGENTS.md
2. docs/README.md
3. docs/15_VISUAL_DIRECTION_LOCK_TR.md
4. docs/14_TRUTH_AUDIT_TR.md
5. docs/01_SITE_FOUNDATION_TR.md
6. docs/02_WIREFRAMES_TR.md
7. docs/05_HOMEPAGE_COPY_TR.md
8. docs/18_DOC_UPDATE_PROTOCOL_TR.md
9. babie+ dosyaları/32-MI5.pdf
10. babie+ dosyaları/babie+\_basvuru_formu.pdf

## 3. Temel Calisma Ilkesi

Babie+ icin ilk web surumu su sekilde dusunulmelidir:

- tam e-ticaret degil
- landing page + oneri studyosu + erken erisim cercevesi mantigi
- trust-first
- mobile-first
- conversion-aware

Ana hedef:

- kullaniciya ilk ziyaretinde projeyi net anlatmak
- onu kisisellestirilmis oneri studyosuna yonlendirmek

Ek sabit kural:

- repo geneli icin kisa davranis cercevesi AGENTS.md tarafindan verilir
- daha detayli kararlar docs/ altindaki markdown dosyalarinda tutulur

## 4. Ne Zaman Concept-First Calisilmali

Asagidaki durumlarda once section seviyesinde tasarim brief'i veya concept spec'i cikarilmalidir:

- sifirdan ana sayfa kurulacaksa
- gorsel yon ilk kez uygulanacaksa
- markanin fotograflama, typography ve component dili oturmamis ise

Asagidaki durumlarda dogrudan kod uzerinden iteratif ilerlemek daha dogrudur:

- spacing ve layout polish'i
- form akisi iyilestirmeleri
- CTA netligi
- SSS, footer veya yardimci section duzeltmeleri

## 5. KIlit Frontend Hedefleri

AI veya gelistirici her degisiklikte su hedefleri gtmeli:

## 5.1 Trust-First Netlik

- ilk ekran urunun ne oldugunu net anlatmali
- fazla jargon veya iddia kullanilmamali
- kisisellestirme mantigi sakin bir sekilde gorunmeli

## 5.2 Donusum Netligi

- header, hero ve final CTA ayni ana aksiyona baglanmali
- birincil aksiyon kisisellestirilmis oneri studyosuna yonlendirme olmali
- ikincil CTA ana aksiyonu zayiflatmamali

## 5.3 Premium ve Sicak Ton

- ana ton Calm Premium Care
- cok siradan startup tasarimina kacilmamali
- fazla bebeksi veya fazla tip sal gorunmemeli

## 5.4 Mobil Okunurluk

- hero copy bloklari kisa tutulmali
- form alanlari buyuk ve rahat olmali
- kartlar mobilde nefes alacak sekilde kirilmali

## 5.5 Truth-Safe Copy

- yeni copy eklenirse docs/14 ile hizali olmali
- aktif olmayan AI, topluluk veya lojistik kabiliyetleri varmis gibi yazilmamali

## 6. Yapilmasi Iyi Olan Seyler

Bu repo icin iyi hareketler:

- once tasarim tokenlari ve ana sayfa section sistemi kurmak
- landing page'i tek bir guclu hikaye halinde yazmak
- oneri studyosunu az ama anlamli secimle yormayan yapida tasarlamak
- hafif animasyonlarla kaliteli ama sakin bir deneyim vermek
- urun mantigini gorsel panellerle sade sekilde anlatmak

## 7. Yapilmamasi Gereken Seyler

Bu repo icin yapilmamasi gerekenler:

- ilk turda tam marketplace kurmak
- sahte testimonial uydurmak
- olmayan uygulama ekranlarini gercek urun gibi gostermek
- purple-on-white SaaS sablonuna dusmek
- sadece sevimli bebek fotografi galerisi uretmek
- hero'yu uzun metin duvarina cevirmek
- formu tek ekranda yorucu hale getirmek

## 8. Onerilen Uygulama Sirasi

1. Dokumanlari oku.
2. Basit proje iskeletini kontrol et veya gerekirse kucuk tutarak genislet.
3. Tasarim tokenlarini src/static/styles.css icinde tutarli kullan.
4. Home page sirasini koru: hero -> problem -> nasil calisir -> kutu -> guven -> hedef deneyim -> FAQ -> final CTA (bridge teaser) -> footer.
5. Backend baglanmadigi surece studyoyu gercek form submit gibi kurma; submit'i blokle, URL'ye yazma, sahte odeme veya siparis hissi verme. Studyo `/oneri/` sayfasinda yasar.
6. Erken erisim sayfasinda (`/erken-erisim/`) form, input veya submit-capable buton kurma; sayfa karsilastirma kartlari ana deneyimi tasimali, alttaki not kisa kalmali, fiyat/odeme/abonelik dili icermemelidir.
7. Mobil nav ve reveal davranislarini progressive enhancement mantiginda tut; studyoda no-JS fallback olarak intro/transition/result fazlari gizlenir, questions fazi tamamen stack edilmis fieldset'ler olarak kalsin.
8. Build ve check komutlarini calistir; uc page (`dist/index.html`, `dist/oneri/index.html`, `dist/erken-erisim/index.html`) uretiminin gectigini gor.
9. GitHub Pages hedefleniyorsa ayni build/check akisini bir kez `BABIE_SITE_BASE_PATH=/repo-adi/` ile de calistir; subpage CTA ve home anchor linklerinin repo alt yoluna dondugunu gor.
10. Check ciktisinda home/no-studio guard, recommendation phase guard'lari, early-access tier guard, no-JS nav, sticky-cta mobile, PDF yolu ve truth-safe copy guard'larinin gectigini dogrula.
11. Brand degisikligi varsa favicon, touch icon, manifest ve header/footer lockup secimlerinin zemin kontrastiyla uyumlu oldugunu kontrol et.
12. Truth audit ile public copy taramasi yap.
13. Deploy gerekiyorsa `.github/workflows/pages.yml` uzerinden GitHub Actions run'inin basarili oldugunu kontrol et.
14. Sonra ilave bir yuzey gerekiyorsa ayni multi-page disiplinle ekle.

## 9. Dogrulama Checklist'i

- ilk ekran 5 saniyede anlasiliyor mu?
- ana CTA net mi?
- mobilde okunurluk korunuyor mu?
- form anlasilir mi?
- copy truth audit ile uyumlu mu?
- gorsel yon visual direction lock ile tutarli mi?
- yapilan kod degisikligi docs/18'e gore gerekli markdown guncellemesini aldi mi?
- yapilan degisiklik AGENTS.md icindeki repo geneli talimatlari etkiliyor mu?

## 10. Sonuc

Babie+ reposunda ilk frontend calismasi, buyuk sistem kurma hevesiyle degil; dogru hikaye, guvenli ton ve net donusum mantigiyla ilerlemelidir. Quadrix'ten alinacak esas fayda kod kalibi degil, disiplinli docs ve guardrail mantigidir.

Ek kural: Her anlamli kod degisikliginden sonra docs/18_DOC_UPDATE_PROTOCOL_TR.md dikkate alinmali ve etkilenen markdown dosyalari ayni turda guncellenmelidir.
