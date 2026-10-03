from __future__ import annotations
import ast, json, pathlib, sys

root = pathlib.Path('plugins')
seen = []
for d in sorted(p for p in root.iterdir() if p.is_dir()):
    manifest = json.loads((d / 'manifest.json').read_text())
    assert manifest['name'] == d.name, (d, manifest)
    tree = ast.parse((d / 'plugin.py').read_text())
    assert any(isinstance(n, ast.ClassDef) for n in tree.body)
    assert (d / 'README.md').exists()
    seen.append(d.name)
assert seen == ['database_test', 'failure_test', 'heartbeat_test'], seen
assert (root / 'database_test/migrations/0001_probe.sql').exists()
print('PLUGIN_CONTRACT_OK', ','.join(seen))
