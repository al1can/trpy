import sys
import os

import trpy.parser
import trpy.logger


"""
Modül: TrPy dosyalarını Python kodunda içe aktarmak.
"""


def glaze(modül_adı, globals, logger=None):
    """
    TrPy dosyalarını Python kodunda içe aktar. Örnek:

    ```python
    from trpy.importing import glaze
    glaze("test_modül", globals())

    # Şimdi, 'test_modül' her zamanki modüller gibi kullanılabilir:
    test_modül.fonksiyon()
    ```

    Args:
        modül_adı (str):              İçe aktarılacak modülün adı.
        globals (dict):               Global isim alanı (globals() kullanarak 
                                      elde edilebilir).
        logger (trpy.logger.Logger):   Opsiyonel. Logger nesnesi. Genellikle 
                                        hata ayıklama için kullanılır.

    Raises:
        ImportError: Eğer modül için trpy dosyası bulunmazsa veya trpy dosyası 
        doğru şekilde işlenemezse.
    """
    if logger is None:
        logger = trpy.logger.Logger()

    logger.log_info("Aranıyor: %s.trpy" % modül_adı)
    yol = _modül_bul(modül_adı, logger)

    logger.log_info("Parse ediliyor: %s" % yol)
    try:
        trpy.parser.parse_file(yol, os.path.join(sys.path[0], "python_"))

        hata_sırasında = None

    except Exception as e:
        hata_sırasında = e

    if hata_sırasında is not None:
        raise ImportError("Hata '%s' parse edilirken: %s" % (yol, str(e)))

    python_dosya_yolu = os.path.join(
        sys.path[0], 
        "python_" + trpy.parser._change_file_name(modül_adı, None)
    )

    logger.log_info("İçe aktarılıyor: %s" % python_dosya_yolu)

    # Hacky (Geçici) çözüm: Global modül içe aktarmak
    exec("global %s" % modül_adı, globals)
    exec("import python_%s as %s" % (modül_adı, modül_adı), globals)

    # Temizlik
    logger.log_info("Siliniyor: %s" % python_dosya_yolu)
    os.remove(python_dosya_yolu)


def _modül_bul(modül_adı, logger):
    """
    Verilen modül adı için trpy dosyasını bulur.

    Args:
        modül_adı (str):              Aranacak modül adı.
        logger (trpy.logger.Logger): Opsiyonel. Logger nesnesi. Hata ayıklama için.

    Returns:
        str: Modüle ait trpy dosyasının tam yolu.

    Raises:
        ImportError: Modül bulunamazsa.
    """
    for yol in sys.path:
        logger.log_info("Aranıyor: %s" % yol)

        modül_yolu = _dizin_içinde_arama(modül_adı, yol) 

        if modül_yolu is not None:
            logger.log_info("Modül bulundu: %s" % modül_yolu)
            break

    if modül_yolu is None:
        raise ImportError("Modül için herhangi bir trpy dosyası bulunamadı: %s" % modül_adı)

    return modül_yolu


def _dizin_içinde_arama(modül_adı, dizin):
    """
    Bir dizini (ve alt dizinleri) tarar, ve 'modül_adı'.trpy dosyasını arar.

    Args:
        modül_adı (str):              Aranacak modül adı.
        dizin (str):                  Tarama yapılacak dizinin yolu.

    Returns:
        str: Modüle ait trpy dosyasının tam yolu, eğer bulunamazsa None döner.
    """
    for kök_dizin, alt_dizinler, dosyalar in os.walk(dizin):
        for dosya in dosyalar:
            if dosya == (modül_adı + ".trpy"):
                return os.path.join(kök_dizin, dosya)

    return None
