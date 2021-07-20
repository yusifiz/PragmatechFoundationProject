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

