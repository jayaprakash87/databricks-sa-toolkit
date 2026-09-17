# Release Process

1. Update `VERSION` using semantic versioning.
2. Update `CHANGELOG.md` and the version line in `README.md`.
3. Run `python3 -m pytest tests/ -q`.
4. Run `sa-kit validate` (or `python3 scripts/sakit.py validate`).
5. Run `./scripts/package_release.sh`.
6. Review generated ZIP contents before publishing.
