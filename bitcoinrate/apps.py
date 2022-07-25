from django.apps import AppConfig


class BitcoinrateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bitcoinrate'

    def ready(self):
        from bitcoinrate import scheduler
        scheduler.start()   