from __future__ import annotations
from plugins.base import BasePlugin

class HeartbeatTestPlugin(BasePlugin):
    @property
    def name(self): return "heartbeat_test"

    @property
    def version(self): return "1.0.0"

    async def setup(self, ctx):
        self.ticks = 0
        async def tick():
            self.ticks += 1
        ctx.provide_service("heartbeat_test.status", self)
        ctx.schedule_interval("heartbeat", 0.02, tick, persist=False)

    async def teardown(self):
        self.ticks = -1

PLUGIN = HeartbeatTestPlugin
