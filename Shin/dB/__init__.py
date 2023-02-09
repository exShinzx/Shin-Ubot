from .. import run_as_module

if not run_as_module:
    from ..exceptions import RunningAsFunctionLibError

    raise RunningAsFunctionLibError(
        "You are running 'Shin' as a functions lib, not as run module. You can't access this folder.."
    )

from .. import *

CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."

DEVLIST = [
    2049080295, # @Umemekk
]

cmd = CMD_HANDLER
CMD_LIST = {}

DEFAULT = [
    2049080295, # @Umemekk
]

Shin_IMAGES = [
    f"https://graph.org/file/{_}.jpg"
    for _ in [
        "9b26db2c351d68d71dc1d",
    ]
]

stickers = [

]
