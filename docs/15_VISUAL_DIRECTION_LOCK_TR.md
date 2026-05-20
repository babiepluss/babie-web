# Babie+ Gorsel Yon Kilidi

## 1. Dokumanin Amaci

Bu belge, babie+ sitesinin ilk gorsel yonunu tek secenege indirir.

Amac, tasarim surecinin surekli farkli yone kaymasini engellemek ve secilen dili daha tutarli uygulamaktir.

Bu dokumandan sonra hedef yeni yon aramak degil, secilen yonu iyi uygulamaktir.

## 2. Nihai Karar

Babie+ sitesi icin secilen ana gorsel yon:

- Calm Premium Care

Destek katmanlari:

- Warm Editorial Trust
- Soft Clinical Precision

V1 kural seti:

- ana yon bir tane
- destek tonlari yalnizca bilgi mimarisi ve guven alanlarinda calisir
- site ne cizgi film gibi fazla bebeksi, ne de soguk bir saglik paneli gibi gorunur

## 3. Tek Cumlelik Gorsel Tanimi

Sicak kirik krem zeminler, yumusak ada panelleri, sakin tipografi ve kontrollu dogal aksanlarla kurulmus premium ebeveyn destek vitrini.

## 4. Neden Bu Yon Secildi

- Babie+ guven vermeli ama soguk gorunmemeli
- Bebek odakli olmali ama klise pastel-magaza diline dusmemeli
- Premium his vermeli ama ulasilmaz gorunmemeli
- Kisisellestirme ve onboarding mantigi rahat okunmali

## 5. Kilitlenen Gorsel Sistem

## 5.1 Arka Plan Dili

- duz saf beyaz yok
- duz karanlik tema yok
- yumusak kirik krem veya sut tonlu zemin var
- section bazli cok hafif ton farklari olabilir
- arka plan hareketi veya gurultusu minimumda tutulur

## 5.2 Renk Dili

Ana renk ailesi (V2 — sky + peach paleti):

- Peach Base: #fbe8dd
- Milk Surface: #fffaf6
- Cream Surface: #fff5ef
- Slate Text: #2a3a45
- Sky Soft Accent: #a8c5d6
- Soft Peach Accent: #ffd7c8
- Powder Sky Support: #c5dae6
- Sky Deep Primary: #3c6b86
- Deep Peach Support: #d99275

Kurallar:

- ayni section'da en fazla iki canli aksan kullanilir
- CTA alanlarinda Sky Deep ana vurgu, Soft/Deep Peach destek aksan olarak kullanilir
- Sky Soft genel denge rengi olarak davranir
- Powder Sky bilgi panelleri ve serinlik dengesi icin destek tonudur
- arka plan ana zemin Peach Base ve Milk Surface tonlarinda kalir

Logo uygulama matrisi:

- acik zeminlerde (Milk, Cream, Peach Base, acik panel ve header yuzeyleri) derin mavi lockup kullanilir
- koyu zeminlerde (footer, koyu featured panel veya derin mavi badge alani) soft peach lockup kullanilir
- ters varyant sirf farkli gorunsun diye kullanilmaz; secim yuzey kontrastindan gelir
- transparent lockup UI icinde birincil cozumdur; kare tile yalnizca favicon, touch icon ve benzeri kontrollu brand alanlarina ayrilir
- logo dekoratif pattern gibi tekrar edilmez; once yon bulma, marka tanimi ve guven isaretidir

V2 gecis notu:

