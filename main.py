from CodeLoader import load_code

INSTRUCTIONS = {
	"MOV" : 0b01000000,
	"MVI" : 0b00000001,
	"ADD" : 0b00000010,
	"SUB" : 0b00000011,
	"INC" : 0b00000100,
	"NOP" : 0b00000000,
	"HLT" : 0b11111111,
	"JMP" : 0b00000101,
}

REGS = {
	"$B" : 0b000,
	"$C" : 0b001,
	"$D" : 0b010,
	"$E" : 0b011,
	"$H" : 0b100,
	"$L" : 0b101,
	"$M" : 0b110,
	"$A" : 0b111,
}

out = []

code, outfile = load_code()

code = code.upper().strip().replace(" ", "")
code = code.split("\n")


for i in range(len(code)):
	add_to_out = [0]
	line = code[i]
	ins = line[:3]

	reg_num = 1

	if ins not in INSTRUCTIONS:
		print(f"On line {i}: {line} unknown instruction {ins}")

	ins_code = INSTRUCTIONS[ins]
	args = line[3:].split(",")
	
	for arg in args:
		if arg[0] == '$':
			ins_code |= (REGS[arg] << (reg_num*3))
	print(bin(ins_code))
