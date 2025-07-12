#include "main.h"

//extern Settings_t settings;
//Settings_t settingsToSave;
//extern PublicSettings_t pSettings;
//uint8_t mapOfAddresses [sizeof(PublicSettings_t) / 2] = { 0xFF };
//uint16_t initialized = 0;

// uint8_t FULLY_EDITABLE = 0xFF;
// uint8_t PARTIALLY_EDITABLE = 0x0F;
// uint8_t NOT_EDITABLE = 0x00;

//crc
uint16_t crc16(uint8_t *adr_buffer, uint32_t byte_cnt);
//init
void initSettings();
void SetDefaults();
uint16_t getRegAddrOfSetting(uint32_t addr);
uint16_t getRegAddrOfPublicSetting(uint32_t addr);
void setAccessPermission(uint32_t addr, uint8_t permission, uint8_t size);
void initMap();
void putAllData();
void updateAllData();
void checkLock();