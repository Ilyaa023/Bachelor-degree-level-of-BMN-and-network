#include "main.h"
#include "utils.h"

#define PAGE 12

typedef __packed struct {
  Signal_t signal;
  uint8_t SSD_stopFlag;
  uint32_t UART_speed;
  uint8_t UART_address;
  uint8_t userBuffer[512];
} Settings_t;

uint8_t write_flash(uint32_t start_addr, uint32_t page, Settings_t* data);
uint8_t write_to_default_page(Settings_t* data);
uint8_t read_flash(uint32_t start_addr, Settings_t* data);
uint8_t read_from_default_page(Settings_t* data);