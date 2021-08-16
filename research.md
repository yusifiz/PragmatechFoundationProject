## Araşdırma

# Suallar

- 1.justify-content və align-items xüsusiyyətləri arasındakı fərqləri izah edin.
- 2.align-items və align-content arasındakı fərqləri izah edin.
- 3.box-sizing: border-box xüsusiyyəti hansı hallarda istifadə olunur?
- 4.inline styling hansı hallarda istifadə oluna bilər?
- 5.css-də !important və inherit ifadələrinin mənası nədir?

# Cavablar

* Flexbox modelini biz iki cür idarə edə bilərik: üfüqi və şaquli. Flexbox modelində defolt olaraq sətir üzrə düzülmə olur. Sətir üzrə düzülmədə üfüqi vəziyyətdə justify-content, şaquli vəziyyətdə isə align-items istifadə olunur.
* align-items şaquli düzülmələrdə istifadə olunur, tək sətirə təsir edir. align-content isə tək sətirli flexbox mmodellərinə təsir etmir.
* box-sizing parametri sayəsində, "box"lar verilən width parametri qədər genişləyir.
* --
* !important parametri özündən sonrakı parametrləri nəzərə almır. inherit parametri isə özündən qabaqkı elementin parametrlərini qəbul edir.

## Araşdırma-02

# Suallar

1. width:100% və width:100vw arasındakı fərqlər nədir və nə vaxt istifadə olunması məsləhətdir sizcə?
2. cm, em, in, mm, pc, pt, and px bu css ölçüləndirmə vahidlərin açıqlamalarını yazın
3. justify-content:space-around xüsusiyyəti ara məsafələri hansı formulaya görə tənzimləyir?
4. css pseudo-class və pseudo-element nədir? Nümunlərlər izah edin
5. meta tag nədir?
6. utf8 nə deməkdir?


# Cavablar

* width:100% - elementin həcmini, width:100vw - isə cihazın ekran ölçüsünə uyğun tənzimlənir. Yəni, vw istifadə etmək responsivlik üçün daha əlverişlidir.

* cm - santimetr
  em - defoult yazının ölçüsünü göstərir. Məsələn, 2em dəyəri hal-hazırkı defoult yazı ölçüsünün 2 qatı kimi nəzərdə tutulur.
  in - inç (1in = 96px = 2.54cm)
  mm - millimetr
  px - pixels (1px = 1/96 of in)
  pt - points (1pt = 1/72 of in)
  pc - picas (1pc = 12 pt)

* justify-content:space-around xüsusiyyəti ara məsafələri x:2x:2x:x kimi, yəni başlanğıc elementdən əvvəlki və son elementdən sonrakı boşluqlar elementlər arasındakı məsafənin yarısına bərabər şəkildə tənzimləyir.

* pseudo-class (yalançı sinif) və pseudo-element (yalançı element) web brauzerlərdə avtomatik tanınan xüsusi sinif və elementlərdir. Əgər yazdığımız sinif və ya elementdə spesifik bir xüsusiyyəti dəyişmək istəyirksə, bu xüsusiyyətlərdən istifadə edəciyik.  pseudo-class bir elementi fərqli siniflərə bölür, pseudo-element isə bir elementi alt hissələrə bölür. Məsələn, daha əvvəl açılmış linklərin rəngini dəyişmək üçün pseudo-class'dan istifadə edə bilərik.

* meta tag'i səhifə haqqında məlumat almaq, məzmununu öyrənmək üçün istifadə olunur. Əsasən, brauzerlərdə səhifənin istfadəçinin qabağına çıxmağı üçün açar sözlər, səhifənin müəllifi və s. kimi vasitələri arxaplanda yazmaq üçün əlverişlidir.

* utf-8 səhifənin şriftini müəyyən edir.

## Araşdırma-03

# Mövzular

1. Yaddaşdan istifadəyə görə
- interpereter dillər
- compiler dillər
2. Dizayn uslubuna gore diller (Pragadigmalar)
- imperative uslub
- declarative uslub

# Cavablar

1. Yaddaşdan istifadəyə görə proqramlaşdırma dilləri 2 yerə bölünür: 1.Interpreter dillər 2.Compiler dillər.

* Oxşar cəhətləri: Hər ikisi eyni funksiyanı yerinə yetirir. Yəni, hər ikisi proqramlaşdırma dilində verdiyimiz əmrləri maşın dilinə (machine language) tərcümə edir. Bizim hal-hazırda istifadə etdiyimiz proqramlaşdırma dilləri High Level Language sayılır, çünki bu dillərdə istifadə etdiyimiz kodlar insan dilinə ən yaxın kodlardır. Bir sözlə, interpreter və compiler bizim başa düşdüyümüz dili maşına başa salır.)