- Sage/Moss yesil aile, Sky Blue ailesine tasindi
- Apricot/Deep Apricot tonlari yumusak peach ailesiyle (#ffd7c8 / #d99275) yenilendi
- CSS degisken adlari (`--sage`, `--sage-dark`, `--apricot`, `--apricot-deep`) anlam olarak korundu fakat Sky Blue / Peach degerlerini tasir; semantik isim refactor'u ileride yapilabilir

## 5.3 Tipografi Dili

Kilitle:

- display: Fraunces
- body: Manrope
- label ve micro copy: IBM Plex Sans

Yapma:

- Inter veya sistem fonta geri kacma
- cocuksu display font kullanma
- tipografiyi moda blogu gibi fazla romantiklestirme

## 5.4 Panel ve UI Dili

- yuzeyler yumusak kartlar gibi davranmali
- hafif border ve ince golge yeterli
- sert cam efekti veya asiri blur kullanilmaz
- formlar nazik ve kolay anlasilir gorunmeli

V2.5 plan karsilastirma kart notu:

- Uc kartli Mevcut / Plus / Premium karsilastirma yuzeyinde secili plan Sky Deep Primary / derin mavi aileyle koyu featured gorunebilir.
- Featured gorunum ortadaki karta sabitlenmez; snapshot veya kullanici secimi hangi karta giderse koyu yuzey o karta tasinir.
- Secili kartta Soft/Deep Peach pill ve check vurgulari kullanilabilir; secili olmayan kartlar Milk/Cream yuzeyde ince sky/peach border ile sakin kalir.
- Buyuk kart ici vurgu satiri artik fiyat satiridir; Manrope'un guclu agirligi kullanilir, ancak SaaS pricing sertligine kaymadan Calm Premium Care dengesi korunur.

Brand kilit notu:

- Header ve footer ayni placeholder mantigiyla degil, ayni oran disiplinine sahip iki lockup varyantiyla cozulmelidir.
- Logo esnetilmez, ek glow/bevel/cam efekti almaz, gereksiz hover gosteri nesnesi gibi davranmaz.
- Home page icinde marka tekrarinin dozu dusuk tutulur; gerekirse yalnizca kutu ornegi gibi kontrollu bir yerde kucuk mark kullanilir.

## 5.5 Motion Dili

Kilitle:

- hafif reveal
- kucuk CTA lift
- yavas ve yumusak gecisler

Yapma:

- buyuk parallax
- surekli hareket eden arka planlar
- asiri micro interaction gosterisi

## 6. Section Bazli Gorsel Kilit

Hero:

- en sakin ama en guvenli gorunen alan
- copy baskin kalir
- gorsel panel urun mantigini destekler

Problem:

- biraz daha kontrastli kartlar olabilir
- sorun net okunur ama korku pazarlamasina donusmez

Nasil Calisir:

- editorial ve sistematik dil birlikte calisir
- ikon yerine sade numarali adimlar tercih edilir

Ornek Kutu:

- urun dizimi gercek ve temiz gorunmeli
- dekoratif oyuncak gibi davranmamali

Guven:

- daha duz ve utility-first bir ritim
- gereksiz sus yok

Iletisim kapanisi:

- hero'nun yumusak kopyasi veya ikinci bir oneri teaser'i degil
- Instagram ve e-posta kartlari Calm Premium Care panel diliyle sakin kapanis yapar
- ikonlar sade, temaya uygun ve okunurlugu destekleyen boyutta kalir

V2.7 iletisim modulu kilidi:

- Iletisim alanı ayri bir tam ekran sayfa veya ikinci bir hero gibi davranmaz; SSS sonrasi tek bir kompakt panel olarak kalir.
- Eyebrow yaninda 12px hissinde, kucuk bir aksan ikonu kullanilir. Bu ikon dekoratif degildir; sadece etiketi destekler.
- Kanal kartlari sol ikon + orta metin + sag yon oku duzeninde calisan kompakt list-row hibridi olarak kurulur. Masaustunde ikon 36px, mobilde 32px boyutundadir.
- Buyuk siyah/bos rounded-square medya alani, sahte mockup, harita veya iframe yerlestirilmez. Iletisim alaninda dekoratif placeholder kullanilmaz.
- Panel padding'i, kart yuksekligi ve baslik buyuklugu, ana hero veya plan karsilastirma kartlari kadar agirlik tasimayacak sekilde kucultulmustur. Iletisim section'i tek bakista okunan tok bir blok olarak kalir.

## 6.1 V1 Uygulama Notu

Ilk calisan web yuzeyi Calm Premium Care yonunu su sekilde uygular:

- gercek gorsel olmadigi icin sahte stok fotograf, sahte urun fotografi veya sahte uygulama ekrani kullanmaz
- hero ve kutu alaninda CSS tabanli profil/kutu kompozisyonlari kullanir
- ana zemin Peach Base ve Milk Surface tonlarinda kalir
- CTA ve vurgu alanlarinda Sky Deep ve Soft/Deep Peach kontrollu kullanilir
- Fraunces, Manrope ve IBM Plex Sans fontlari hedeflenir
- mor-beyaz startup, medikal panel veya cocuksu pastel magazacilik diline kaymaz

## 7. Care-First Kural Seti

Bu yonun en kritik kurali sudur:

- gorsel stil, guven ve okunurlugun onune gecemez

Pratik anlami:

- ilk ekran bir moda cekimi gibi davranmaz
- CTA her zaman net kalir
- form alanlari gorsel gosteriye kurban edilmez
- urun mantigi, dekoratif objelerden daha on planda olur

## 8. Reddedilecek Gorsel Sapmalar

- jenerik mor-beyaz startup sitesi
- asiri pastel ve sadece sevimlilik ureten bebek magazasi dili
- yogun emoji veya ilustrasyon kalabaligi
- steril hastane paneli hissi
- tum section'larda ayni kart yapisinin kopyalanmasi
- gereksiz dev yuvarlak blob arka planlar

## 9. Tasarim Review Sorulari

Her ciddi tasarim turunda su sorular sorulmalidir:

- ilk ekran ne sundugumuzu net anlatiyor mu?
- CTA en gorunur etkileim noktasi mi?
- tipografi hem premium hem sicak mi?
- sayfa fazla bebeksi mi, fazla kurumsal mi?
- guven unsurlari yeterince sade mi?
- mobilde form ve kartlar rahat okunuyor mu?

## 10. Freeze Kurali

Bu dokumandan sonra yeni ana gorsel yon aranmaz.

Yalnizca su iki durumda yeniden acilir:

- secilen yon okunurlugu zayiflatiyorsa
- mobil deneyim ciddi sekilde dusuyorsa

## 11. Sonuc

Babie+ icin secilen gorsel yon Calm Premium Care'dir. Bu yon, guveni, premium hissi ve ebeveyn rahatligini ayni sistemde toplar. Warm Editorial Trust markaya sicaklik verir; Soft Clinical Precision ise secim mantigina netlik katar.
