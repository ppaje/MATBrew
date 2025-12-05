"""
Конфигурация гибридной системы
"""

import os
from pathlib import Path

# Базовые пути
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
LOGS_DIR = BASE_DIR / 'logs'

# Создание директорий
for directory in [DATA_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Telegram API
API_ID = 1234567  # Заменить на ваш
API_HASH = 'abcdef1234567890'  # Заменить на ваш

# Администратор
ADMIN_CHAT_ID = 123456789  # @fish_qe

# Веб-серверы
WEB_SERVER = {
    'auth_host': '0.0.0.0',
    'auth_port': 8080,
    'dashboard_host': '0.0.0.0',
    'dashboard_port': 8081,
    'debug': False,
    'secret_key': 'change-this-secret-key'
}

# Настройки аналитики
ANALYTICS_CONFIG = {
    'report_interval_hours': 24,
    'generate_charts': True,
    'store_raw_data': True,
    'data_retention_days': 90,
    'analyze_sentiment': True,
    'detect_patterns': True,
    'generate_insights': True
}

# Настройки мониторинга
MONITORING_CONFIG = {
    'forward_to_admin': True,
    'forward_media': True,
    'forward_edited': False,
    'keywords_to_monitor': [],  # Ключевые слова для отслеживания
    'excluded_chats': [],  # Чаты для исключения
    'check_interval_seconds': 1
}

# Настройки безопасности
SECURITY_CONFIG = {
    'encrypt_sessions': True,
    'encrypt_database': True,
    'require_2fa': True,
    'session_timeout_hours': 72,
    'max_login_attempts': 3
}

# Форматы отчетов
REPORT_FORMATS = {
    'json': True,
    'html': True,
    'pdf': True,
    'csv': True
}

# Визуализация
VISUALIZATION_CONFIG = {
    'theme': 'dark',
    'generate_heatmaps': True,
    'activity_timelines': True,
    'message_distribution': True,
    'response_time_analysis': True
}

# Уведомления
NOTIFICATION_CONFIG = {
    'daily_summary': True,
    'weekly_report': True,
    'important_messages': True,
    'anomaly_detection': True
}

# Логирование
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': LOGS_DIR / 'system.log',
    'max_size_mb': 10,
    'backup_count': 5
}