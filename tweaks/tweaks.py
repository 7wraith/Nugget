from devicemanagement.constants import Version
from .tweak_classes import MobileGestaltTweak, MobileGestaltMultiTweak, MobileGestaltPickerTweak, FeatureFlagTweak, TweakModifyType, BasicPlistTweak, RdarFixTweak
from .eligibility_tweak import EligibilityTweak, AITweak
from .basic_plist_locations import FileLocation

    
tweaks = {
    ## MobilGestalt Ayarları
    "DynamicIsland": MobileGestaltPickerTweak("Dinamik Ada'yı Değiştir", "oPeik/9e8lQWMszEjbPzng", "ArtworkDeviceSubType", [2436, 2556, 2796, 2976, 2622, 2868]),
    "RdarFix": RdarFixTweak(),
    "ModelName": MobileGestaltTweak("Cihaz Model Adını Ayarla", "oPeik/9e8lQWMszEjbPzng", "ArtworkDeviceProductDescription", "", TweakModifyType.TEXT),
    "BootChime": MobileGestaltTweak("Önyükleme Zil Sesini Aç", "QHxt+hGLaBPbQJbXiUJX3w"),
    "ChargeLimit": MobileGestaltTweak("Şarj Sınırlaması Ayarla", "37NVydb//GP/GrhuTN+exg"),
    "CollisionSOS": MobileGestaltTweak("Çarpışma SOS'ini Aç", "HCzWusHQwZDea6nNhaKndw"),
    "TapToWake": MobileGestaltTweak("Dokunarak Uyandırma (iPhone SE içindir)", "yZf3GTRMGTuwSV/lD7Cagw"),
    "CameraButton": MobileGestaltMultiTweak("iPhone 16 Ayarlarını Etkinleştir", {"CwvKxM2cEogD3p+HYgaW0Q": 1, "oOV1jhJbdV3AddkcCg0AEA": 1}, min_version=Version("18.0")),
    "Parallax": MobileGestaltTweak("Parallax Duvar Kağıdını Devre dışı bırak", "UIParallaxCapability", value=0),
    "StageManager": MobileGestaltTweak("Sahne Yöneticisi'ni Etkinleştir (UYARI:Bazı Cihazlarda,Özellikle iPhone'lar da Risklidir)", "qeaj75wk3HF4DwQ8qbIi7g", value=1),
    "Medusa": MobileGestaltMultiTweak("Medusa'yı Etkinleştir (iPad'lerde bulunan Multitasking özelliği) (UYARI: Bazı telefonlarda riskli olabilir)", {"mG0AnH/Vy1veoqoLRAIgTA": 1, "UCG5MkVahJxG1YULbbd5Bg": 1, "ZYqko/XM5zD3XBfN5RmaXA": 1, "nVh/gwNpy7Jv1NOk00CMrw": 1, "uKc7FPnEO++lVhHWHFlGbQ": 1}),
    "iPadApps": MobileGestaltTweak("iPad Uygulamalarını iPhone da Çalıştır", "9MZ5AdH43csAUajl/dU+IQ", value=[1, 2]),
    "Shutter": MobileGestaltMultiTweak("Bölge Kısıtlamalarını Devre Dışı Bırak (örn. Deklanşör Sesi)", {"h63QSdBCiT/z0WU6rdQv6Q": "US", "zHeENZu+wbg7PUprwNwBWg": "LL/A"}),
    "FindMyFriends": MobileGestaltTweak("Arkadaşlarımı Bul'u Etkinleştir", "Y2Y67z0Nq/XdDXgW2EeaVg"),
    "Pencil": MobileGestaltTweak("Apple Pencil Etkinleştir", "yhHcB0iH0d1XzPO/CFd3ow"),
    "ActionButton": MobileGestaltTweak("Eylem Butonu'nu Etkinleştir", "cT44WE1EohiwRzhsZ8xEsw"),
    "InternalStorage": MobileGestaltTweak("Dahili Depolama'yı Etkinleştir (UYARI: Bazı cihazlar için risklidir, özellikle iPad'ler için)", "LBJfwOEzExRxzlAnSuI7eg"),
    "InternalInstall": MobileGestaltTweak("Apple Dahili Yükleme olarak ayarlayın (yani herhangi bir uygulamada Metal HUD)", "EqrsVvjcYDdxHBiQmGhAWw", divider_below=True),
    "EUEnabler": EligibilityTweak("Avrupa Birliği Ayarlarını Etkinleştir", divider_below=True),
    "AOD": MobileGestaltMultiTweak("Her Zaman Açık Ekran",
                            {"2OOJf1VhaM7NxfRok3HbWQ": 1, "j8/Omm6s1lsmTDFsXjsBfA": 1},
                            min_version=Version("18.0")),

    ## Popüler Özellikler
    "ClockAnim": FeatureFlagTweak("Kilit Ekranında Saat Animasyonu", flag_category='SpringBoard',
                     flag_names=['SwiftUITimeAnimation'],
                     min_version=Version("18.0")),
    "Lockscreen": FeatureFlagTweak("Kilit Ekranın'daki Uygulamaları Özelleştir", flag_category="SpringBoard",
                     flag_names=['AutobahnQuickSwitchTransition', 'SlipSwitch', 'PosterEditorKashida'],
                     min_version=Version("18.0")),
    "PhotoUI": FeatureFlagTweak("Eski Galeri Arayüzü (ios17)", flag_category='Photos', flag_names=['Lemonade'], is_list=False, inverted=True, min_version=Version("18.0")),
    "AI": FeatureFlagTweak("Apple Intelligence'ı Etkinleştir", flag_category='SpringBoard', flag_names=['Domino', 'SuperDomino'], min_version=Version("18.1"), divider_below=True),

    ## AI Etkinleştirme
    "AIEligibility": AITweak(),
    "AIGestalt": MobileGestaltTweak("Apple Intelligence'ı Etkinleştir (Desteklenmeyen Cihazlar için) (Gestalt)", "A62OafQ85EJAiiqKn4agtg", min_version=Version("18.1")),
    "SpoofModel": MobileGestaltTweak("Sahte Cihaz Modeli", "h9jDsbgj7xIVeIQ8S3/X3Q", value="iPhone17,3", min_version=Version("18.1"), divider_below=True),

    ## Springboard Tweaks
    "LockScreenFootnote": BasicPlistTweak(
        "Kilit Ekranı Dipnot Metnini Ayarla",
        FileLocation.footnote,
        key="LockScreenFootnote", value="",
        edit_type=TweakModifyType.TEXT
    ),
    "SBDontLockAfterCrash": BasicPlistTweak(
        "Yeniden Başlatma Sonrası Kilit Ekranı'nı Devredışı Bırak",
        FileLocation.springboard,
        "SBDontLockAfterCrash"
    ),
    "SBDontDimOrLockOnAC": BasicPlistTweak(
        "Şarj Sırasında Ekran Karartmayı Devre Dışı Bırak",
        FileLocation.springboard,
        "SBDontDimOrLockOnAC"
    ),
    "SBHideLowPowerAlerts": BasicPlistTweak(
        "Düşük Pil Uyarılarını Devredışı Bırak",
        FileLocation.springboard,
        "SBHideLowPowerAlerts"
    ),
    "SBNeverBreadcrumb": BasicPlistTweak(
        "Geri dönme Butonu'nu Devredışı Bırak",
        FileLocation.springboard,
        "SBNeverBreadcrumb"
    ),
    "SBShowSupervisionTextOnLockScreen": BasicPlistTweak(
        "Kilit Ekranında Supervision Metnini Göster",
        FileLocation.springboard,
        "SBShowSupervisionTextOnLockScreen"
    ),
    "AirplaySupport": BasicPlistTweak(
        "Sahne Yöneticisi için AirPlay desteğini etkinleştirin",
        FileLocation.springboard,
        "SBExtendedDisplayOverrideSupportForAirPlayAndDontFileRadars",
        divider_below=True
    ),

    ## Dahili Seçenekler
    "SBBuildNumber": BasicPlistTweak(
        "Durum Çubuğunda Yapı Sürümünü Göster",
        FileLocation.globalPreferences,
        "UIStatusBarShowBuildVersion"
    ),
    "RTL": BasicPlistTweak(
        "Sağdan Sola Düzeni Zorla(RTL)",
        FileLocation.globalPreferences,
        "NSForceRightToLeftWritingDirection"
    ),
    "MetalForceHudEnabled": BasicPlistTweak(
        "Metal HUD Hata Ayıklamayı Etkinleştir",
        FileLocation.globalPreferences,
        "MetalForceHudEnabled"
    ),
    "AccessoryDeveloperEnabled": BasicPlistTweak(
        "Aksesuar Hata Ayıklamayı Etkinleştir",
        FileLocation.globalPreferences,
        "AccessoryDeveloperEnabled"
    ),
    "iMessageDiagnosticsEnabled": BasicPlistTweak(
        "iMessage Hata Ayıklamayı Etkinleştir",
        FileLocation.globalPreferences,
        "iMessageDiagnosticsEnabled"
    ),
    "IDSDiagnosticsEnabled": BasicPlistTweak(
        "Süreklilik Hata Ayıklamayı Etkinleştir",
        FileLocation.globalPreferences,
        "IDSDiagnosticsEnabled"
    ),
    "VCDiagnosticsEnabled": BasicPlistTweak(
        "FaceTime Hata Ayıklamayı Etkinleştir",
        FileLocation.globalPreferences,
        "VCDiagnosticsEnabled"
    ),
    "AppStoreDebug": BasicPlistTweak(
        "App Store Hata Ayıklama Hareketini Etkinleştir",
        FileLocation.appStore,
        "debugGestureEnabled"
    ),
    "NotesDebugMode": BasicPlistTweak(
        "Notlar Uygulaması Hata Ayıklama Modunu Etkinleştir",
        FileLocation.notes,
        "DebugModeEnabled"
    ),
    "BKDigitizerVisualizeTouches": BasicPlistTweak(
        "Hata Ayıklama Bilgileriyle Dokunuşları Göster",
        FileLocation.backboardd,
        "BKDigitizerVisualizeTouches"
    ),
    "BKHideAppleLogoOnLaunch": BasicPlistTweak(
        "Yeniden Başlat Simgesini Gizle",
        FileLocation.backboardd,
        "BKHideAppleLogoOnLaunch"
    ),
    "EnableWakeGestureHaptic": BasicPlistTweak(
        "Uyandırmak için Kaldırıldığında Titreşim",
        FileLocation.coreMotion,
        "EnableWakeGestureHaptic"
    ),
    "PlaySoundOnPaste": BasicPlistTweak(
        "Yapıştırırken Sesi Çal",
        FileLocation.pasteboard,
        "PlaySoundOnPaste"
    ),
    "AnnounceAllPastes": BasicPlistTweak(
        "Sistem Yapıştırmaları için Bildirimleri Göster",
        FileLocation.pasteboard,
        "AnnounceAllPastes"
    )
}
