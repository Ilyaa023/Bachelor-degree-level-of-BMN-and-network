#include "utils.h"
#include "flash_manager.h"
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
uint16_t crc16(uint8_t *adr_buffer, uint32_t byte_cnt)
{
	register uint16_t crc = 0xFFFF;
	static const uint16_t table[] =
	{
		0x0000, 0xC0C1, 0xC181, 0x0140, 0xC301, 0x03C0, 0x0280, 0xC241,
		0xC601, 0x06C0, 0x0780, 0xC741, 0x0500, 0xC5C1, 0xC481, 0x0440,
		0xCC01, 0x0CC0, 0x0D80, 0xCD41, 0x0F00, 0xCFC1, 0xCE81, 0x0E40,
		0x0A00, 0xCAC1, 0xCB81, 0x0B40, 0xC901, 0x09C0, 0x0880, 0xC841,
		0xD801, 0x18C0, 0x1980, 0xD941, 0x1B00, 0xDBC1, 0xDA81, 0x1A40,
		0x1E00, 0xDEC1, 0xDF81, 0x1F40, 0xDD01, 0x1DC0, 0x1C80, 0xDC41,
		0x1400, 0xD4C1, 0xD581, 0x1540, 0xD701, 0x17C0, 0x1680, 0xD641,
		0xD201, 0x12C0, 0x1380, 0xD341, 0x1100, 0xD1C1, 0xD081, 0x1040,
		0xF001, 0x30C0, 0x3180, 0xF141, 0x3300, 0xF3C1, 0xF281, 0x3240,
		0x3600, 0xF6C1, 0xF781, 0x3740, 0xF501, 0x35C0, 0x3480, 0xF441,
		0x3C00, 0xFCC1, 0xFD81, 0x3D40, 0xFF01, 0x3FC0, 0x3E80, 0xFE41,
		0xFA01, 0x3AC0, 0x3B80, 0xFB41, 0x3900, 0xF9C1, 0xF881, 0x3840,
		0x2800, 0xE8C1, 0xE981, 0x2940, 0xEB01, 0x2BC0, 0x2A80, 0xEA41,
		0xEE01, 0x2EC0, 0x2F80, 0xEF41, 0x2D00, 0xEDC1, 0xEC81, 0x2C40,
		0xE401, 0x24C0, 0x2580, 0xE541, 0x2700, 0xE7C1, 0xE681, 0x2640,
		0x2200, 0xE2C1, 0xE381, 0x2340, 0xE101, 0x21C0, 0x2080, 0xE041,
		0xA001, 0x60C0, 0x6180, 0xA141, 0x6300, 0xA3C1, 0xA281, 0x6240,
		0x6600, 0xA6C1, 0xA781, 0x6740, 0xA501, 0x65C0, 0x6480, 0xA441,
		0x6C00, 0xACC1, 0xAD81, 0x6D40, 0xAF01, 0x6FC0, 0x6E80, 0xAE41,
		0xAA01, 0x6AC0, 0x6B80, 0xAB41, 0x6900, 0xA9C1, 0xA881, 0x6840,
		0x7800, 0xB8C1, 0xB981, 0x7940, 0xBB01, 0x7BC0, 0x7A80, 0xBA41,
		0xBE01, 0x7EC0, 0x7F80, 0xBF41, 0x7D00, 0xBDC1, 0xBC81, 0x7C40,
		0xB401, 0x74C0, 0x7580, 0xB541, 0x7700, 0xB7C1, 0xB681, 0x7640,
		0x7200, 0xB2C1, 0xB381, 0x7340, 0xB101, 0x71C0, 0x7080, 0xB041,
		0x5000, 0x90C1, 0x9181, 0x5140, 0x9301, 0x53C0, 0x5280, 0x9241,
		0x9601, 0x56C0, 0x5780, 0x9741, 0x5500, 0x95C1, 0x9481, 0x5440,
		0x9C01, 0x5CC0, 0x5D80, 0x9D41, 0x5F00, 0x9FC1, 0x9E81, 0x5E40,
		0x5A00, 0x9AC1, 0x9B81, 0x5B40, 0x9901, 0x59C0, 0x5880, 0x9841,
		0x8801, 0x48C0, 0x4980, 0x8941, 0x4B00, 0x8BC1, 0x8A81, 0x4A40,
		0x4E00, 0x8EC1, 0x8F81, 0x4F40, 0x8D01, 0x4DC0, 0x4C80, 0x8C41,
		0x4400, 0x84C1, 0x8581, 0x4540, 0x8701, 0x47C0, 0x4680, 0x8641,
		0x8201, 0x42C0, 0x4380, 0x8341, 0x4100, 0x81C1, 0x8081, 0x4040
	};

	register uint8_t lut;
	/* CRC Generation Function */
	while( byte_cnt--) /* pass through message buffer */
	{
		lut = crc^ *adr_buffer++;
		crc  = (crc >> 8) ^ table[lut];
	}
	return crc;
}

