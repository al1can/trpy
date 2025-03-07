# TrPy

Türkçe Sözdizimi Python Çeviricisi

> Türk milletinin dili Türkçedir. Türk dili dünyada en güzel, en zengin
> ve en kolay olabilecek bir dildir. Onun için her Türk, dilini çok
> sever ve onu yükseltmek için çalışır… Türk dili, Türk milleti için
> kutsal bir hazinedir. Çünkü Türk milleti geçirdiği sayısız felaketler
> içinde ahlâkının, geleneklerinin, hatıralarının, çıkarlarının, kısaca
> bugün kendi milliyetini yapan her şeyin dili sayesinde korunduğunu
> görüyor. Türk dili, Türk milletinin kalbidir, zihnidir. Mustafa Kemal
>  — Atatürk

TrPy, Python sözdizimindeki kelimeleri Türkçe karşılıkları ile çeviren bir önişleyicidir.

[PyGyat](https://github.com/shamith09/pygyat) projesi baz alınarak geliştirilmiştir.
  

## README İçerikleri:

* [Özellikler](#özellikler)

* [Kod Örneği](#kod-örneği)

* [Yükleme](#yükleme)

* [Sözdizimi Çevirileri](#sözdizimi-çevirileri)

* [Hızlı Giriş](#hızlı-giriş)

* [Proje Yapısı](#proje-yapısı)

  
  

## Özellikler

  

* Türkçe sözdizimi ile Python yaz.

  

* TrPy dosyalarını `trpy` komutu ile çalıştırabilirsin, aynı Python da çalıştırıldığı gibi.

  

* Python dosyalarını Türkçe sözdizimi ile yazılmış TrPy dosyalarına çevir.

  

* Gerçek Python anahtar kelimeleri, TrPy eşlemeleri ile tanımlanmışsa kullanılamaz.

## Kod Örneği

Fibonacci dizisi (özyinelemeli):

```

fonksiyon fib(n):
    eğer n eşit 0:
        döndür 0
    değilse eğer n eşit 1:
        döndür 1
    yoksa:
        döndür fib(n çıkar 1) topla fib(n çıkar 2)

konuş(fib(10))

```

Faktöriyel (özyinelemeli):

```

fonksiyon fakt(n):
    eğer n eşit 1:
        döndür 1
    yoksa:
        döndür fact(n çıkar 1) rizz n

konuş(fakt(5))

```

## Yükleme
 
 Projeyi denemek için bu adımları yapmanız gerekmektedir:
```

$ git clone https://github.com/al1can/trpy.git

$ cd trpy

$ pip3 install .

```
  

Yüklemeyi kaldırmak için:

  

```

$ pip3 uninstall trpy

```

  

Bu işlemler tüm yüklemeleri kaldırır.
  

## Sözdizimi Çevirileri

  
Aşağıda tüm Python sözdizimleri ve operatörlerin Türkçe karşılıkları bulunmaktadır. Bu tabloda bulunmayan Python sözdizimleri aynı şekilde kullanılmaya devam edilebilir. Yeni eklemelerin yapılmasını isterseniz pull request açabilirsiniz.

| Python Sözdizimi/Operatör | TrPy Çevirisi |
| Türkçe        | Python Karşılığı |
|---------------|------------------|
| dene          | try              |
| olmazsa       | except           |
| en son da     | finally          |
| döndür        | return           |
| çıkar         | -                |
| topla         | +                |
| konuş         | print            |
| doğru         | True             |
| yanlış        | False            |
| fonksiyon     | def              |
| iken          | while            |
| içe aktar     | import           |
| dan           | from             |
| sınıf         | class            |
| eğer          | if               |
| değilse       | elif             |
| yoksa         | else             |
| için          | for              |
| durdur        | break            |
| devam         | continue         |
| teyit         | assert           |
| fırlat        | raise            |
| ile           | with             |
| olarak        | as               |
| genel         | global           |
| nâyerel       | nonlocal         |
| sil           | del              |
| burdan gönder | yield from       |
| gönder        | yield            |
| Hiç           | None             |
| kendi         | self             |
| aralık        | range            |
| büyük eşit    | >=               |
| küçük eşit    | <=               |
| eşit          | ==               |
| büyüktür      | >                |
| küçüktür      | <                |
| içinde        | in               |
| geç           | pass             |
| aç            | open             |
| kapat         | close            |
| ve            | and              |
| ya da         | or               |

  

## Hızlı Giriş

  
TrPy, TrPy dosyalarını (önerilen dosya uzantısı: `.trpy`) önce Python dosyalarına çevirir ve ardından Python kullanarak çalıştırır. Bu yüzden TrPy'nin çalışabilmesi için geçerli bir Python kurulumuna ihtiyacınız vardır.
  
 Bir TrPy programını çalıştırmak için, sadece aşağıdaki komutu yazabilirsiniz:


  

```

$ trpy source.gyat arg1 arg2 ...

```

  
Bu komut, `source.trpy` dosyasını arg1, arg2 gibi komut satırı argümanları ile çalıştırır. TrPy dosyalarını çalıştırmak için daha fazla bilgi edinmek için:

  

```

$ trpy -h

```

  
komutunu kullanarak yardım sayfasını görüntüleyebilirsiniz. Ayrıca `man` sayfasını da şu şekilde görebilirsiniz:
  

```

$ man trpy

```

TrPy, ayrıca Python'dan TrPy'ye dönüştürücü içerir. Bu `py2trpy` komutu ile yapılabilir:

  

```

$ py2trpy test.py

```

  
Bu, `test.gyat` adında bir TrPy dosyası oluşturur. `py2trpy` komutunun tam açıklamasına, şu komutla ulaşabilirsiniz:
 
```

$ py2trpy -h

```

  

Ya da `man` sayfasını şu komutla açabilirsiniz:
  

```

$ man py2trpy

```

  

## Proje Yapısı

  

Şu an TrPy, Python dilinde yazılmıştır. Git deposu 4 dizinden oluşmaktadır:
  
-   `trpy`: Ana script tarafından kullanılan parser ve diğer yardımcı araçları içeren Python paketi.
-   `etc`: Manuel sayfalar ve diğer yardımcı dosyalar.
-   `scripts`: Shell'den çalıştırılabilen Python scriptlerini içerir.
-   `testcases`: Test amacıyla kullanılan bazı örnek `.trpy` ve `.py` dosyalarını içerir.