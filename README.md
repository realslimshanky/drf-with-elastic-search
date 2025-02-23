# Django search api with Elastic Search

## Installation

The package uses poetry to manage dependencies.

```bash
make install
```

## Development Server

Make sure to update `.env` with Elastic search credentials before running the
following command.

```bash
make run
```

Discoverable API can be found here
[http://127.0.0.1:8000/search/images/](http://127.0.0.1:8000/search/images/)