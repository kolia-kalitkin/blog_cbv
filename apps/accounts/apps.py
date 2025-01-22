from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    verbose_name = 'Аккаунты'
    
    # переопределили метод ready() в классе конфигурации пользовательского приложения для выполнения задачи инициализации, которая регистрирует сигналы
    def ready(self):    
        import apps.accounts.signals