#include "stm32f0xx_hal.h"

#define INITIAL_OUT 0b100000000

typedef enum
{
  SINE,
	TRIANGLE,
	CONST,
	SQUARE,
	USER
} SignalForm_t;

typedef __packed struct {
	uint8_t amplitude;
	uint8_t offset;
	SignalForm_t form;
	uint16_t frequency;

	uint16_t out;

	uint16_t _prescaler;
	uint16_t _arr;
} Signal_t;

void SignalInit();
uint8_t GetNext();
uint16_t* GetSignal();
void SetForm(SignalForm_t form);
void SetFrequency(uint16_t freq);
void SetAmplitude(uint8_t ampl);
void SetOffset(uint8_t offset);
