# Babie+ Web Sitesi Temel Plani

## 1. Dokumanin Amaci

Bu belge, babie+ web sitesinin ilk stratejik temelini tanimlar.

Buradaki hedef su sorulari erken asamada netlestirmektir:

- Site neyi anlatacak?
- Kime anlatacak?
- Ilk surumde hangi aksiyonu aldiracak?
- Hangi sayfalar veya section'lar gerekli?
- Hangi teknik ve icerik yaklasimi dogru olur?

Bu belge, siteyi tam kapsamli bir e-ticaret vitrini olarak degil; guven veren, kisisellestirme mantigini anlatan ve kisisellestirilmis oneri studyosuna yonlendiren bir erken asama urun vitrini olarak ele alir.

## 2. Site Neden Var?

Babie+ sitesinin ilk gorevi, projeyi ilk kez goren bir ebeveyne su uc sorunun cevabini hizli vermektir:

1. babie+ ne yapiyor?
2. Neden faydali?
3. Ben simdi ne yapmaliyim?

Bu nedenle site ayni anda su rolleri tasimalidir:

- Marka vitrini
- Guven yuzeyi
- Donusum araci
- Oneri studyosu girisi
- Gelecekteki dijital ekosistem icin temel zemin

## 3. Marka Konumlandirmasi

## 3.1 Ana Marka Cekirdegi

Babie+, 0-24 aylik bebegi olan ebeveynler icin urun secimini ve tekrar siparis surecini kolaylastirmayi hedefleyen bir ebeveyn destek platformudur.

Ana fark su cizgide anlatilmalidir:

- urun bollugu icinde kaybolmayi azaltir
- kisisellestirme mantigi sunar
- tekrar eden temel ihtiyaclari daha yonetilebilir hale getirmeyi hedefler
- zaman, zihinsel yuk ve guven problemini birlikte ele alir

## 3.2 Hero Seviyesinde Verilecek Duygu

Hero, su duyguyu vermelidir:

- Daha az arastirma
- Daha az kafa karisikligi
- Daha fazla guven
- Daha sakin ebeveyn deneyimi

## 3.3 Hero Seviyesinde Verilmemesi Gereken Duygu

- Rastgele sevimli bebek magazasi
- Steril tip teknoloji paneli
- Hazir olmayan buyuk e-ticaret platformu
- Yalnizca "AI" kelimesiyle guven isteyen jenerik bir SaaS urunu

## 4. Hedef Kitle Segmentleri

## 4.1 Birincil Kitle

Yeni ebeveynler, ozellikle 0-6 ay araliginda bebegi olan aileler.

Neden:

- satin alma davranisi yeni olusuyor
- karar yukleri yuksek
- dogru yonlendirme ihtiyaci en guclu bu donemde

## 4.2 Ikincil Kitle

Calisan anneler ve zaman baskisi altindaki aileler.

Neden:

- tekrarli ihtiyaclari manuel yonetmek daha zor
- kolaylik ve duzen onlar icin premium bir degerdir

## 4.3 Ucuncul Kitle

Organik ve premium urun arayan ebeveynler.

Neden:

- urun kalitesi ve guven onlar icin fiyat kadar onemlidir
- uzun vadeli baglilik potansiyeli yuksektir

## 4.4 Tamamlayici Kitle

Yeni dogum donemi icin hediye kutusu arayan kullanicilar.

## 5. Donusum Hedefleri

## 5.1 Birincil Donusum

- Kisisellestirilmis oneri studyosunu deneyimleme

## 5.2 Ikincil Donusum

- Nasil calistigini inceleme
- Ornek kutu icerigini gorme
- SSS bolumune inme

## 5.3 Ucuncul Donusum

- Takimi tanima
- Ileride gelecek topluluk ve destek modelini anlama

## 6. Basari Olcumleri

Ilk surum icin takip edilmesi gereken temel KPI'lar:

