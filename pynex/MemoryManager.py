# import re
#
# import server
#
#
# class MemoryManager:
#     def __init__(self):
#         self.server = server.Server
#         self.memory_limit = None
#         self.global_memory_limit = None
#         self.check_rate = None
#         self.check_ticker = 0
#         self.low_memory = False
#
#         self.continuous_trigger = True
#         self.continuous_trigger_rate = None
#         self.continuous_trigger_count = 0
#         self.continuous_trigger_ticker = 0
#
#         self.garbage_collection_period = None
#         self.garbage_collection_ticker = 0
#         self.garbage_collection_trigger = None
#         self.garbage_collection_async = None
#
#         self.lowmem_chunk_radius_override = None
#         self.lowmem_chunk_gc=None
#
#         self.lowmem_disable_chunk_cache = None
#         self.lowmem_clear_world_cache = None
#
#         self.dump_workers = None
#         self.init()
#
#     def init(self):
#         self.memory_limit = (self.server.get_property("memory.main-limit", 0)) * 1024 * 1024
#         print(self.memory_limit)
#         default_memory = 1024
#         # matches = re.findall("/([0-9]+)([KMGkmg])/", self.server.get_config_string("memory-limit", ""))
#         # if len(matches) > 0:
#         #     m = matches[1]
#         #     if m <= 0:
#         #         default_memory = 0
#         #     else:
#         #         if str(matches[2]).upper() is 'K':
#         #             default_memory = m / 1024
#         #         elif str(matches[2]).upper() is 'M':
#         #             default_memory = m
#         #         elif str(matches[2]).upper() is 'G':
#         #             default_memory = m * 1024
#         #         else:
#         #             default_memory = m
#         #
#         # pass
#
#     def is_low_memory(self):
#         pass
