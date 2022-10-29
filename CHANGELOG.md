# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2022-10-29
### Removed
- `raw` keyword argument completely
### Changed
- `search_anime` and `search_manga` will always return a list of `Anime` or `Manga` instances

## [1.1.1] - 2022-06-11
### Fixed
- Category's title attribute
- Resolved a few typecheck issues

## [1.1.0] - 2022-06-03
### Added
- Added `trending_manga` function
- Added `categories` (Replaced Genres) to Anime & Manga
- Added `streaming_links` to Anime
- Added `episodes` to Anime
- Added [Documentation](https://kitsu-py.readthedocs.io/)

### Changed
- Changed the title property in `Anime` & `Manga`
  
  Now you can get different types of titles, such as `anime.title.ja_jp` will now return the japanese name of the resource. `anime.title` still works as it did before.

## [1.0.0] - 2022-05-15
### Added
- More examples
- Implemented filter functionality
- `Manga` model
- `get_manga` & `search_manga` functions
- `NotFound` & `BadRequest` Exceptions
### Removed
- `ServerTimeout` & `KitsuError` Exceptions
### Fixed
- title bug in `Anime`
### Changed
- `_id` parameter to `anime_id` in `get_anime` & `search_anime`

## [0.1.1] - 2021-09-17
### Added
- examples folder
- `trending_anime` method
- Add more attributes to `Anime`

## [0.1.0] - 2021-09-06
The First Release!
### Added
- `get_anime` method
- `Anime` model
- `KitsuError`, `HTTPException` & `ServerTimeout` errors

[Unreleased]: https://github.com/MrArkon/Kitsu.py
[1.1.2]: https://github.com/MrArkon/kitsu.py/releases/tag/v1.1.2
[1.1.1]: https://github.com/MrArkon/kitsu.py/releases/tag/v1.1.1
[1.1.0]: https://github.com/MrArkon/kitsu.py/releases/tag/v1.1.0
[1.0.0]: https://github.com/MrArkon/kitsu.py/releases/tag/v1.0.0
[0.1.1]: https://github.com/MrArkon/kitsu.py/releases/tag/v0.1.1
[0.1.0]: https://github.com/MrArkon/kitsu.py/releases/tag/v0.1.0
