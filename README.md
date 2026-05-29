# Proje Adı

vbl1

## Proje Hakkında

Bu proje, çeşitli Python modüllerinden oluşan bir yazılım uygulamasıdır. Projede agent ve asistan dosyaları ile, front-end tarafında ise HTML dosyaları ile kullanıcı ara yüzleri oluşturulmuştur.

## Kurulum

Projeyi çalıştırmak için gereksinim dosyasındakı paketlerin kurulması gerekmektedir. Bunun için:

```
pip install -r requirements.txt
```

komutunu çalıştırarak gerekli tüm bağımlılıkları yükleyebilirsiniz.

## Kullanım

Proje, arka planda `app.py`, `agent.py`, `asistan.py` ve `llm.py` Python dosyaları ve ön yüzde `frontend` klasöründeki HTML dosyaları ile çalışmaktadır. Her bir bileşen spesifik işlemler için tasarlanmıştır.

## Araçlar

### `count_words` (Kelime Sayacı)

`backend/tools/count_words.py` içinde tanımlanan `count_words` aracı, kullanıcının verdiği metindeki kelime sayısını hesaplar. Agent sayfasında model bu araca erişebilir; "Şu metindeki kaç kelime var?" gibi sorularda otomatik olarak çağrılır ve sonucu döner.

## Katkıda Bulunma

Katkıda bulunmak isteyenler standart bir pull request süreci üzerinden projeye katkıda bulunabilirler.

## Lisans

Bu projeye ait lisans bilgileri burada yer alacaktır.