* Fərqli cəhətləri:
- Interpreter dillər: Əmrləri sətir-sətir tərcümə edir. Yəni yanlış koda qədər bütün kodları tərcümə edir, bu da kodu təhlil etmək üçün daha az vaxt sərf etməyimiz deməkdir. Həmçinin heç bir obyekt kodu yaratmadığı üçün yaddaşdan daha səmərəli istifadə edir.
- Compiler dillər: Yazılan proqramları bütünlüklə tərcümə edir. Kodda yanlış varsa, proqramı ümumiyyətlə tərcümə etmir, lakin interpreter dillərdən fərqli olaraq, ümumi icra müddəti daha sürətlidir. Obyekt kodu yaratdığı üçün yaddaşdan daha çox istifadə edir.

2. Dizayn üslubuna görə də proqramlaşdırma dilləri əsas iki yerə bölünür və bunlara paradiqmalar deyilir: 1.İmperativ paradiqma 2.Deklarativ paradiqma.

* Paradiqmalar istifadə olunan proqramlaşdırma dilinə görə fərqlilik göstərir. Belə ki, bəzi dillərdə asan olan üslub digərlərində daha çətin ola bilər. Ümumi olaraq, paradiqma dediyimiz şey kodun üslubunu, problemin hansı strategiya ilə həll olacağını göstərir.

- İmperativ üslub: Bu üslubda yazdığımız kodlar maşına sətir-sətir izah edilir. Yəni, nəticəni görmək üçün lazım olan hər addımı siz təyin edirsiniz.İmperativ paradiqması da kod yazılış üslubuna görə Prosesli, Obyekt yönümlü və Paralel prosesli kimi bir neçə yerə bölünür. Bu üslub daha çox 'old' dillərdə istifadə olunduğna görə klassik üslub da deyilir.
- Deklarativ üslub: Bu üslubda isə problemi həll etmək üçün onun nə olduğunu bilmək kifayətdir.Deklarativ paradiqması da Məntiqi, Funksional və Məlumat bazası emalı kimi bir neçə yerə bölünür. Biz sadəcə maşına nəticəni bildiririk, necə edəcəyini isə özü bilir.) Bu üslub isə əsasən yeni dillərdə istifadə olunur.

## Araşdırma-04 (JavaScript)

# Suallar

1. Mən niyə javascript öyrənməliyəm?
2. Yeni proqramlaşdırma dilini öz başıma öyrənməli olsaydım nə edərdim?
3. dəyişən təyin edərkən hansı sintaktik qaydalara diqqət etməliyik?
4. javascript kodlarının oxunma sırası necədir?
5. niyə mən yazılan javascript kodunu browserda açıram?
6. javascript operatorlarının istifadə edərkən nələrə diqqət etməliyəm?

# Cavablar

1. Fikrimcə, yazdığım html səhifələrini daha dinamik, əlaqəli və fərqli görünüm yaratmaq üçün öyrənməliyəm.

2. Kursa başlamazdan əvvəl təcrübə etdiyim kimi desək, c++, python basic səviyyədə youtube və digər platformalardan search edərək öyrənirdim. Əgər youtube platformasını Samir müəllim ləğv etmiş olsa idi, hər halda əvvəlcə proqramlaşdırmanı niyə öyrənəcəyimə, daha sonra hansı sahəsini öyrənəcəyimə qərar verərdim. Sonra isə həmin sahəyə hardan başlamaq lazım olduğunu search edərdim.

3. Dəyişən tipinin dəyişənə uyğun olmasına və harada istifadə edəcəyimizə diqqət etmək lazımdır.

4. Js'də oxunma sırası yuxarıdan aşağıya doğrudur, proqram əvvəlcə bütün kodu oxuyur, daha sonra ardıcıllıqla icra edir.

5. Js'i istifadə etmək üçün lazım olan interpreter browser'lərdə hazır mövcud olur. Və Js'i interpret etmək üçün engine deyilən vasitələrdən istifadə olunur. Məsələn bunlar, Chrome'da V8, Firefox'da SpiderMonkey, Internet Explorer'də Chakra, Safari'də JavaScriptCore'dur.

6. Operatorlardan istifadə edərkən, onların yalnız riyazi ifadələr olmadığını bilmək lazımdır. Həmçinin functions, conditional statements(şərti ifadələr), loop'larda (dövr) düzgün istifadə etmək etmək lazımdır.

## Araşdırma 05 (Python, Flask)

# Suallar və Cavabları

 ## Python module və package nədir? Necə istifadə olunur?

### Modul nədir?

Python'da yazdığımız hər proqram əslidə bir moduldur. Python'un bu baxımdan bizə verdiyi üstünlük isə bir növ function kimi modulları da istədiyimiz proqramın içində çağıra bilərik. Bu isə bizi kod təkrarından azad edir. Modullar 2 yerə bölünür:

  1. Öz yazdığımız modullar
  2. Hazır modullar

Hər yazdığımız .py faylının bir modul olduğunu qeyd etdik. Python bizim işimizi tezləşdirmək və asanlaşdırmaq üçün bizə hazır moddullar verir.Hazır modullar da öz içlərində 2 yerə bölünür:

  1. Standart Library Modules
  2. Third Party Modules

Standart kitabxana modulları pyhton yükləyəndə hazır gələn modullardır. Üçüncü şəxs modulları isə üçüncü şəxslər tərəfindən yazılıb istifadəyə verilən modullardır.

