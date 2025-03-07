from setuptools import setup
from trpy import VERSION_NUMBER  # Türkçe Python kütüphanesi ismi olarak trpy

with open("README.md", "r") as fh:
    long_description = fh.read()

# Install python package, scripts and manual pages
setup(name="trpy",  # Türkçe Python kütüphanesi ismi
      version=VERSION_NUMBER,
      author="Ali Can Gündüz",
      author_email="ac.gunduz7878@gmail.com",
      license="MIT",
      description="Türk milletinin dili Türkçedir." +
        "Türk dili dünyada en güzel, en zengin ve en kolay olabilecek bir dildir." +
        "Onun için her Türk, dilini çok sever ve onu yükseltmek için çalışır…" +
        "Türk dili, Türk milleti için kutsal bir hazinedir." +
        "Çünkü Türk milleti geçirdiği sayısız felaketler içinde ahlâkının, geleneklerinin, hatıralarının, çıkarlarının," +
        "kısaca bugün kendi milliyetini yapan her şeyin dili sayesinde korunduğunu görüyor." +
        "Türk dili, Türk milletinin kalbidir, zihnidir.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/al1can/türkçe_python",  # GitHub URL'si de değiştirildi
      scripts=["scripts/trpy2py", "scripts/trpy", "scripts/py2trpy"],  # Türkçe versiyon script'leri
      data_files=[("man/man1", ["etc/trpy.1", "etc/py2trpy.1", "etc/trpy2py.1"])],
      packages=["trpy"],  # Türkçe Python kütüphanesi ismi olarak trpy
      zip_safe=False)
