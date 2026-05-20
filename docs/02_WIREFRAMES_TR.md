# Babie+ Web Wireframe Dokumani

## 1. Dokumanin Amaci

Bu belge, babie+ web sitesinin dusuk sadakat yerlesim planini tanimlar.

Buradaki wireframe'ler gorsel tasarim degildir. Asagidaki sorulara cevap verir:

- Hangi icerik hangi sirada gelmeli?
- Kullanici ilk ekranda ne gormeli?
- CTA'lar nereye yerlestirilmeli?
- Mobil ve masaustunde hangi bloklar korunmali?

## 2. Kullanim Kurallari

- Her section tek bir soruya cevap vermeli.
- Her ekranda tek bir ana aksiyon baskin kalmali.
- Ilk ekran guven ve faydayi ayni anda anlatmali.
- Gorseller dekor degil, urun mantigini aciklayan destekleyici kanit olmali.

## 3. Global Yapi

## 3.1 Header

Masaustu:

```text
+------------------------------------------------------------------------------------------------+
| LOGO | Nasil Calisir | Kutu Mantigi | Guven | SSS | CTA: Kisisellestirilmis Oneriyi Gor    |
+------------------------------------------------------------------------------------------------+
```

Mobil:

```text
+--------------------------------------------------+
| LOGO                          Menu | Onizleme    |
+--------------------------------------------------+
```

Header notlari:

- CTA her zaman gorunur kalmali.
- Mobilde menu sade olmali.
- JS kapali durumda mobil navigasyon baglantilari erisilebilir kalmali.
- Header fazla kategori yuklememeli.

## 4. Ana Sayfa Wireframe

## 4.1 Masaustu

```text
+------------------------------------------------------------------------------------------------+
| HEADER                                                                                         |
+------------------------------------------------------------------------------------------------+
| HERO COPY                                   | HERO VISUAL                                      |
| Babie+ ne yapiyor?                          | Yumusak editorial urun/gorsel paneli             |
| Kisa aciklama                               | Profil karti veya kutu mantigi onizlemesi        |
| [Oneriyi Gor] [Nasil Calisir]               |                                                  |
+------------------------------------------------------------------------------------------------+
| PROOF STRIP                                                                                   |
| Yas odakli secim | Hassasiyet notlari | Tekrarli ihtiyac akisi | Guven odakli secki         |
+------------------------------------------------------------------------------------------------+
| PROBLEM CARDS                                                                                 |
| Karar zorlugu | Eksik urun stresi | Guvensiz bilgi ortami                                     |
+------------------------------------------------------------------------------------------------+
| NASIL CALISIR                                                                                |
| 1 Profil olustur | 2 Uygun kutu mantigi | 3 Surekli destek                                     |
+------------------------------------------------------------------------------------------------+
| ORNEK KUTU / ICERIK MANTIGI                                                                   |
| Sol: kutu gorseli veya icerik yerlesimi | Sag: neden bu kutu herkese ayni degil anlatimi     |
+------------------------------------------------------------------------------------------------+
| NEDEN GUVENILIR                                                                              |
| Sertifika odagi | Acik kriterler | Sade veri toplama | Kullaniciyi yormayan akis             |
+------------------------------------------------------------------------------------------------+
| HEDEF DENEYIM                                                                                |
| Daha az arastirma | Daha az unutma | Daha sakin tekrar siparis                               |
+------------------------------------------------------------------------------------------------+
| FAQ PREVIEW                                                                                  |
| 4-5 soru                                                                                      |
+------------------------------------------------------------------------------------------------+
| ILETISIM                                                                                     |
| "Babie+ ile sakin ve dogrudan iletisime gecin"                                               |
| [Instagram karti] + [E-posta karti]                                                          |
+------------------------------------------------------------------------------------------------+
| FOOTER                                                                                       |
+------------------------------------------------------------------------------------------------+
```

V2 uygulama notu (multi-page IA):

