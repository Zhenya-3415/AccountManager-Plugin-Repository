from __future__ import annotations
from plugins.base import BasePlugin

class FailureTestPlugin(BasePlugin):
    @property
    def name(self): return "failure_test"

    @property
    def version(self): return "1.0.0"

    async def setup(self, ctx):
        ctx.provide_service("failure_test.before_error", True)
        raise RuntimeError("intentional failure-test plugin error")

PLUGIN = FailureTestPlugin
