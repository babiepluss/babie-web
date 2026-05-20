# Babie+ Dokuman Guncelleme Protokolu

## 1. Dokumanin Amaci

Bu belge, babie+ reposunda yapilan her kod degisikliginden sonra ilgili markdown dosyalarinin da gozden gecirilmesini zorunlu kilmak icin yazildi.

Amac su:

- kod ile dokumanin birbirinden kopmasini engellemek
- sonraki gelistiricinin veya AI'nin eski belgeye bakip yanlis karar vermesini onlemek
- proje gercegini her turda guncel tutmak

Bu belge bir tavsiye notu degil, calisma protokoludur.

## 2. Ana Kural

Repo icinde her kodsal guncellemeden sonra su soru zorunlu olarak sorulmalidir:

- Bu degisiklik, docs altindaki herhangi bir markdown dosyasini etkiliyor mu?

Eger cevap evet veya kismen evet ise, ilgili markdown dosyalari ayni tur icinde guncellenmelidir.

Kod degisiklikleri ile dokuman degisiklikleri farkli zamanlara birakilmamali.

## 3. Ne Zaman Dokuman Guncellemesi Zorunludur?

Asagidaki durumlarda markdown guncellemesi zorunludur:

- repo geneli calisma kurallari veya instruction dosyalari etkilenirse
- yeni sayfa, yeni section veya yeni bilgi mimarisi eklendiyse
- hero, CTA, form akisi veya ana donusum hedefi degistiyse
- truth-safe copy sinirlari degisecek yeni claim'ler geldiyse
- yeni gorsel yon, yeni component sistemi veya yeni tasarim dili karari alindiysa
- onboarding alanlari veya kullanicidan istenen veri yapisi degistiyse
- build sistemi, klasor yapisi, template akisi veya ortam kurulumu degistiyse
- yeni kutuphane veya yeni gelistirme araci kalici olarak projeye girdiyse
- mevcut dokumanlarda artik yanlis kalacak herhangi bir ifade olustuysa

## 4. Hangi Dosyalar Once Kontrol Edilir?

Kod degisikliginden sonra en az su dosyalar kontrol edilmelidir:

1. AGENTS.md
2. docs/README.md
3. docs/17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md
4. docs/14_TRUTH_AUDIT_TR.md
5. docs/15_VISUAL_DIRECTION_LOCK_TR.md
6. docs/01_SITE_FOUNDATION_TR.md
7. docs/02_WIREFRAMES_TR.md
8. docs/05_HOMEPAGE_COPY_TR.md

Hepsi her turda degismek zorunda degildir. Ama hepsi etkilenme ihtimali icin dusunulmelidir.

## 5. Degisiklik Turu -> Guncellenecek Muhtemel Dokumanlar

## 5.1 Layout, section veya bilgi mimarisi degistiysa

Oncelikle kontrol et:

- docs/02_WIREFRAMES_TR.md
- docs/01_SITE_FOUNDATION_TR.md
- docs/README.md

## 5.2 Copy, CTA veya mesaj hiyerarsisi degistiysa

Oncelikle kontrol et:

- docs/05_HOMEPAGE_COPY_TR.md
- docs/14_TRUTH_AUDIT_TR.md
- docs/README.md

## 5.3 Gorsel sistem, renk, tipografi veya component dili degistiysa

Oncelikle kontrol et:

- docs/15_VISUAL_DIRECTION_LOCK_TR.md
- docs/17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md
- docs/README.md

## 5.4 Form, veri toplama veya onboarding akisi degistiysa

Oncelikle kontrol et:

- docs/02_WIREFRAMES_TR.md
- docs/01_SITE_FOUNDATION_TR.md
- docs/17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md

## 5.5 Build, template, klasor yapisi veya bagimliliklar degistiysa

Oncelikle kontrol et:

- AGENTS.md
- docs/17_AI_FRONTEND_BUILD_PLAYBOOK_TR.md
- docs/README.md
- gerekirse yeni teknik not dosyalari

## 6. Minimum Calisma Akisi

Her kod turundan sonra su sirayla ilerlenmelidir:

1. Kod degisikligi tamamlanir.
2. Degisiklikten etkilenen dokumanlar dusunulur.
3. Gerekli markdown dosyalari ayni turda guncellenir.
4. Kisa bir dogrulama yapilir.
5. Final ozetinde hem kod hem dokuman guncellemeleri belirtilir.

## 7. Final Mesaj Kurali

Her anlamli kod degisikligi sonrasinda final mesajda su da acikca belirtilmelidir:

- hangi markdown dosyalari guncellendi
- hangi dokumanlarin etkilenmedigi dusunuldu
- eger dokuman guncellenmediyse neden gerekmedigi

## 8. Yapilmamasi Gerekenler

- kodu degistirip docs'u sonra bakariz diye birakmak
- aktif olmayan, eskimis veya yanlis kalan markdown'lari bilerek tutmak
- build veya klasor yapisi degistigi halde playbook'u guncellememek
- yeni public claim ekleyip truth audit'i es gecmek
- gorsel sistemi degistirip visual lock dosyasini eski halde birakmak

## 9. Sonuc

Babie+ reposunda markdown dosyalari yardimci not degil, karar sistemi olarak kabul edilmelidir. Bu nedenle kod ve dokuman ayni gercegi anlatmak zorundadir. Kod degisip docs degismiyorsa, repo bilgisi sessizce bozuluyor demektir.