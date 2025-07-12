//#include "main.h"
//#include "arm_math.h"
#include "math.h"
#include <stdint.h>
#include "stm32f0xx_hal.h"
#include "stm32f0xx_hal_flash.h"
#include "flash_manager.h"
//#include "cmsis_os.h"
//#include "utils.h"


uint8_t write_flash(uint32_t start_addr, uint32_t page, Settings_t* data)
{
	volatile uint8_t status = 0;
	uint32_t PAGEError = 0;

	FLASH_EraseInitTypeDef EraseInitStruct;

	EraseInitStruct.TypeErase = FLASH_TYPEERASE_PAGES;
//	EraseInitStruct.Banks = 1;
	EraseInitStruct.PageAddress = page;
	EraseInitStruct.NbPages = 1;
//  __HAL_FLASH_CLEAR_FLAG(FLASH_FLAG_ALL_ERRORS);

	__HAL_FLASH_CLEAR_FLAG(FLASH_FLAG_PGERR);
	status = HAL_FLASH_Unlock();
//	HAL_Delay(5);
  while (status != 0);

	status = HAL_FLASHEx_Erase(&EraseInitStruct,&PAGEError);

	if (status == 0)
	{
    uint64_t crc = (uint64_t) crc16((uint8_t*) data, sizeof(Settings_t));
    HAL_FLASH_Program(FLASH_TYPEPROGRAM_DOUBLEWORD, start_addr, crc);
    start_addr += 8;
    SET_BIT(FLASH->CR, FLASH_CR_PG);
    *(__IO Settings_t*) start_addr = *data;
    CLEAR_BIT(FLASH->CR, FLASH_CR_PG);
  }
	HAL_FLASH_Lock();

	return status;

}

uint8_t write_to_default_page(Settings_t* data) {
  uint32_t start_addr = 0x8000000 + (PAGE * 1024);
  return write_flash(start_addr, PAGE, data);
}

uint8_t read_flash(uint32_t start_addr, Settings_t* data)
{
  uint16_t *crc = (uint16_t*) (start_addr);
  uint16_t crcData = *crc;
  start_addr += 8;
  Settings_t *tse = (Settings_t*) start_addr;
  *data = *tse;
  uint16_t crcA = crc16((uint8_t*) data, sizeof(Settings_t));
  if (crcData != crcA)
    return 1;
	return 0;
}

uint8_t read_from_default_page(Settings_t* data){
  uint32_t start_addr = 0x8000000 + (PAGE * 2048);
  return read_flash(start_addr, data);
}