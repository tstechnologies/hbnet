# Changelog

## pre_pre v0.0.1-apha/xxx - Ongoing

### 3/2022

#### Data Gateway
* Implemented External Services API via MQTT, see [HBNet External Services](https://github.com/kf7eel/hbnet_external_services)
* Fixed CSBK block generation
* Implement IPv4/UDP packet generation for SMS
* SMS data length now variable
* Added "DMR Standard" format to generated SMS 
* Add UTF-16BE per ETSI 361-3, should theoretically cover more radios 
* Added ARS response, still WIP
* Added dictionary to keep track of subscriber SMS format
* Add code to detect UDT headers and decode SMS, should now decode Hytera type SMS
* Add locally executable commands via SMS

#### Web Service
* Fix APRS settings on registration
* Add help page for data gateway
* Fix Pi-Star setup script

#### Notes
Used Anytone 878  to reverse engineer "DMR Standard", uses UTF-16LE, not UTF-16BE, per ETSI(why?) Also added UTF-16BE as an option.