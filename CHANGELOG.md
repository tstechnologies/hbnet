# Changelog

## pre_pre v0.0.1-apha/xxx - Ongoing

### 3/2022

#### Data Gateway
* Implemented External Services API via MQTT, see [HBNet External Services](https://github.com/kf7eel/hbnet_external_services)
* Implement IPv4/UDP packet generation for SMS
* SMS data length now variable
* Added "DMR Standard" format to generated SMS (Used Anytone to reverse engineer, uses UTF-16LE, not UTF-16BE, per ETSI(why?))
* Added ARS response, still WIP
* Added dictionary to keep track of subscriber SMS format

#### Web Service
* Fix APRS settings on registration
* Add help page for data gateway