- Hero birincil CTA tiklama orani
- Oneri studyosu baslatma orani
- Oneri sonuc fazina ulasma orani
- Plan karsilastirma sayfasina gecis orani
- Mobilde scroll derinligi
- SSS acma orani
- Ornek kutu veya nasil calisir section'ina erisim

## 7. Bilgi Mimarisi

## 7.1 Ilk Surum Site Modeli

En dogru baslangic, tek bir guclu landing page, ayri bir oneri studyosu ve fiyat/kapsam bilgisini acik veren plan karsilastirma yuzeyi ile ilerlemektir.

Onerilen ilk set:

- Ana sayfa
- Ayrik kisisellestirilmis oneri studyosu sayfasi
- Ayrik Mevcut / Plus / Premium plan karsilastirma sayfasi
- Ana sayfada sade iletisim kapanisi
- Gerekiyorsa ikinci adimda gizlilik yuzeyi

V2.5 uygulama notu (plan comparison final surface):

- Site uc yuzeyden olusur: trust-first landing page (`/`), kisisellestirilmis oneri studyosu (`/oneri/`) ve Mevcut / Plus / Premium plan karsilastirma yuzeyi (`/erken-erisim/`).
- Home page son bolumu artik bridge teaser degil; Instagram ve e-posta kanallarini gosteren iletisim kapanisidir.
- Header CTA, hero birincil CTA ve mobil sticky CTA `/oneri/` rotasina baglidir.
- Iletisim kapanisi siparis, odeme veya otomatik basvuru akisi baslatmaz; yalnizca `@babieplus` Instagram hesabi ve `babieplus@gmail.com` e-postasini gosterir.
- `/oneri/` sayfasi dort faza bolunmustur: intro (karsilama), questions (sorular), transition (derleme), result (oneri). Step 1'de gorunur "Karsilamaya don" butonu vardir.
- Result reveal sonrasi birincil CTA artik FAQ degil `/erken-erisim/` sayfasina gider; result olusunca stüdyo durumunun sessionStorage snapshot'i kaydedilir.
- "Secimleri duzenle" mevcut secimi korur; "Bastan basla" formu varsayilanlara dondurur ve onceki `babie:studio-snapshot` kaydini temizler.
- `/erken-erisim/` uc kartli fiyat/plan karsilastirma yuzeyidir: Mevcut, Plus, Premium.
- Fiyatlar ve plan kapsam maddeleri kartlarin ana karar alanidir; buyuk fiyat satiri, CTA ve checklist tek bakista okunur.
- Snapshot varsa context ribbon stüdyo paket adi+ozeti gosterir, tona gore deterministic mapping ile uygun plana "Sana uygun" badge'i eklenir ve secili/featured gorunum o plana tasinir.
- Snapshot yoksa context ribbon JS beklemeden gizli kalir, neutral default metin gorunur ve server tarafinda `plus` plani secili render edilir.
- Plan kartlarinda article pasif kalir; secim yalnizca kart icindeki `<button type="button">` ile yapilir ve secili durum `aria-pressed` + kart icindeki secili badge ile ifade edilir.
- Eski buyuk detail panel ana odak degildir; kartlarin altinda yalnizca secili plani aciklayan kisa durust not paneli kalir.
- Sadece radio chip secimleri vardir; serbest text, e-posta, telefon, dosya, select veya textarea gibi sahte form izleri yoktur.
- Truth-safe dil korunur: "AI karar verdi", "akilli motor", "doktor onayli", "aboneliginiz basladi", "teslimat tarihi", "dinamik fiyatlandirma", "topluluk rozeti" gibi iddialar yoktur. Fiyat ve plan adi serbesttir; sahte checkout veya operasyon taahhudu degildir.
- Bilgilerin tarayici disina gitmedigi, kaydedilmedigi ve URL'ye eklenmedigi kullaniciya stüdyo girisinde acikca soylenir; sessionStorage snapshot yalnizca sekme suresince kullanilir.
- Stüdyoda no-JS fallback gercek calisir: intro/transition/result fazlari gizlenir, questions fazi tamamen stack edilmis fieldset'ler olarak gorunur ve dogrudan kullanilabilir; submit yine yoktur.
- Stüdyo ve plan karsilastirma sayfalarinda nav linkleri home anchor'larina (`/#nasil-calisir`, `/#guven`, `/#sss` vb.) doner; header sag CTA'si "Ana sayfaya don" olur.
- Mobil ilk ekranda copy ve CTA, gorsel panelden once gelerek "ne yapiyor, neden faydali, simdi ne yapmaliyim" sorularini daha hizli cevaplar.

