Insider Careers Automation Test Case

Proje Açıklaması
Bu proje, Insider web sitesinin kariyer sayfasında belirlenen test senaryolarını Selenium + Python kullanarak otomatikleştirmek için geliştirilmiştir. Testler, belirlenen adımları takip ederek QA iş ilanlarının filtrelenmesini ve doğru şekilde listelenmesini kontrol eder.

---- Test Senaryoları
* Anasayfa Yüklenme Kontrolü:
https://useinsider.com/ adresine gidilir ve anasayfanın açıldığı doğrulanır.

*Kariyer Sayfasına Yönlendirme:
 Navbarda bulunan Company menüsüne tıklanır.
 Açılan menüden Careers seçeneğine tıklanarak ilgili kariyer sayfasına yönlendirilir.
 Kariyer sayfasında Locations, Teams, Life at Insider gibi sectionların var olup olup olmadığı kontrol edilir.
 
* QA İş İlanlarını Filtreleme:

 https://useinsider.com/careers/quality-assurance/ adresine gidilir.
 Sayfanın yüklenmesi beklenip, "See all QA Jobs" butonuna tıklanır.
 job liste scroll yapıp,  Listelenen verilerine ait olan Resultcounterın tamamen yüklenmesini bekler.
 Filtreleme Location dropdown açılır ve Istanbul, Turkey seçilir.
 Filtreleme Department dropdown açılır ve Quality Assurance seçilir.
 Listelenen iş ilanlarının doğru filtrelendiği kontrol edilir.
 
* İş İlanlarının Kontrolü:

 Tüm ilanların;
Pozisyonunun: "Quality Assurance" içerdiği,
Departmanının: "Quality Assurance" içerdiği,
Lokasyonunun: "Istanbul, Turkey" içerdiği doğrulanır.

* İş Başvurusu Sayfası Kontrolü:
 İlk iş ilanındaki "View Role" butonuna tıklanır.
 Lever Application Form sayfasına yönlendirme yapıldığı doğrulanır.
Test bitirilir.

(Başlangıçta çerezlerin temizlenmesinde fayda var.)
