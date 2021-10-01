from autopub.plugins import hookimpl
from autopub.plugins.trigger import AfterReleaseEvent


@hookimpl
def after_release(payload: AfterReleaseEvent):
    print('after release:', payload)