## 7.2 Ana Sayfa Cevap Sirasi

Ana sayfa kullaniciya su sirayla cevap vermelidir:

1. Babie+ hangi sorunu cozmeye calisiyor?
2. Nasil calisiyor?
3. Neye gore kisisellestiriyor?
4. Neden guvenilir gorunmeli?
5. Ilk adim olarak ne yapmaliyim?

## 7.3 Ana Sayfada Olmasi Gereken Section'lar

- Hero
- Problem alanlari
- Nasil calisir
- Ornek kutu / ornek icerik mantigi
- Guven katmani
- Hedeflenen ebeveyn deneyimi
- SSS
- Iletisim kapanisi

## 8. Icerik Mimarisi

## 8.1 Yonetilecek Icerik Tipleri

- Hero basliklari
- CTA metinleri
- Problem kartlari
- Nasil calisir adimlari
- Ornek kutu icerigi
- SSS maddeleri
- Takim veya guven unsurlari
- Form alanlari

## 8.2 Zorunlu Veri Alanlari

Oneri mantiginda bugun veya ileride degerlendirilebilecek temel alanlar:

- Bebegin ay bilgisi
- Kilo bilgisi
- Hassasiyet veya alerji notlari
- Oncelikli urun kategorileri
- Iletisim bilgisi
- Teslimat sehri veya bolgesi

## 9. Teknik Yakit

## 9.1 Ilk Teknik Yapi

Ilk surum icin en dogru yaklasim:

- hizli acilan statik veya hafif hibrit landing page
- guclu tipografi ve token tabanli CSS sistemi
- gerektiginde form entegrasyonu
- mobil once tasarim

V2 teknik karsilik:

- Jinja2 tabanli statik build (multi-page)
- src/templates kaynaklari (`base.html`, `index.html`, `recommendation.html`, `early_access.html`)
- src/content/home.py icinde `HOME`, `RECOMMENDATION` ve `EARLY_ACCESS` veri yapilari, `NAV` slug listesi
- src/static/styles.css ve src/static/app.js (paylasimli)
- Kokteki `build.py` ve `check.py` wrapper'lari ile kisa yerel komut akisi
- scripts/build.py ile `dist/index.html`, `dist/oneri/index.html` ve `dist/erken-erisim/index.html` uretimi (asset_prefix ile relative path yonetimi)
- scripts/check.py ile multi-page output, home/no-studio guard, recommendation studio guard, plan comparison guard, no-JS nav guard, sticky-cta mobile guard, PDF yolu ve truth-safe copy guard kontrolu

## 9.2 Ilk Surumde Yapilmamasi Gerekenler

- tam kapsamli pazar yeri
- yuzlerce urun listeleme
- agir hesap paneli kurgusu
- gereksiz dashboard hissi
- dogrulanmamis AI demosu

## 10. Sonuc

Babie+ icin ilk site, urun karmasini buyutmek yerine ebeveynin karar yukunu azalttigini gostermelidir. Baslangic noktasi buyuk bir e-ticaret yapisi degil; net, premium ve guven veren bir landing page, ayri oneri studyosu ve durust bir erken erisim cercevesi olmalidir.
