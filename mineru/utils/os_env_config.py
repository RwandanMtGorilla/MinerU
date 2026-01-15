import os


def get_op_num_threads(env_name: str) -> int:
    env_value = os.getenv(env_name, None)
    return get_value_from_string(env_value, -1)


def get_load_images_timeout() -> int:
    env_value = os.getenv('MINERU_PDF_RENDER_TIMEOUT', None)
    return get_value_from_string(env_value, 300)


def get_api_request_timeout() -> int:
    """获取 API 请求超时时间（秒）

    从环境变量 MINERU_API_REQUEST_TIMEOUT 读取。
    返回 0 表示不限制超时时间。
    """
    env_value = os.getenv('MINERU_API_REQUEST_TIMEOUT', None)
    if env_value is not None:
        try:
            timeout = int(env_value)
            if timeout >= 0:
                return timeout
        except ValueError:
            pass
    return 0  # 默认不限制


def get_value_from_string(env_value: str, default_value: int) -> int:
    if env_value is not None:
        try:
            num_threads = int(env_value)
            if num_threads > 0:
                return num_threads
        except ValueError:
            return default_value
    return default_value


if __name__ == '__main__':
    print(get_value_from_string('1', -1))
    print(get_value_from_string('0', -1))
    print(get_value_from_string('-1', -1))
    print(get_value_from_string('abc', -1))
    print(get_load_images_timeout())