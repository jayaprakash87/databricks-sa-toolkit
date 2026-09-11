# Release Process

1. Update `VERSION` using semantic versioning.
2. Update `MANIFEST.json` if skill inventory changed.
3. Update `CHANGELOG.md`.
4. Run `python3 scripts/validate_toolkit.py`.
5. Run `./scripts/package_release.sh`.
6. Review generated ZIP contents before publishing.
