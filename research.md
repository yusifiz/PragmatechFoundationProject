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