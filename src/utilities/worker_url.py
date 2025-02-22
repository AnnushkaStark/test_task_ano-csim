from config.configs import rabbit_settings


def get_url() -> str:
    return f"ampq://{rabbit_settings.RABBIT_USER}:{rabbit_settings.RABBIT_PASSWORD}@{rabbit_settings.RABBIT_HOST}/"  # noqa: E501
