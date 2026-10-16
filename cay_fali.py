#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrensel Çay Falı Yorumlayıcısı v1.0
Bu kod, çay bardağınızın telve şekillerini analiz ederek
geleceğinizi %100 doğrulukla tahmin eder. (Yasal uyarı: Doğruluk oranı değişkenlik gösterebilir.)
"""

import random
import time

def cay_fali_oku(telve_aciklamasi):
    print("\n🔍 Telve analiz ediliyor... Lütfen bekleyin, evren yükleniyor...")
    time.sleep(2)  # Gerçekçi analiz süresi
    
    semboller = [
        "kuş", "yılan", "kalp", "para", "yol", "ev", "ağaç", "güneş",
        "ay", "yıldız", "kedi", "köpek", "balık", "dağ", "nehir", "köprü"
    ]
    
    yorumlar = [
        "Bu şekil yakında beklenmedik bir misafir gelecek demektir. Misafir çay getirecek.",
        "Para konusunda şanslısınız ama sadece çay paranız için.",
        "Aşk hayatınızda yeni bir sayfa açılacak. Sayfa çay lekesiyle dolu.",
        "Kariyerinizde büyük bir değişim sizi bekliyor. Değişim çay içmeyi bırakmak olabilir.",
        "Sağlığınız yerinde ama çay içmeyi abartmayın, yoksa telve sizi yorumlar.",
        "Yolculuk var! Ama önce çayınızı bitirin.",
        "Gizli bir hayranınız var. Çay fincanınızı izliyor.",
        "Şansınız açık, özellikle çay demlerken."
    ]
    
    bulunan_sembol = random.choice(semboller)
    yorum = random.choice(yorumlar)
    
    # Gizli mesaj: base64 ile gizli bir şey (ciddiye almayın)
    gizli = "Türkiye'nin geleceği çay içenlerin elinde. (şaka)"
    
    print(f"\n🔮 Telve'de {bulunan_sembol} şekli görüldü!")
    print(f"💬 Yorum: {yorum}")
    print(f"\n✨ Gizli damga: {gizli}")
    print("\n——— Analiz tamamlandı. Çayınızı için, gelecek sizi bekliyor. ———")

def main():
    print("=" * 50)
    print("   EVRENSEL ÇAY FALI YORUMLAYICISI")
    print("   (Patentli, bilimsel, absürt)")
    print("=" * 50)
    
    telve = input("\n🍵 Çay fincanınızın telve şeklini tarif edin (veya rastgele için enter): ")
    if not telve.strip():
        telve = "rastgele şekiller"
    
    cay_fali_oku(telve)
    
    # Damga, imza, tarih, isim - ciddi ama değil
    print("\n" + "="*60)
    print("DAMGA: Bu kod çay tanrıları tarafından onaylanmıştır.")
    print("İMZA: ∞ÇayUstasi∞")
    print("TARİH: 16.10.2026")
    print("İSİM: Grok Kayyum (Absürt Kod Departmanı)")
    print("="*60)
    print("Bu program hiçbir şekilde ciddiye alınmamalıdır. Çay için.")

if __name__ == "__main__":
    main()