- Site iki yuzeyden olusur: home page (`/`) ve ayri kisisellestirilmis oneri studyosu (`/oneri/`).
- Home page bu sirayi korur: Header, Hero, proof strip, Problem, Nasil Calisir, Ornek Kutu, Guven, Hedef Deneyim, SSS, Iletisim, Footer.
- Hero visual gercek fotograf veya sahte uygulama ekrani kullanmaz; profil ve kutu mantigini CSS tabanli editorial panel ile anlatir.
- Son alan artik bridge teaser degildir; Instagram ve e-posta kanallarini gosteren iletisim panelidir.
- Mobil hero'da copy ve CTA, gorsel panelden once gelir.
- Header CTA, hero birincil CTA ve mobil sticky CTA `/oneri/` rotasina baglidir.
- Mobil sticky CTA ilk ekranda hero CTA'yi tekrar etmez; scroll sonrasinda destek aksiyonu olarak gorunur ve iletisim/footer gorunurken otomatik gizlenir.
- Sticky CTA, mobil menu acikken, iletisim bolumu veya footer gorunurken otomatik gizlenir; kullanici yukari donerse dogru state'e geri doner. Subpage'lerde sticky CTA render edilmez.
- V2.7 itibarıyla iletisim alanı kompakt bir list-row modulu olarak calisir: kucuk eyebrow ikonu, kucultulmus baslik, kisa lede + sakin pill not, sol-ikon + ortada label/text/note + sag yon oku tasiyan iki ince kanal karti. Ayri bir contact hero, dev rounded-square medya alani, sahte form veya iframe kullanilmaz; mobilde tek kolon, 32px ikon ve dar padding'le calisir.
- `dist/index.html`, `src/templates/index.html` kaynagindan; `dist/oneri/index.html`, `src/templates/recommendation.html` kaynagindan uretilir; nihai HTML elle tek basina duzenlenmez.

Oneri studyosu (`/oneri/`) wireframe ozetı (V2.2 — phase machine):

```text
+--------------------------------------------------------------------------+
| HEADER (sag CTA: Ana sayfaya don)                                        |
+--------------------------------------------------------------------------+
| FAZ RAIL: 01 Karsilama | 02 Sorular | 03 Derleme | 04 Oneri              |
+--------------------------------------------------------------------------+
| FAZ 0 - KARSILAMA (intro)                                                |
| Eyebrow: Oneri studyosu                                                  |
| H1: Bebeginizin donemine uygun paket cercevesini birlikte hazirlayalim   |
| Kisa aciklama + transparency notu                                        |
| CTA: "Oneriyi birlikte olusturalim" + akis hint                          |
+--------------------------------------------------------------------------+
| FAZ 1 - SORULAR (questions)                                              |
| Adim X / 4 + ilerleme bari (gradient fill)                               |
| Tek seferde bir adim gorunur (legend: Adim 0X · Etiket)                  |
| Soru                                                                     |
| Hint                                                                     |
| Radio chip secimleri                                                     |
| [Geri]                                                  [Devam / Goster] |
+--------------------------------------------------------------------------+
| FAZ 2 - DERLEME (transition, aria-live polite)                           |
| Eyebrow: Hazirlaniyor                                                    |
| H2: Secimleriniz bir araya getiriliyor                                   |
| 3 satirlik akis listesi (stagger ile aydinlanir)                         |
| Reduced-motion: tum satirlar anlik, sonra result faz acilir              |
+--------------------------------------------------------------------------+
| FAZ 3 - ONERI (result, aria-live polite, focusable)                      |
| Eyebrow: Sonuc                                                           |
| Paket adi (Fraunces serif, rise animation)                               |
| "Bugun bize anlattiginiz cerceve" intro line + ozet                      |
| Simdiye kadar sectikleriniz: 4 satirlik chip listesi                     |
| Paket katmanlari (4 layer)                                               |
| Neden bu oneri (rationale)                                               |
| Dikkat notu                                                              |
| Sonraki adim CTA'lari (FAQ, Nasil Calisir, Ana sayfa)                    |
| [Secimleri duzenle]   [Bastan basla]                                     |
+--------------------------------------------------------------------------+
| FOOTER                                                                   |
+--------------------------------------------------------------------------+
```

## 4.2 Hero Aciklamasi

Hero'in amaci:

- babie+'in ne yaptigini ilk 5 saniyede anlatmak
- ebeveyni sakin, guvenli ve premium bir deneyimle karsilamak
- ana aksiyon olarak kisisellestirilmis oneri studyosuna yonlendirmek

Hero icerigi:

- kisa bir ana baslik
- kisa bir aciklama
- birincil CTA
- ikincil CTA
- kisisellestirme mantigini gosteren sade bir gorsel panel

## 4.3 Problem Bolumu

Bu bolum su uc aciyi hizli anlatmali:

- cok fazla secenek yuzunden karar yorgunlugu
- temel urunlerin bitisini takip etme stresi
- reklam odakli ve guvensiz bilgi akisi

## 4.4 Nasil Calisir Bolumu

Onerilen uc adim:

