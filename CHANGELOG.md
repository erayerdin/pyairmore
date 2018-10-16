# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
