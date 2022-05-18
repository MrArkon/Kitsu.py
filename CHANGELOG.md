# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Added `trending_manga` function
- Added `Categories` (Replaced Genres) to Anime & Manga

## [1.0.0] - 2022-05-15
### Added
- More examples
- Implemented filter functionality
- `Manga` model
- `get_manga` & `search_manga` functions
- `NotFound` & `BadRequest` Exceptions
### Removed
- `ServerTimeout` & `KitsuError` Exceptions
## Fixed
- title bug in `Anime`
### Changed
- `_id` parameter to `anime_id` in `get_anime` & `search_anime`
- Change badges style in README

## [0.1.1] - 2021-09-17
### Added
- examples folder
- `trending_anime` method
- Add more attributes to `Anime`
### Changed
- Edit README to be more detailed and add a PyPi badge

## [0.1.0] - 2021-09-06
The First Release!
### Added
- `get_anime` method
- `Anime` model
- `KitsuError`, `HTTPException` & `ServerTimeout` errors
- Description & Badges to README.md

[Unreleased]: https://github.com/MrArkon/Kitsu.py
[1.0.0]: https://github.com/MrArkon/kitsu.py/releases/tag/v1.0.0
[0.1.1]: https://github.com/MrArkon/kitsu.py/releases/tag/v0.1.1
[0.1.0]: https://github.com/MrArkon/kitsu.py/releases/tag/v0.1.0