1. Bebek profili girilir.
2. Ihtiyaca gore kutu mantigi olusturulur.
3. Destek, tekrar siparis ve gelisim yolculugu kolaylasir.

## 4.5 Ornek Kutu Bolumu

Bu bolum tek bir sabit kutu satmiyormus gibi davranmamalidir.

Vurgu su olmali:

- icerik profil bilgisine gore sekillenir
- kutu mantigi ihtiyaca gore degisir
- urun ornegi fikir vermek icindir

## 4.6 Guven Bolumu

Bu bolumde kullanilabilecek baslik eksenleri:

- Neye gore seciyoruz?
- Neden rastgele urun onermiyoruz?
- Hangi sinirlar icinde ilerliyoruz?

## 4.7 Mobil Akis

```text
+--------------------------------------------------+
| HEADER                                           |
+--------------------------------------------------+
| HERO COPY                                        |
| Baslik                                           |
| Alt metin                                        |
| [Oneriyi Gor] [Nasil Calisir]                    |
+--------------------------------------------------+
| HERO VISUAL                                      |
+--------------------------------------------------+
| PROOF STACK                                      |
+--------------------------------------------------+
| PROBLEM CARD 1                                   |
+--------------------------------------------------+
| PROBLEM CARD 2                                   |
+--------------------------------------------------+
| PROBLEM CARD 3                                   |
+--------------------------------------------------+
| NASIL CALISIR                                    |
+--------------------------------------------------+
| ORNEK KUTU                                       |
+--------------------------------------------------+
| GUVEN                                            |
+--------------------------------------------------+
| FAQ                                              |
+--------------------------------------------------+
| STICKY CTA                                       |
+--------------------------------------------------+
| FOOTER                                           |
+--------------------------------------------------+
```

Mobil notlari:

- CTA alt sabitte dusunulebilir.
- Sticky CTA ilk yuklemede degil, kullanici sayfada ilerledikten sonra gorunmelidir.
- Kartlar asiri yogun olmamali.
- Kutu gorseli veya visual panel mobilde okunur kalmali.
- Fazla hover bagimli davranis kullanilmamali.

## 5. Oneri Studyosu Wireframe

Bu bolum eski "Onboarding Formu Wireframe" yerine konumlanmistir. Babie+ artik klasik tek sayfa onboarding formu yerine `/oneri/` sayfasinda yasayan dort fazli oneri studyosu kullanir.

## 5.1 Studyo Akisi

`/oneri/` sayfasi dort faza bolunmustur:

1. Faz 0 - Karsilama (intro)
2. Faz 1 - Sorular (questions)
3. Faz 2 - Derleme (transition)
4. Faz 3 - Oneri (result)

Detayli akis `4.7 V2.2 uygulama notu` bolumundeki sema ile aynidir.

## 5.2 Studyo Kurallari

- Studyo gercek backend baglantisi tasimaz; `<form>` kullanir fakat submit davranisini blokeler.
- Sadece radio chip secimleri vardir; serbest text, e-posta, telefon, dosya, select veya textarea bulunmaz.
- Bilgilerin tarayicidan disari cikmadigi kullaniciya transparency notuyla acikca soylenir.
- Result reveal sonrasi `/erken-erisim/` sayfasi Mevcut / Plus / Premium planlarini fiyat ve kapsamla karsilastirir.
- Plan karsilastirma sayfasi karar yuzeyidir; uc plan karti ana deneyimi tasir, alt kisimda yalnizca kisa durust not ve sonraki adim CTA'lari kalir.

V2.2 form notu (phase machine):