//init
void initSettings()
{
//  if (read_from_default_page(&settings) != 0) {
//    SetDefaults();
//  }
////  settings.generalSettings.eventAttr = 0;
////
////  pSettings.generalSettings.editSettingsRegister = 0;
}

void SetDefaults() {
//  uint8_t flashCount = settings.generalSettings.saveCounter;
//  uint8_t *ts = (uint8_t *) &settings;
////  for (uint16_t i = 0; i < sizeof(Settings_t); i++){
////    *ts++ = 0;
////  }
//
////  settings.generalSettings.saveCounter = flashCount;
////  write_to_default_page(&settings);
}

void SetUserDefaults() {
//  uint8_t *ts = (uint8_t *) &settings;
//  for (uint16_t i = 0; i < sizeof(Settings_t); i++){
//    *ts++ = 0;
//  }

//  write_to_default_page(&settings);
}

uint16_t getRegAddrOfSetting(uint32_t addr){
//  uint32_t sa = (uint32_t) &settings;
//  return (uint16_t) (addr - sa) / 2;
}

uint16_t getRegAddrOfPublicSetting(uint32_t addr){
//  uint32_t sa = (uint32_t) &pSettings;
//  return (uint16_t) (addr - sa) / 2;
}

void setAccessPermission(uint32_t addr, uint8_t permission, uint8_t size){
//  if (permission != FULLY_EDITABLE &&
//      permission != PARTIALLY_EDITABLE &&
//      permission != NOT_EDITABLE)
  	return;
//  uint32_t psa = (uint32_t) &pSettings;
//  uint32_t maa = (uint32_t) &mapOfAddresses;
//  addr = maa + (addr - psa) / 2;
//  for (uint8_t i = 0; i < size / 2; i++)
//  	mapOfAddresses[(addr - psa) / 2 + i] = permission;
//    *(__IO uint8_t*) (addr + i) = permission;
}

void initMap(){
//   for (int i = 0; i < sizeof(Settings_t) / 2; i++)
//     mapOfAddresses[i] = 0xFFFF;

//  initialized = 1;
  return;

//	setAccessPermission((uint32_t) &pSettings.generalSettings.voltage, NOT_EDITABLE, sizeof(float32_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.versionHi, NOT_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.versionLo, NOT_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.voltageSetPointFlag, NOT_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.eventAttr, NOT_EDITABLE, sizeof(uint32_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.saveCounter, NOT_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.XT_connectError, NOT_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.TBUS_connectError, NOT_EDITABLE, sizeof(uint16_t));
//
//	setAccessPermission((uint32_t) &pSettings.generalSettings.voltageSetPoints.low, FULLY_EDITABLE, sizeof(float32_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.voltageSetPoints.high, FULLY_EDITABLE, sizeof(float32_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.warmUpSec, FULLY_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.displayOffTime, FULLY_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.editSettingsRegister, FULLY_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.ModBusSpeedTBUS, FULLY_EDITABLE, sizeof(float32_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.ModBusSpeedXT, FULLY_EDITABLE, sizeof(float32_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.ModBusAddr, FULLY_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.id_powerWarningHigh, FULLY_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.generalSettings.id_powerWarningLow, FULLY_EDITABLE, sizeof(uint16_t));
//
//	setAccessPermission((uint32_t) &pSettings.generalSettings.coeffVoltageCorrect, PARTIALLY_EDITABLE, sizeof(float32_t));
//
//	setAccessPermission((uint32_t) &pSettings.quitAll, FULLY_EDITABLE, sizeof(uint16_t));
//
//	setAccessPermission((uint32_t) &pSettings.outputChannel420.value, NOT_EDITABLE, sizeof(float32_t));
//	setAccessPermission((uint32_t) &pSettings.outputChannel420.sourceSignal, FULLY_EDITABLE, sizeof(uint16_t));
//	setAccessPermission((uint32_t) &pSettings.outputChannel420.config.coefK, PARTIALLY_EDITABLE, sizeof(float32_t));
//	setAccessPermission((uint32_t) &pSettings.outputChannel420.config.coefB, PARTIALLY_EDITABLE, sizeof(float32_t));
//
//  	for (uint16_t i = 0; i < 6; i++) {
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].averageCurrentValue, NOT_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].breakSensor, NOT_EDITABLE, sizeof(uint16_t));
//
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].warningSetPoints.low, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].warningSetPoints.high, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].EmergencySetPoints.low, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].EmergencySetPoints.high, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].onoffChannel, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].lowLimitRange, FULLY_EDITABLE, sizeof(float32_t));				//not used yet
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].highLimitRange, FULLY_EDITABLE, sizeof(float32_t));			//not used yet
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].id_break, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].id_warningLow, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].id_warningHigh, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].id_emergencyLow, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].id_emergencyHigh, FULLY_EDITABLE, sizeof(uint16_t));
//
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].config.coefK, PARTIALLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.inputChannel420[i].config.coefB, PARTIALLY_EDITABLE, sizeof(float32_t));
//
//		setAccessPermission((uint32_t) &pSettings.outputDescreteChannel[i].state, NOT_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.outputDescreteChannel[i].id, NOT_EDITABLE, sizeof(uint16_t));
//
//		setAccessPermission((uint32_t) &pSettings.outputDescreteChannel[i].mode, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.outputDescreteChannel[i].delayIn, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.outputDescreteChannel[i].delayOut, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.outputDescreteChannel[i].quit, FULLY_EDITABLE, sizeof(uint16_t));
//		setAccessPermission((uint32_t) &pSettings.outputDescreteChannel[i].test, FULLY_EDITABLE, sizeof(uint16_t));
//
//		setAccessPermission((uint32_t) &pSettings.pidData[i].processValue_pid, NOT_EDITABLE, sizeof(float32_t));
//
//		setAccessPermission((uint32_t) &pSettings.pidData[i].coef_P_pid, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.pidData[i].coef_I_pid, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.pidData[i].coef_D_pid, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.pidData[i].setPoint_pid, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.pidData[i].minValue_pid, FULLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.pidData[i].maxValue_pid, FULLY_EDITABLE, sizeof(float32_t));
//
//		setAccessPermission((uint32_t) &pSettings.pidData[i].config.coefK, PARTIALLY_EDITABLE, sizeof(float32_t));
//		setAccessPermission((uint32_t) &pSettings.pidData[i].config.coefB, PARTIALLY_EDITABLE, sizeof(float32_t));
//  }
//  initialized = 1;
}

