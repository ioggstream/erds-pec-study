# Data files and schemas for REM and PEC


## Files

```bash
.
├── documento_finale_gdl_rem_versione_1.2_28.07.2022_1.latest_version
├── en_31953204v010201p0
├── tests
└── ts_119612v020201p0  # from https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.02.01_60/
```


## Contributing

Please, see [CONTRIBUTING.md](CONTRIBUTING.md) for more details on:

- using [pre-commit](CONTRIBUTING.md#pre-commit);
- following the git flow and making good [pull requests](CONTRIBUTING.md#making-a-pr).

## Using this repository

You can create new projects starting from this repository,
so you can use a consistent CI and checks for different projects.

Besides all the explanations in the [CONTRIBUTING.md](CONTRIBUTING.md) file, you can use the docker-compose file
(e.g. if you prefer to use docker instead of installing the tools locally)

```bash
docker-compose run pre-commit
```
