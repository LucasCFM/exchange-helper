import logging, os


class BaseConfig(object):
    # SANIC BASICS - https://sanic.readthedocs.io/en/latest/sanic/config.html (CHECK IT OUT)
    REQUEST_TIMEOUT = 10
    RESPONSE_TIMEOUT = 10
    KEEP_ALIVE_TIMEOUT = 5
    
    LOG_FORMAT = '%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s'
    LOG_LEVEL = logging.DEBUG
    LOG_SAVE = True
    LOG_FILENAME = 'exchange-helper.log'

    EXCHANGE_CONNECTOR_URL = os.getenv('EXCHANGE_CONNECTOR_URL', 'http://localhost:3000/api')
    BAD_REQUEST_MAX_ATTEMPT = 1

    TICK_SIZE = 0.5

    # MAX_LEVERAGE = 5
    # MIN_LEVERAGE = 1


class DevConfig(BaseConfig):
    ENVIRONMENT = 'development'


class ProdConfig(BaseConfig):
    ENVIRONMENT = 'production'

    # SANIC BASICS - https://sanic.readthedocs.io/en/latest/sanic/config.html (CHECK IT OUT)
    REQUEST_TIMEOUT = 3
    RESPONSE_TIMEOUT = 5
    KEEP_ALIVE_TIMEOUT = 5
    PROXIES_COUNT = 1
    
    LOG_LEVEL = logging.DEBUG # TODO: Change to INFO
    
    EXCHANGE_CONNECTOR_URL = os.getenv('EXCHANGE_CONNECTOR_URL', 'http://localhost:3000/api')
    if not EXCHANGE_CONNECTOR_URL:
        raise Exception('Must inform a EXCHANGE_CONNECTOR_URL')
    BAD_REQUEST_MAX_ATTEMPT = 3


class Config():
    """ Class instance for singleton """

    class __Config():
        """ Private singleton class """
        def __init__(self, config: BaseConfig):
            self.config = config

    instance = None

    def __init__(self, config: BaseConfig = None):
        if not config and not Config.instance:
            raise Exception('Config singleton has not been set yet')
        if config:
            Config.instance = Config.__Config(config)
    
    @property
    def config_vars(self) -> BaseConfig:
        return Config.instance.config


def set_config_var(env_type='development'):
    print(f'Initializing config singleton for env: {env_type}')
    if 'dev' in env_type:
        Config(DevConfig)
    else:
        Config(ProdConfig)

set_config_var( os.getenv('ENV_TYPE', 'development') )