void putAllData(){
//	settings.generalSettings = pSettings.generalSettings;
//	settings.outputChannel420 = pSettings.outputChannel420;
//	settings.quitAll = pSettings.quitAll;
//	for (uint8_t i = 0; i < 6; i++){
//		settings.inputChannel420[i] = pSettings.inputChannel420[i];
//		settings.outputDescreteChannel[i].mode = pSettings.outputDescreteChannel[i].mode;
//		settings.outputDescreteChannel[i].delayIn = pSettings.outputDescreteChannel[i].delayIn;
//		settings.outputDescreteChannel[i].delayOut = pSettings.outputDescreteChannel[i].delayOut;
//		settings.outputDescreteChannel[i].quit = pSettings.outputDescreteChannel[i].quit;
//		settings.outputDescreteChannel[i].test = pSettings.outputDescreteChannel[i].test;
//
//		settings.pidData[i].coef_P_pid = pSettings.pidData[i].coef_P_pid;
//		settings.pidData[i].coef_I_pid = pSettings.pidData[i].coef_I_pid;
//		settings.pidData[i].coef_D_pid = pSettings.pidData[i].coef_D_pid;
//		settings.pidData[i].setPoint_pid = pSettings.pidData[i].setPoint_pid;
//		settings.pidData[i].minValue_pid = pSettings.pidData[i].minValue_pid;
//		settings.pidData[i].maxValue_pid = pSettings.pidData[i].maxValue_pid;
//		settings.pidData[i].config = pSettings.pidData[i].config;
//	}
}

void updateAllData(){
//  uint16_t accessCode = pSettings.generalSettings.editSettingsRegister;
//	pSettings.generalSettings = settings.generalSettings;
//  pSettings.generalSettings.editSettingsRegister = accessCode;
//	pSettings.outputChannel420 = settings.outputChannel420;
//	pSettings.quitAll = settings.quitAll;
//	for (uint8_t i = 0; i < 6; i++){
//		pSettings.inputChannel420[i] = settings.inputChannel420[i];
//
//		pSettings.outputDescreteChannel[i].state = settings.outputDescreteChannel[i].state;
//		pSettings.outputDescreteChannel[i].mode = settings.outputDescreteChannel[i].mode;
//		pSettings.outputDescreteChannel[i].delayIn = settings.outputDescreteChannel[i].delayIn;
//		pSettings.outputDescreteChannel[i].delayOut = settings.outputDescreteChannel[i].delayOut;
//		pSettings.outputDescreteChannel[i].quit = settings.outputDescreteChannel[i].quit;
//		pSettings.outputDescreteChannel[i].test = settings.outputDescreteChannel[i].test;
//		pSettings.outputDescreteChannel[i].id = settings.outputDescreteChannel[i].id;
//
//		pSettings.pidData[i].coef_P_pid = settings.pidData[i].coef_P_pid;
//		pSettings.pidData[i].coef_I_pid = settings.pidData[i].coef_I_pid;
//		pSettings.pidData[i].coef_D_pid = settings.pidData[i].coef_D_pid;
//		pSettings.pidData[i].setPoint_pid = settings.pidData[i].setPoint_pid;
//		pSettings.pidData[i].minValue_pid = settings.pidData[i].minValue_pid;
//		pSettings.pidData[i].maxValue_pid = settings.pidData[i].maxValue_pid;
//		pSettings.pidData[i].processValue_pid = settings.pidData[i].processValue_pid;
//		pSettings.pidData[i].config = settings.pidData[i].config;
//	}
}


void checkLock(){
//  if (initialized == 0){
//    initMap();
//  }
}