### Package nədir?

Package modullar toplusudur deyə bilərik. Modulardan daha geniş bir qavramdır. Python'da ümumiyyətlə package'lərdən çox istifadə olunur. Hər sahə üçün ayrı bir package var. Məsələn, web application yazmaq üçün django, flask istifadə olunur. Yəni, bu framework'lər özlüyündə bir neçə moduldan ibarətdir.

 ## Module və package arasındakı fərqlər nələrdir?

  * Yuxarıda da qeyd etdiyim kimi, package modullar toplusudur. Məsələn, os.py bir moduldur, django isə package'dir.Eyni zamanda hər package bir moduldur, ancaq modullar bir package deyildir. Yəni 'venv' package'inə biz 'venv' modulu da deyə bilərik.

 ## Web Server nədir?

  * Web Server - istifadəçilərin internetdəki web-səhifələrə və digər verilənlərə daxil olmasına şərait yaradan xüsusi proqramlar ilə təmin olunmuş kompüterdir. Web-server web-saytın əsasını təşkil edir. Web-server informasiyaların saxlanılmasını, təşkilini və göndərilməsini təmin edir. Web-server web-brauzerdən qəbul etdiyi sorğu əsasında soruşulan sənədin elektron surətini istifadəçiyə göndərir. Belə sorğuların emal edilməsi və yerinə yetirilmə ardıcıllığı HTTP protokolu vasitəsilə yerinə yetirilir.

 ## WSGI nədir?

  * Web Server Gateway Interface - Python'da yazılan kodun web-serverin başa düşəcəyi hala gətirən interfeysdir. Veb server request'ləri WSGI'ə göndərir, WSGI isə proramınızı işə salıb bu requestin cavablarını HTML olaraq veb serverə çatdırır.

 ## Web Server və WSGI arasındakı fərqlər nələrdir?

  * WSGI, veb serverdən fərqli portda işləyir. Yəni, veb serverlər pythonda yazılmış kodu başa düşmürlər bunun üçün WSGI'dən istifadə edirlər

 ## HTTP Request nədir?

  * Client server tərəfindən veb serverə verilən sorğudur. Əsas iki yerə bölünür:

      * GET request
      * POST request

 ## GET,POST request nə deməkdir?

  * GET request veb serverdən sadəcə məlumat alır.
  * POST request isə veb serverə məlumat daxil edir.

 ## Flask framework necə işləyir?

  [Web saytın işləmə məntiqi](https://www.google.com/url?sa=i&url=https%3A%2F%2Fcodeburst.io%2Fflask-for-dummies-a-beginners-guide-to-flask-part-uno-53aec6afc5b1&psig=AOvVaw1TaccmUYQ2PidtOUfrmyWy&ust=1629157628873000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjV2qWbtPICFQAAAAAdAAAAABAX)

  * Flask (django da həmçinin) jinja2 templete dilindən istifadə edir. Flask ümumiyyətlə python üçün yazılmış bir framework'dür. Vebə bir request göndərdiyimiz zaman, məlumat database'dən alınır, ORM'ə ötürülür, ordan flask framework'ə daha sonra isə HTML olaraq bizə qayıdır.

 ## URL nədir? Detalları nədən ibarətdir?

  * Uniform Resource Loader - kompüterin serverlə əlaqə qurması üçün istifadə olunur. Domain kimi, ip ünvanlarını sözə çevirərək daha asan yaddaqalan edir.

 ## Virtual environment nədir? Nə üçün istifadə olunur?

  * Hər bir layihə üçün ayrıca virtual bir mühit yaratmaq üçün istifadə olunur. Əgər hər layihə üçün eyni flask'dən istifadə etsək, flask'də baş verəcək hər dəyişiklik (update) avtomatik olaraq bütün layihələrdə dəyişəcək. Bu isə bir çox hallarda istəməyəcəyimiz bir şeydir. Bu səbəbdən virtual environment bizim üçün daha əlverişlidir.

 ## Aşağıda yazılan pyton kodları nə iş görür? Sətir sətir izah etməyə çalışın.
    
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"

    if __name__=="__main__":
        app.run(debug=True)
  

* İlk öncə Flask kitabxanası koda əlavə olunub. Flask sinifindən bir app dəyişəni yaradılaraq, flask kitabxanasının xüsusiyyətlərindən istifadə olunub. app.route() funksiyası ilə səhifə yaradılıb. Səhifənin adresi isə ("/") şəklində ifadə olunub. def hello() funksiyası ilə 'hello world' return edilib (burada HTML səhifəsi də return edilə bilər). Daha sonra, faylın ayrıca proqram yoxsa, başqa bir proqram daxilində import edildiyi yoxlanılıb. Əgər başqa bir modul daxilində import edilibsə __name__ dəyəri həmin modulun adına bərabər olacaq və proqram işləməyəcək. Lakin, ayrıca proqramdırsa, __name__ == __main__ olacaq və şərt doğrulandığı üçün ekranda 'Hello, World!' yazısını görə biləcəyik.

