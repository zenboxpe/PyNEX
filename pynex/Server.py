#####################################
#  _____       _   _ ________   __  #
# |  __ \     | \ | |  ___ \ \ / /  #
# | |__) |   _|  \| | |__   \ V /   #
# |  ___/ | | | . ` |  __|   > <    #
# | |   | |_| | |\  | |____ / . \   #
# |_|    \__, |_| \_|______/_/ \_\  #
#         __/ |MCBE Server Software #
#        |___/                      #
#####################################
        
import base64
import getopt
import os
from pathlib import Path

from logzero import logger

from pynex.utils import *

class ServerError(Exception):
    pass


class Server:
    BROADCAST_CHANNEL_ADMINISTRATIVE = "pynex.broadcast.admin"
    BROADCAST_CHANNEL_USERS = "pynex.broadcast.user"

    tick_sleeper = None
    ban_by_name = None
    ban_by_ip = None
    operators = None
    whitelist = None
    is_running = True
    has_stopped = False
    plugin_manager = None
    profiling_tickrate = 20
    updater = None
    async_pool = None
    """counts the ticks since the server start"""
    tick_counter = 0
    next_tick = 0
    tick_average = {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20}
    use_average = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
    current_tps = 20
    current_use = 0

    do_title_tick = True
    send_usage_ticker = 0
    dispatch_signals = False
    logger = None
    memory_manager = None
    console = None
    command_map = None
    crafting_manager = None
    resource_manager = None
    max_players = None
    online_mode = True
    auto_save = None
    rcon = None

    entity_metadata = None
    player_metadata = None
    level_metadata = None

    network = None
    network_compression_async = None

    auto_tick_rate = True
    auto_tick_rate_limit = 20
    always_tick_players = False
    base_tick_rate = 1

    auto_save_ticker = 0
    auto_save_ticks = 6000

    language = None
    force_language = False

    server_id = None

    auto_loader = None
    data_path = None
    plugin_path = None

    unique_players = None

    query_handler = None

    query_regenerate_task = None

    properties: Config = None
    property_cache = []

    config = None
    players = None
    logged_in_players = None
    player_list = None
    levels = None
    level_default = None
    def __init__(self, data_path, plugin_path):
        self.instance = self

        # TODO: SleeperHandler
        self.tick_sleeper = ''

        try:
            if not Path(data_path + "worlds/").is_dir():
                os.mkdir(data_path + "worlds/", 0o777)

            if not Path(data_path + "players/").is_dir():
                os.mkdir(data_path + "players/", 0o777)

            if not Path(plugin_path).is_dir():
                os.mkdir(plugin_path, 0o777)

            self.data_path = os.path.realpath(data_path)
            self.plugin_path = os.path.realpath(plugin_path)

            logger.info("Loading pyromine.yml")
            if not os.path.exists(data_path + "pyromine.yml"):
                content = 'test: test'
            self.config = Config(data_path + "pyromine.yml", Config.YAML, [])

            # DEBUG = int(self.get_property("debug.level", 1))

            logger.info("Loading server properties...")

            conf_sec = dict()
            conf_sec["motd"] = "MCBE Server"
            conf_sec["sub-motd"] = "PyNEX Server"
            conf_sec["server-port"] = 19132
            conf_sec["server-ip"] = "0.0.0.0"
            conf_sec["view-distance"] = 8
            conf_sec["white-list"] = False
            conf_sec["achievements"] = True
            conf_sec["announce-player-achievements"] = True
            conf_sec["spawn-protection"] = 16
            conf_sec["max-players"] = 20
            conf_sec["allow-flight"] = False
            conf_sec["spawn-animals"] = False
            conf_sec["spawn-mobs"] = False
            conf_sec["gamemode"] = 0
            conf_sec["force-gamemode"] = False
            conf_sec["hardcore"] = False
            conf_sec["pvp"] = True
            conf_sec["difficulty"] = 1
            conf_sec["generator-settings"] = ""
            conf_sec["level-name"] = "world"
            conf_sec["level-seed"] = ""
            conf_sec["level-type"] = "DEFAULT"
            conf_sec["allow-nether"] = True
            conf_sec["enable-query"] = True
            conf_sec["enable-rcon"] = False
            conf_sec["rcon.password"] = base64.b64encode(os.urandom(20))[3:10].decode()
            conf_sec["auto-save"] = True
            conf_sec["force-resources"] = False
            conf_sec["bug-report"] = True
            conf_sec["xbox-auth"] = 

            self.properties = Config(self.data_path + "server.properties", Config.PROPERTIES, conf_sec)

            self.memory_manager = memory_manager.MemoryManager()

            # pool_size = self.get_property("settings.async-workers", "auto")
            # if pool_size is "auto":
            #     pool_size = 2
            #     # TODO: processor
            #     processor = 0
            #
            #     if processor > 0:
            #         pool_size = max(1, processor)
            # else:
            #     pool_size = max(1, int(pool_size))

            # TODO: async_pool
            self.async_pool = 0

            # # TODO: network compression
            # if self.get_property("network.batch-threshold", 256) >= 0:
            #     pass
            # else:
            #     pass
            #
            # self.network_compression_async = bool(self.get_property("network.async-compression", True))
            #
            # # TODO: network cipher
            #
            # self.auto_tick_rate = bool(self.get_property("level-settings.auto-tick-rate", True))
            # self.auto_tick_rate_limit = int(self.get_property("level-settings.auto-tick-rate-limit", 20))
            # self.always_tick_players = bool(self.get_property("level-settings.always-tick-players", False))
            # self.base_tick_rate = int(self.get_property("level-settings.base-tick-rate", 1))
            #
            # # TODO: Terminal.has_formatting_close
            # self.do_title_tick = bool(self.get_property("console.title-tick", True))
            #
            # # TODO: SleeperNotifier
            # console_notifier = ''
            # # TODO: CommandReader
            # self.console = ''
            # self.tick_sleeper = ''


            logger.info("pocketmine.server.start")


        except ServerError as e:
            logger.error(e)
            pass

    def get_name(self) -> str:
        return 'pynex'

    def is_running(self) -> bool:
        return self.is_running

    def get_pynex_version(self) -> str:
        pass

    def get_version(self) -> str:
        pass

    def get_api_version(self) -> str:
        pass

    def get_file_path(self) -> str:
        pass

    def get_resource_path(self) -> str:
        pass

    def get_data_path(self) -> str:
        return self.data_path

    def get_plugin_path(self) -> str:
        return self.plugin_path

    def get_max_players(self) -> int:
        return self.max_players

    def get_online_mode(self) -> bool:
        return self.get_online_mode()

    def requires_authentication(self) -> bool:
        return self.get_online_mode()

    def get_port(self) -> int:
        pass

    def get_view_distance(self) -> int:
        pass

    def get_allowed_view_distance(self, distance) -> int:
        pass

    def get_ip(self) -> str:
        pass

    def get_server_unique_id(self):
        pass

    def get_auto_save(self, value):
        return self.auto_save

    def set_auto_save(self, value: bool):
        pass

    def get_level_type(self) -> str:
        pass

    def get_generated_structure(self) -> bool:
        pass

    def get_gamemode(self) -> int:
        pass

    def get_force_gamemode(self) -> bool:
        pass

    @staticmethod
    def get_gamemode_string(mode: int) -> str:
        pass

    @staticmethod
    def get_gamemode_name(mode: int) -> str:
        pass

    @staticmethod
    def get_gamemode_from_string(string: str) -> int:
        pass

    def get_difficulty(self) -> int:
        pass

    def has_whitelist(self) -> bool:
        pass

    def get_spawn_radius(self) -> int:
        pass

    def is_hardcore(self) -> bool:
        pass

    def get_default_gamemode(self) -> int:
        pass

    def get_motd(self) -> str:
        pass

    # ClassLoader - not needed
    def get_loader(self):
        return self.auto_loader

    def get_entity_metadata(self):
        return self.entity_metadata

    def get_player_metadata(self):
        return self.player_metadata

    def get_player_metadata(self):
        return self.player_metadata

    def get_level_metadata(self):
        return self.level_metadata

    def get_updater(self):
        return self.updater

    def get_plugin_manager(self):
        return self.plugin_manager

    def get_crafting_manager(self):
        return self.crafting_manager

    def get_resource_pack_manager(self):
        return self.resource_manager

    def get_async_pool(self):
        return self.async_pool

    def get_tick(self) -> int:
        return self.tick_counter

    def get_tick_per_second(self) -> float:
        return round(self.current_tps, 2)

    def get_tick_per_second_average(self) -> float:
        return round((sum(self.use_average) / len(self.use_average)) * 100, 2)

    def get_command_map(self):
        return self.command_map

    def get_logged_in_players(self):
        return self.logged_in_players

    def get_online_players(self):
        return self.player_list

    def should_save_player_data(self) -> bool:
        pass

    def get_offline_player(self, name):
        pass

    def has_offline_player_data(self, name) -> bool:
        pass

    def get_offline_player_data(self, name):
        pass

    def save_offline_player_data(self, name):
        pass

    def get_player(self):
        pass

    def get_player_exact(self):
        pass

    def match_player(self, partial_name):
        pass

    def get_player_by_raw_uuid(self, raw_uuid):
        pass

    def get_player_by_uuid(self, uuid):
        pass

    def get_level(self):
        pass

    def get_default_level(self):
        return self.level_default

    def set_default_level(self, level):
        pass

    def is_level_loaded(self, name) -> bool:
        pass

    def get_level(self, level_id):
        pass

    def get_level_by_name(self, name):
        pass

    def unload_level(self, level, force_unload=False) -> bool:
        pass

    def remove_level(self, level):
        pass

    def load_level(self, name):
        pass

    def generate_level(self, name, seed=None, generator=None, options=None) -> bool:
        pass

    def is_level_generated(self, name) -> bool:
        pass

    def find_entity(self, entity_id):
        pass

    @classmethod
    def get_property(cls, variable, default_value=None):
        # TODO: property getter
        print(variable, default_value)
        # v = getopt.getopt("", variable)
        # if variable not in cls.property_cache:
        #     v = getopt.getopt("", variable)
        #     print(v)
        #     if v[variable]:
        #         cls.property_cache[variable] = v[variable]
        #     else:
        #         cls.property_cache[variable] = cls.config.get_nested(variable)
        # return cls.property_cache[variable] if cls.property_cache[variable] else default_value

    def get_config_string(self, variable):
        pass

    def set_config_string(self, variable, value):
        pass

    def get_config_int(self, variable, default_value=0) -> int:
        pass

    def set_config_int(self, variable, value):
        pass

    def get_config_bool(self, variable, default_value=False) -> bool:
        pass

    def set_config_bool(self, variable, value):
        pass

    def get_plugin_command(self, name):
        pass

    def get_name_bans(self):
        return self.ban_by_name

    def get_ip_bans(self):
        return self.ban_by_ip

    def add_op(self, name):
        pass

    def remove_op(self, name):
        pass

    def add_whitelist(self, name):
        pass

    def remove_whitelist(self, name):
        pass

    def is_whitelisted(self, name) -> bool:
        pass

    def is_op(self, name) -> bool:
        pass

    def get_whitelisted(self):
        return self.get_whitelisted()

    def get_ops(self):
        return self.operators

    def reload_whitelist(self):
        pass

    def get_command_aliases(self):
        pass

    def get_instance(self):
        pass

    # >>>

    def broadcast_message(self, message, recipients=None):
        pass

    def broadcast_tip(self, tip, recipients=None):
        pass

    def broadcast_popup(self, popup, recipients=None):
        pass

    def broadcast_title(self, title, subtitle="", fade_in=-1, stay=-1,fade_out=-1, recipients=None):
        pass

    def broadcast(self, message, permissions):
        recipients = None

        pass

    def broadcast_packet(self, players, packet):
        pass

    def broadcast_packets(self, players, packets):
        pass

    def prepare_batch(self, stream, force_sync=False):
        pass

    def enable_plugins(self, type):
        pass

    def enable_plugin(self, plugin):
        pass

    def disable_plugins(self):
        pass

    def dispatch_command(self, sender, command_line, internal=False):
        pass

    def reload(self):
        logger.info("Saving levels...")
        pass

    def shutdown(self):
        pass

    def force_shutdown(self):
        pass

    def get_query_information(self):
        pass

    def start(self):
        pass

    def handle_signal(self, signo):
        pass

    def exception_handler(self, e, trace=None):
        pass

    def crash_dump(self):
        pass

    def __debug_info(self):
        return []

    def get_tick_sleeper(self):
        return self.tick_sleeper

    def tick_processor(self):
        pass

    def on_player_login(self, player):
        pass

    def on_player_logout(self, player):
        pass

    def add_player(self, player):
        pass

    def remove_player(self, player):
        pass

    def add_online_player(self, player):
        pass

    def remove_online_player(self, player):
        pass

    def update_playerlist_data(self, uuid, entity_id, name, skin, xbox_user_id="", players=None):
        pass

    def remove_playerlist_data(self, uuid, players=None):
        pass

    def send_full_playerlist_data(self, p):
        pass

    def check_tick_updates(self, current_tick):
        pass

    def do_auto_save(self):
        pass

    def send_usage(self, _type):
        pass

    def get_language(self):
        return self.language

    def is_language_forced(self) -> bool:
        return self.force_language()

    def get_network(self):
        return self.network()

    def get_memory_manager(self):
        return self.memory_manager

    def title_tick(self):
        pass

    def handle_packet(self, interface, address, port, payload):
        pass

    def tick(self):
        pass

    def __sleep(self):
        raise ValueError("Cannot serialize Server instance")