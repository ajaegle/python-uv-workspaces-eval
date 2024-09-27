# Python UV workspaces evaluation

Figuring out how `uv` deals with nested projects. See git history for detailed changes after every step.

The `outer` project contains two nested ones (`first` and `second`). The nested projects were created by simply running `uv init first` inside the `outer` dir. This sets up the uv workspace in the `outer` project.

```shell
.
├── README.md
├── first
│   ├── README.md
│   ├── call.py
│   ├── hello.py
│   └── pyproject.toml
├── hello.py
├── pyproject.toml
├── second
│   ├── README.md
│   ├── hello.py
│   └── pyproject.toml
└── uv.lock
```

Dependencies added in a nested project e.g. `uv add httpx` are tracked in the nested projects' files. Still, there is only a single virtual environment (the outer one).

This workspace approach allows importing modules from the nested project in the outer one. Still, it is necessary to `uv sync` the nested projects individually. This neither happens on `uv sync` nor implicitly on `uv run hello.py` in the outer one.
