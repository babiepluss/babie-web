# Babie+ Truth Audit

## 1. Dokumanin Amaci

Bu belge, babie+ sitesinde kullanilacak dilin proje gercegiyle uyumlu kalmasini saglar.

Amac su uc soruyu netlestirmektir:

- Hangi iddialar bugun guvenle soylenebilir?
- Hangi iddialar sadece daha dikkatli bir dille kullanilabilir?
- Hangi iddialardan simdilik tamamen kacinilmalidir?

## 2. Kullanim Kurali

Yeni bir public copy satiri yazilmadan once su filtre uygulanmalidir:

- Safe Now
- Conditional Wording
- Avoid

Bu uc gruptan birine girmeyen ifade, yayina alinmamalidir.

## 3. Safe Now

Asagidaki iddialar, mevcut proje belgelerine gore guvenle kullanilabilir:

- Babie+, 0-24 aylik bebekleri olan ebeveynlere odaklanan bir ebeveyn destek platformudur.
- Proje, bebek urunu secimi ve tekrarli ihtiyac yonetimi sirasinda olusan karar yukunu azaltmayi hedefler.
- Kisisellestirilmis kutu modeli, yas, gelisim evresi ve hassasiyet gibi bilgilere gore sekillenmeyi hedefler.
- Proje; abonelik kutusu, destek deneyimi ve daha guvenli yonlendirme mantigini bir araya getirmeyi amaclar.
- Erken asama web sitesi, oneri studyosu deneyimi, aciklama ve fiyatli plan karsilastirma yuzeyi olarak konumlanabilir.

## 4. Conditional Wording

## 4.1 AI Dili

Guvenli dil:

- AI destekli altyapi hedefi
- veri destekli karar mantigi
- kural tabanli baslayip gelisecek kisisellestirme modeli

Kacin:

- bugun tam calisan yapay zeka asistani
- urun bitmeden once kusursuz tahmin yapan aktif sistem
- hazir ve yayinda akilli motor

## 4.2 Topluluk Dili

Guvenli dil:

- ebeveyn toplulugu hedefi
- guvenilir bilgi ve deneyim paylasimi icin tasarlanan katman
- ileride acilacak topluluk yapisi

Kacin:

- aktif buyuk topluluk
- uzman moderasyonlu canli platform yayinda
- bugun isleyen sosyal topluluk ekosistemi

## 4.3 Urun Kalitesi ve Onay Dili

Guvenli dil:

- organik odakli secki
- sertifika ve guven kriterlerine dayali secim hedefi
- kalite ve icerik standardina oncelik veren yaklasim

Kacin:

- doktor onayli tum urunler
- tip otoriteleri tarafindan resmi olarak onaylanmis platform
- tamamen risksiz urun deneyimi

Not:

Public sitede onay veya sertifika adi kullanilacaksa belgeye dayali olmali.

## 4.4 Kendi Marka Dili

Guvenli dil:

- uzun vadeli marka hedefi
- ileride gelistirilmesi planlanan kendi urun katmani

Kacin:

- kendi marka urunler aktif satista
- marka lansmani tamamlandi

## 4.5 Lojistik ve Kullanima Aciklik Dili

Guvenli dil:

- erken erisim cercevesi
- plan karsilastirma yuzeyi
- kademeli acilis plani

Kacin:

- tum Turkiye'de aktif hizmet
- sorunsuz ve anlik ulasim
- her yerde kullanima hazir abonelik modeli

## 4.6 Veri ve Guvenlik Dili

Guvenli dil:

- gerekli verileri acikca isteme
- kullaniciya neden bilgi toplandigini anlatma
- veri surecini acik ve sade kurma hedefi

Kacin:

- tum veriler eksiksiz hukuki uyumla bugun korunuyor iddiasi
- tam KVKK uyumu tamamlandi ifadesi, gercekten hazir degilse

## 5. Avoid

Asagidaki iddialardan tamamen kacinilmalidir:

- aktif ve kusursuz yapay zeka asistani yayinda
- pediatrist onayli tum urun havuzu
- canli ebeveyn toplulugu hazir
- kendi marka urunler satista
- tum sehirlerde aktif teslimat
- hic eksik urun yasatmaz
- ebeveynlik yukunu tamamen sifirlar
- tum bebekler icin tek dogru cozum
- hazir marketplace ve genis urun katalogu

## 6. Surface Bazli Truth Kurallari

## 6.1 Hero

Hero'da yalnizca en guvenli iddialar kullanilmali.

Guvenli alanlar:

- karar yukunu azaltma
- kisisellestirme mantigi
- erken erisim cercevesi
- daha duzenli ve sakin deneyim

Hero'da kacin:

- aktif AI motorunu bugun kullaniyormus gibi gostermek
- buyuk pazar rakamlariyla asiri iddia kurmak
- canli topluluk ve lansman dili

V1 public uygulama notu:

