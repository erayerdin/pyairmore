# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
 - Test server for testing

### Changed
 - All tests to test server
 - API from ground up
 - Tests to `mkdocs`
 - Style to PEP8

## [0.1.0a13] - 2018-10-22
### Fixed
 - ModuleNotFoundError: No module named 'pyairmore.services' | [#9](https://github.com/erayerdin/pyairmore/issues/9)
 - Cache Travis Dependencies | [#11](https://github.com/erayerdin/pyairmore/issues/11)
 - Adding Requests Upgrade to Pip in Travis | [#10](https://github.com/erayerdin/pyairmore/issues/10)
 - Importing `services.device` Package Fails in PIL is not Found | [#8](https://github.com/erayerdin/pyairmore/issues/8)

## [0.1.0a12] - 2018-10-20
### Changed
 - `AirmoreSession::is_server_running` now uses socket instead of `requests`
 for faster, accurate and consistent check of Airmore server
 - `Service::request` method's logic to check and request authorization
 properly, prefeferably via `AirmoreSession::is_server_running` and
 `AirmoreSession::request_authorization`
 - RTD config from `setup_py_install` to `pip install`
 - Documentation
   - "Getting Started > Starting A Section" is simplified.
   - "Getting Started > Getting Device's Info" refers to "Services > Device Service"

### Added
 - `AirmoreSession::is_application_open` property
 - Documentation
   - "Session" chapter

## [0.1.0a11] - 2018-10-17
### Added
 - "Services" chapter for documentation
   - "Device Services" section

### Changed
 - Minor stylistic fixes

## [0.1.0a10] - 2018-10-17
### Added
 - Docstring for `request` package
   - Docstring for `AirmoreSession` class
 - Docstring for root package
 - Docstring for `services` package
   - Docstring for `Service` class
   - Docstring for `Process` class
   - Docstring for `ServerUnreachableException`
   - Docstring for `AuthorizationException`
 - Docstring for `services.device` package
   - Docstring for `DeviceDetail` class
   - Docstring for `DeviceDetailProcess`
   - Docstring for `DeviceScreenshotProcess`
   - Docstring for `DeviceService`

### Changed
 - Refactored `ServerIdleException` to `ServerUnreachableException`

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
