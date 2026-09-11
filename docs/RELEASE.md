# Release Process

1. Update `VERSION` using semantic versioning.
2. Update `CHANGELOG.md`.
3. Run `python3 scripts/validate_toolkit.py`.
4. Run `./scripts/package_release.sh`.
5. Review generated ZIP contents before publishing.
