import os
from dotenv import load_dotenv
from typing import Dict, Any

class AppConfig:
    """Centralized configuration that remains implementation-agnostic"""
    
    @classmethod
    def load(cls) -> Dict[str, Any]:
        load_dotenv()
        return {
            'storage': {
                'type': os.getenv('STORAGE_TYPE', 'memory'),  # 'memory' or 'database'
                'database': {
                    'dialect': os.getenv('DB_DIALECT', 'postgresql'),
                    'user': os.getenv('DB_USER'),
                    'password': os.getenv('DB_PASSWORD'),
                    'host': os.getenv('DB_HOST'),
                    'port': os.getenv('DB_PORT'),
                    'name': os.getenv('DB_NAME')
                }
            }
        }