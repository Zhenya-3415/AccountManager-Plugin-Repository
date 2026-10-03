from __future__ import annotations
from plugins.base import BasePlugin

class DatabaseTestPlugin(BasePlugin):
    @property
    def name(self): return "database_test"

    @property
    def version(self): return "1.0.0"

    async def setup(self, ctx):
        await ctx.db.execute("INSERT INTO plugin_probe(value) VALUES (?)", ("loaded",))

PLUGIN = DatabaseTestPlugin
