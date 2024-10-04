from tempfile import TemporaryDirectory
from pathlib import Path

from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.mobilebackup2 import Mobilebackup2Service
from pymobiledevice3.exceptions import PyMobileDevice3Exception
from pymobiledevice3.services.diagnostics import DiagnosticsService
from pymobiledevice3.lockdown import LockdownClient

from . import backup

def perform_restore(backup: backup.Backup, reboot: bool = False, lockdown_client: LockdownClient = None):
    try:
        with TemporaryDirectory() as backup_dir:
            backup.write_to_directory(Path(backup_dir))
            
            if lockdown_client == None:
                lockdown_client = create_using_usbmux()
            with Mobilebackup2Service(lockdown_client) as mb:
                mb.restore(backup_dir, system=True, reboot=False, copy=False, source=".")
    except PyMobileDevice3Exception as e:
        if "Find My" in str(e):
            print("Bu aracı kullanabilmek için Bul özelliğinin devre dışı bırakılması gerekir.")
            print("Ayarlar'dan (Ayarlar -> [Adınız] -> Bul) Bul özelliğini devre dışı bırakın ve ardından tekrar deneyin.")
            raise e
        elif "crash_on_purpose" not in str(e):
            raise e
        else:
            if reboot and lockdown_client != None:
                print("Başarılı! Cihazınız yeniden başlatılıyor...")
                with DiagnosticsService(lockdown_client) as diagnostics_service:
                    diagnostics_service.restart()
                print("Bul'u açmayı unutmayın!")