- Hero'da AI, aktif topluluk, lojistik veya finansal metrik iddiasi kullanilmadi.
- Dil, erken asama platform ve kisisellestirilmis kutu mantigi uzerinde calisan yapi olarak sinirlandi.
- CTA, gercek kayit backend'i varmis gibi degil; kullaniciyi kisisellestirilmis oneri studyosuna yonlendiren durust bir aksiyon olarak yazildi.
- Oneri studyosu gercek form submit semantigi tasimaz; JS kapali durumda bile bilgi gonderimi veya URL serialization olusmaz.

V2.2 oneri studyosu uygulama notu (phase machine):

- Site iki yuzeye ayrildi: trust-first home page (`/`) ve ayri kisisellestirilmis oneri studyosu (`/oneri/`).
- Studyo dort faza bolunmustur: intro (karsilama), questions (sorular), transition (derleme), result (oneri).
- Studyo dili "kisisellestirilmis oneri", "secimlerinize gore sekillenen paket cercevesi" ailesinde kalir; "AI sizin icin karar verdi", "akilli motor", "doktor onayli" gibi iddialar kullanilmaz.
- Studyo backend'e bagli degildir: oneri mantigi tarayicidaki deterministic bir kural setiyle calisir.

V2.5 plan karsilastirma sayfasi notu:

- `/erken-erisim/` sayfasi result reveal sonrasi acilan ucuncu yuzeydir; urun sahibi onayiyla fiyatli Mevcut / Plus / Premium plan karsilastirmasidir.
- Fiyat, plan adi ve plan kapsam maddeleri bu yuzeyde guvenli kabul edilir: `0 TL`, `799 TL / 15 Gun`, `1199 TL'den baslar`.
- Sayfa yine gerçek checkout veya operasyon akisi baslatmaz; CTA'lar inceleme/secim mantiginda kalir.
- Secili plan hangi kart ise koyu featured gorunum o karta tasinir; Plus sadece snapshot yokken varsayilan baslangictir.
- Eski buyuk detail panel ana okuma yukunu tasimaz; kart altinda yalnizca secili planin sinirini anlatan kisa durust not bulunur. "bugun satin alinabilir", "checkout'a git", "aboneliginiz basladi" gibi cumleler kullanilmaz.
- Kart CTA'lari "Mevcut seviye / Plus'i incele / Premium'u incele / Secili plan" tonundadir; "Plani satin al / Hemen basla / Aboneligi ac / Paketi al" gibi cumleler yasaktir.
- Hala yasak olan claim'ler: AI takip/analiz, doktor veya uzman onayi, kargo/teslimat tarihi, stok uyarisi, dinamik fiyatlandirma, oyuncak ekleme, mama ekleme, topluluk rozeti ve otomatik teslimat.

V2.6 iletisim kapanisi notu:

- Home page son bolumu artik Instagram ve e-posta kanallarini gosteren iletisim panelidir.
- Bu panelde `@babieplus` Instagram hesabi ve `babieplus@gmail.com` e-postasi gosterilebilir.
- Iletisim paneli siparis, odeme, otomatik basvuru, aktif destek taahhudu, teslimat veya stok claim'i kurmaz.
- Sonraki adim CTA'lari "Oneri studyosuna don / Bu mantigin nasil calistigini gor / Sik sorulan sorular / Babie+ ana sayfa" seklindedir; check.py truth-safe guard yasak ifadeleri yakalar.
- Sayfa `<form>`, input, select, textarea veya submit-capable button icermez; check.py bunu structurel olarak dogrular.

## 6.2 Nasil Calisir

Bu alanda sistemin mantigi anlatilabilir, ama aktif olmayan ozellikler final urunmus gibi yazilmamalidir.

## 6.3 FAQ

Sartli gercekler burada daha acik anlatilabilir.

Guvenli ornekler:

- erken erisim asamasindayiz
- kisisellestirme icin hangi bilgi alanlarini dusunuyoruz
- hangi ozellikler sonraki fazda hedefleniyor

V1 FAQ notu:

- FAQ, sayfanin fiyatli plan karsilastirmasi sunabilecegini ama gercek checkout veya calisan operasyon akisi olmadigini acikca soyler.
- Urun kategorileri nihai katalog veya satis listesi gibi sunulmaz.

## 6.4 Footer ve Meta Yuzeyleri

En korumaci dil kullanilmalidir.

Kisa, net ve dogrulanabilir ifade tercih edilmelidir.

## 7. Publish Oncesi Checklist

- bu iddia kaynak belgelerle savunulabiliyor mu?
- hazir olmayan bir ozellik hazirmis gibi mi duruyor?
- AI dili gerektiginden sert mi?
- guven vurgusu resmi onay gibi mi okunuyor?
- erken erisim gercegi yeterince acik mi?
- public metinde satisa hazir urun hissi gereksiz buyutuluyor mu?

## 8. Sonuc

Babie+ sitesi gucunu buyuk laflardan degil; sakin, acik ve guven veren bir anlatidan alacaktir. En iyi copy, en fazla soz veren copy degil; bugunku urun gercegini en dogru beklentiyle anlatan copy'dir.
