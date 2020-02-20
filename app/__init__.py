import logging

from sanic import Sanic

from app.config import Config
from app.blueprints.order import router as order_router


CONFIG = Config().config_vars


def create_app(*args, **kwargs):
    # Initialize app
    app = Sanic('mother-exchange')

    # config app
    app.config.from_object(CONFIG)

    # register app routes
    app.register_blueprint(order_router.bp)

    # set logging
    logging.basicConfig(
        level=10,
        filename=CONFIG.LOG_FILENAME if CONFIG.LOG_SAVE else None,
        format=CONFIG.LOG_FORMAT
    )
    logger = logging.getLogger('cors')
    logger.level = CONFIG.LOG_LEVEL

    @app.shell_context_processor
    def make_shell():
        return {'app': app}

    return app

    