- Form ayri bir sayfada (`/oneri/`) yasar; gercek `<form>` kullanir fakat submit davranisini blokeler (`onsubmit="return false;"`).
- Akis dort faza bolunmustur: intro (karsilama), questions (sorular), transition (derleme), result (oneri). `data-studio-phase` attribute'u ile yonetilir.
- Intro fazi pasif bir karsilama yuzeyidir; kullanici "Oneriyi birlikte olusturalim" butonuyla soru fazina gecer, dogrudan form duvarina carpmaz.
- Soru fazinda alanlar yalnizca radio chip'tir; tek seferde bir adim gorunur, ust kisimda "Adim X/4" + gradient progress bar bulunur.
- Step 1'de gorunur "Karsilamaya don" butonu vardir; sonraki step'lerde "Geri" ile bir onceki step'e donulur.
- Transition fazi kisa bir "secimleriniz bir araya getiriliyor" gecisidir; uc satirlik bir liste yumusakca aydinlanir ve sonra result fazina otomatik gecer. Reduced-motion durumunda satirlar anlik gosterilir, gecis kisalir.
- Result fazi reveal animasyonu ile acilir; paket adi rise efektiyle gelir, secim ozeti chip listesi olarak gosterilir, "Secimleri duzenle" butonu kullaniciyi soru fazina geri dondurur.
- Result paneli birincil CTA'si artik `/erken-erisim/` sayfasina baglanir (FAQ anchor'i degil). Tiklamadan once stüdyo durumunun sessionStorage snapshot'i kaydedilir.
- Submit davranisi yoktur; bilgi kaydetmez, gondermez, URL'ye eklemez veya sayfayi yenilemez.
- No-JS fallback olarak intro/transition/result fazlari gizlenir, butun fieldset'ler stack edilmis sekilde gorunur ve dogrudan kullanilabilir; submit yine yoktur.
- Sonuc paneli `aria-live="polite"` ile guncellenir ve `tabindex="-1"` ile odaklanabilir; reveal aninda focus result heading'ine tasinir.
- Phase rail (4 etap) her zaman gorunur: aktif faz `is-current`, gecilen fazlar `is-complete`.

## 6. Erken Erisim Karsilastirma Yuzeyi

`/erken-erisim/` sayfasi result reveal sonrasi acilan ucuncu yuzeydir. Wireframe ozetı:

```text
+--------------------------------------------------------------------------+
| HEADER (sag CTA: Ana sayfaya don)                                        |
+--------------------------------------------------------------------------+
| INTRO                                                                    |
| Eyebrow: Erken erisim cercevesi                                          |
| H1: Bebek ihtiyaclariniz icin en uygun Babie+ planini secin              |
| Kisa aciklama + fiyat/checkout siniri notu                               |
+--------------------------------------------------------------------------+
| CONTEXT RIBBON (sessionStorage snapshot varsa)                           |
| "Az once stüdyoda olusturdugunuz oneri: <packageName>"                   |
| Kisa ozet + "Size daha yakin gorunen plan" satiri                        |
+--------------------------------------------------------------------------+
| THREE-CARD COMPARISON                                                    |
| Mevcut              | Plus (varsayilan featured) | Premium               |
| 0 TL                | 799 TL / 15 Gun            | 1199 TL'den baslar   |
| Plan subhead + guclu CTA + 4-5 madde checklist                           |
+--------------------------------------------------------------------------+
| COMPACT HONEST NOTE (secili plan degistikce guncellenir, aria-live)      |
| Secilen planin neyi temsil ettigini ve sinirini kisa anlatir             |
+--------------------------------------------------------------------------+
| HONEST NEXT STEPS                                                        |
| Oneri studyosuna don | Nasil calisir | SSS | Babie+ ana sayfa            |
+--------------------------------------------------------------------------+
| FOOTER                                                                   |
+--------------------------------------------------------------------------+
```

V2.5 plan karsilastirma notu:

- Sayfa fiyat ve plan karsilastirmasidir; fiyat gostermek serbesttir fakat sahte checkout, kargo/teslimat tarihi, stok, AI takip, dinamik fiyatlandirma, topluluk rozeti veya uzman onayi iddiasi kullanilmaz.
- Uc kart: Mevcut / Plus / Premium. Plus karti snapshot yokken varsayilan featured plandir.
- Secili plan hangisiyse koyu featured gorunum ona tasinir; snapshot Mevcut veya Premium onerirse featured gorunum o karta gecer.
- Kullanici kartlardan birini sectiginde alttaki kisa durust not paneli sakin bir gecisle guncellenir; ana bilgi yukunu kartlar tasir.
- sessionStorage snapshot varsa (`babie:studio-snapshot`), context ribbon stüdyo paket adi ve ozetini gosterir; tona gore deterministic plan mapping ile uygun karta "Sana uygun" badge'i eklenir ve ilk render bu planla baslar.
- Snapshot yoksa context ribbon gizlenir, default karsilastirma metni gosterilir ve ilk render server tarafinda `default_plan` (plus) icerigiyle baslar; JS olmadan placeholder cizgileri gorunmez.
- Kart article'i pasiftir; tek secim kontrolu kart icindeki gercek `<button type="button">` olur ve secili state `aria-pressed` ile ifade edilir. Submit-capable buton, input veya form yoktur.

## 7. Sonuc

Babie+ wireframe mantigi, urun katalogu gostermekten cok karar kolaylastirma vaadini anlatmak uzerine kurulmalidir. Ilk deneyim, sevimlilikten cok netlik ve guven uretmelidir.
