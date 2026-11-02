#!/usr/bin/env python3
"""Writes target/motion_blur-<version>.hnmod: horizon-native.json and the mixin bundle, with fixed
bytes and times, so the same sources always make the same file."""
import hashlib
import json
from pathlib import Path
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'mixins/motion_blur'


def package():
    compat = json.loads((ROOT / 'compatibility.json').read_text())
    mixin = tomllib.loads((BUNDLE / 'horizon-mixin.toml').read_text())
    version = mixin['mod']['version']
    assert compat['hooks'] and compat['horizon_revision'], 'set hooks and horizon_revision first'
    assert mixin['compatibility']['horizon_revision'] == compat['horizon_revision']
    runtime = (BUNDLE / 'motion_blur.rs').read_text()
    assert f'pub const VERSION: &str = "{version}";' in runtime, 'VERSION in motion_blur.rs'
    manifest = dict(schema=1, id='motion_blur', version=version, game=compat['game'],
                    hooks=compat['hooks'], horizon=compat['horizon_revision'],
                    mixins=compat['horizon_mixins_revision'])
    files = {'horizon-native.json': (json.dumps(manifest, indent=2, sort_keys=True) + '\n').encode()}
    for path in sorted(BUNDLE.iterdir()):
        if path.suffix in ('.rs', '.toml'):
            files[str(path.relative_to(ROOT))] = path.read_bytes()
    out = ROOT / 'target' / f'motion_blur-{version}.hnmod'
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    print(json.dumps(dict(file=str(out), size=out.stat().st_size,
                          sha256=hashlib.sha256(out.read_bytes()).hexdigest()), indent=2))


if __name__ == '__main__':
    package()
