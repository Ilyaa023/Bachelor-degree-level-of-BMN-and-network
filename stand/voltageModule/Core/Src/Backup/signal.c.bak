#include "signal.h"

Signal_t signal = {0};
uint16_t counter = 0;
uint8_t signalBuffer[512] = {0};

void CalculateMemoryBuffer(){

}

void CalculateBuffer(){
	switch (signal.form){

	case TRIANGLE:
		for (uint16_t i = 0; i < 512; i++){
			uint16_t tmp = i % 256 * signal.amplitude / 256 + signal.offset;
			if (tmp > 255)
				tmp = 255;
			signalBuffer[i] = tmp;
		}
		break;

	case SQUARE:
		for (uint16_t i = 0; i < 512; i++)
			if (i>>7 & 1 )
				signalBuffer[i] = 0 + signal.offset;
			else {
				uint16_t tmp;
				tmp = signal.amplitude + signal.offset;
				if (tmp > 255)
					tmp = 255;
				signalBuffer[i] = tmp;
			}
		break;

	case SINE:
		for (uint16_t i = 0; i < 512; i++){
			uint16_t tmp;
			if (i < 256)
				tmp = (256*i - i*i + 16384) * signal.amplitude / 32768 + signal.offset;
			else
				tmp = (i*i - 768*i + 147456) * signal.amplitude / 32768 + signal.offset;
			if (tmp > 256)
				tmp = 255;
			signalBuffer[i] = tmp;
		}
		break;

	case CONST:
		for (uint16_t i = 0; i < 512; i++)
			signalBuffer[i] = signal.offset;

	default:
		CalculateMemoryBuffer();
		break;
	}
	signal.out = INITIAL_OUT;
	counter = 0;
}

void SignalInit(){
	signal.amplitude = 128;
	signal.offset = 75;
	signal.frequency = 500;
	signal.form = SINE;
	CalculateBuffer();
}

uint8_t GetNext(){
	if (counter > 511)
		counter = 0;
	return signal.out = signalBuffer[counter++] + INITIAL_OUT;
}

uint16_t* GetSignal(){
	return (uint16_t*) &signal.out;
}

void SetForm(SignalForm_t form){
	signal.form = form;
	CalculateBuffer();
}

void SetAmplitude(uint8_t ampl){
	signal.amplitude = ampl;
	CalculateBuffer();
}
void SetOffset(uint8_t offset){
	signal.offset = offset;
	CalculateBuffer();
}

void SetFrequency(uint16_t freq){
	if (signal.form == CONST)
		freq = 1;
	signal.frequency = freq;
	if (freq > 250){
		signal._prescaler = 0;
		signal._arr = 480000000 / 256 / freq;
	}
	else if (freq > 1250) {
		signal._prescaler = 1;
		signal._arr = 240000000 / 256 / freq;
	}
	else if (freq > 720) {
		signal._prescaler = 2;
		signal._arr = 120000000 / 256 / freq;
	}
	else if (freq > 360) {
		signal._prescaler = 3;
		signal._arr = 60000000 / 256 / freq;
	}
	else if (freq > 180) {
		signal._prescaler = 4;
		signal._arr = 30000000 / 256 / freq;
	}
	else if (freq > 100) {
		signal._prescaler = 5;
		signal._arr = 15000000 / 256 / freq;
	}
	else
		signal._prescaler = 6;
		signal._arr = 7500000 / 256 / freq;

	if (signal.form == SINE || signal.form == USER)
		freq /= 2;
}
