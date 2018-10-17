# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
 - Docstring for `request` package
   - Docstring for `AirmoreSession` class

## [0.1.0a9] - 2018-10-17
### Changed
 - Travis will upload to Pypi on only tags

## [0.1.0a8] - 2018-10-17
### Changed
 - Now Travis deploys if branch is master

## [0.1.0a7] - 2018-10-17
### Changed
 - Now Travis deploys after covarage

## [0.1.0a6] - 2018-10-17
### Added
 - Automatic releases on Pypi after test is successful on master with a tag in Travis

## [0.1.0a5] - 2018-10-16
### Changed
 - `AirmoreSession::is_server_running` timeout has been set to 2 seconds
   - refers to #2
   - closes #3

## [0.1.0a3] - 2018-10-16
### Changed
 - `DeviceService::fetch_device_detail` returns `DeviceDetail` instance
 - `Service::request` now returns `requests.Response`

### Added
 - `DeviceService::take_screenshot` returns `Image` instance from Pillow
 - `DeviceScreenshotProcess`
 - `DeviceDetail`
 
### Removed
 - Properties for device detail moved from `DeviceService` to `DeviceDetail`

## [0.1.0a2] - 2018-10-16
### Changed
 - Travis links on readme

## [0.1.0a1] - 2018-10-16
### Changed
 - Changelog
 - Readme
 - Versioning

## [0.1.0-pre] - 2018-10-16
### Added
 - `AirmoreSession` which extends `requests.Session` helping to create an
 easier-to-manage session for Airmore servers.
 - `Service`s to manage different functionalities of an Airmore server
   - `DeviceService` provides detailed information about device
 - `Process` to manage different aspects of a `Service`, which also extends
 `requests.PreparedRequest`.
   - `DeviceDetailProcess` to request to device detail endpoint of Airmore server
 - Documentation about getting started
