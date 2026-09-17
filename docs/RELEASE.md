# Release Process

1. Update `VERSION` using semantic versioning.
2. Update `CHANGELOG.md`.
3. Run `sa-kit validate` (or `python3 scripts/sakit.py validate`).
4. Run `./scripts/package_release.sh`.
5. Review generated ZIP contents before publishing.
