def get_status_code(module, x):
    if x == module.StatusCode.GenFound:
        return 200
    if x == module.StatusCode.GenNotFound:
        return 404
    if x == module.StatusCode.GenNotFromSupportedTemplate:
        return 400
    raise Exception("Unrecognized StatusCode")
