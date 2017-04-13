from bitFont import BitFont
font = BitFont(
	height = 15,
	pixBytes = bytearray(b'\xfc\x0b\xfe\x05\x07\x80\x03\x00\x00\xe0\x00p\x00@\x02\xf8\x07\xfc\x03H\x00\xff\x80\x7f\x00\t\xc0\x11\xf0\x19\xc8\x08\xfe\x0fb\x02\xf3\x01q\xc0@\xf080\x0e\xc0\x01p\x00\x8e\x81\xe3A`\x008\xe0>\xf8\x11\xe4\x08\xde\x06\xc6\x01\xe0\x01\x98\xe0\x01\xf0\x00\xc0\x03\xf8\x07\x0e\x87\x01F\x00"\x001\xc0p8\xf0\x0f\xe0\x01@\x00\xa8\x00|\x00\x1c\x00\x1f\x80\n\x00\x01\x80\x00@\x00 \x00\xfe\x00\x7f\x00\x04\x00\x02\x00\x01\x00L\x00>\x00\x0f\x10\x00\x08\x00\x04\x00\x02\x00\x01\x80\x00@\x00 \x00\x00\x01\xc0\x01\xe0\x00 \x00\x10\x00\x0e\x80\x03p\x00\x1c\x80\x03\xe0\x00\x10\x00\xc0\x03\xf0\x03\x0c\x03\x03\x83\x81\x81a\x80\x1f\x80\x07 \x10\x18\x08\xfe\x07\xff\x03\x00\x01\x80\x80@`0\x18\x1c\x04\x0b\xc2\x043\x02\x0f\x01\x83@ 00\x08\x10D\x08"\x04;\x03\xf7\x001\x00\x0c\x00\x07\xc0\x020\x01\x8c\x00\xff\x83\xff\x01\x10\xe0\x13\xf0\x19\x88\x18$\x08\x12\x04\x19\x83\xf8\x008\x80\x1f\xe0\x1f\x18\x19D\x08"\x043\x03\xf3\x000 \x00\x10\x00\x08\x00\x04\x0f\xe2\x079\x80\x07\xc0\x01\x80\x18\xe0\x1e\xd8\x19D\x08"\x04;\x03\xf7\x001\x80\x01\xe0\x19\x98\x19\x84\x08B\x04\x13\x03\xff\x00?\x00B\x80s\xc09@\x08 \x008\x13\x9c\x0f\xc4\x03\x06\x80\x07`\x06\x18\x06\x06\x06\x01\x02H\x00$\x00\x12\x00\t\x80\x04@\x02 \x01\x90\x80\x00\xc1\xc0\xc00\xc0\x0c\xc0\x03\xc0\x00\x0c\x00\x07\x80\xa0A\xd8 \x06\xf0\x01p\x00\xf0\x03\xfc\x03\x03\x83\x18A\x9e`I\xe07\xe0\t\xe0\x0f\xf8\x07F\x80!\xc0\x10\xc0\x08\xc0?\xc0\x1f\xfc\x0f\xfe\x07\x11\x82\x08A\x84`g\xe0\x1e \x06\xf0\x03\xfc\x03\x03\x83\x00A\x80 @000\x0c\xfc\x0f\xfe\x07\x01\x82\x00A\x80``\xe0\x1f\xe0\x07\xfc\x0f\xfe\x07\x11\x82\x08A\x84 B\x10 \xf8\x1f\xfc\x0f"\x00\x11\x80\x08@\x04 \x00\x10\x00\xe0\x07\xf8\x07\x06\x06\x01\x82\x00A\x88`| \x1e\xf8\x1f\xfc\x0f \x00\x10\x00\x08\x00\x04\xe0\x7f\xf0?\x08\x10\x04\x08\xfe\x07\xff\x83\x00A\x80\x000\x000\x08\x10\x04\x0c\xfe\x03\xff\x80\xff\xc1\xff\x00\x06\x80\x07`\x06\x18\x06\x06\x06\x01\x82\xff\xc1\xff\x00@\x00 \x00\x10\x00\x08\x00\x04\xff\x83\xff\x81\x01\x80\x07\xc0\x030\x00\xfc\x0f\xfe\x07\xff\x83\xff\x81\x03\x80\x07\x00\x07\x00\x0e\xfc\x0f\xfe\x07\xfc\x00\xff\xc0\xc0 @\x10 \x18\x18\xf8\x07\xf8\x01\xff\x83\xffA\x04 \x02\x10\x01\x88\x00|\x00\x1c\x00\xfc\x00\xff\xc0\xc0 H\x10,\x18\x1c\xf8\x07\xf8\x05\xff\x83\xffA\x0c \x06\x10\x07\x88\x06|\x0e\x1c\x06\x0e\x81\x8fA\x84 B\x10!\x88\x10\xcc\x0f\xc4\x03\x01\x80\x00@\x00\xe0\x7f\xf0?\x08\x00\x04\x00\x02\x00\xff\x80\xff\x00\xc0\x00@\x00 \x00\x18\xfc\x07\xfe\x01\x07\x80\x1f\x00>\x00x\x00<\xc0\x07\xfc\x00\x0e\x00\xff\x83\xff\x01`\x00\x1e\x00\x0f\x00\x0c\xfc\x0f\xfe\x07\x03\x83\xc3\x013\x00\x0f\x80\x07`\x06\x1c\x0e\x06\x06\x03\x80\x03\x00\x03\x00\x7f\x80?`\x00\x1c\x00\x06\x00\x81\x83\xe0A\x98 F\x90!x\x10\x1c\x08\xff\x8f\xffG\x00"\x00\x11\x80\x10\x008\x008\x00p\x00p\x00\xe0\x00\xe0\x00@\x08@\x04 \x02\x10\xff\x8f\xff\x07\x06\x80\x01`\x000\x000\x000\x00\x00\x08\x00\x04\x00\x02\x00\x01\x80\x00@\x00 \x00\x10\x01\x80\x01\x80\x01\x80\x00\x000\x00=\xc0\x12 \t\x90\x04H\x01\xfc\x01\xfc\xe0\x7f\xf0?\x80\x08 \x08\x10\x04\x18\x03\xf8\x008\x00\x1c\x00\x1f\xc0\x18 \x08\x10\x04\x08\x02\x8c\x01D\x00\x1c\x00\x1f\xc0\x18 \x08\x10\x04\x10\x81\xff\xc1\xff\x00\x1c\x00\x1f\xc0\x1a \t\x90\x04X\x02\xb8\x01X\x00\x04\x00\x02\xf0\x1f\xfc\x0fB\x00!\x80\x03\x80\x01\x00\xae\x81\xffA\x94 J\x10%\xf8\x128\x0f\x06\xe3\x7f\xf0?\x80\x00 \x00\x10\x00\x18\x00\xf8\x01\xf8\x00@\x80 \xd8\x1f\xec\x0f\x00\x04\x00\x02\x00\x07\x80\x07\x00\x82\x00A\x80\xec\x7f\xf6\x1f\xff\x83\xff\x01\x18\x00\x1e\x80\x19@\x18\x00\x08\x00\x04\x01\x82\xff\xc1\xff\x00@\x00 \xc0\x1f\xc0\x0f\x10\x00\xf8\x03\xf8\x01\x02\x00\x7f\x00?\xc0\x1f\xe0\x0f \x00\x08\x00\x04\x00\x06\x00~\x00>\x00\x07\xc0\x070\x06\x08\x02\x04\x01\xc6\x00>\x00\x0e\xc0\xff\xe0\x7f \x02\x08\x02\x04\x01\xc6\x00>\x00\x0e\x00\x07\xc0\x070\x06\x08\x02\x04\x01D\x00\xff\x83\xffA\x00\xe0\x0f\xe0\x07\x18\x00\x04\x00\x02\x00\x03\x00\x01\x80\t\xe0\r\x90\x04H\x02$\x01\x92\x00{\x00\x19@\x00 \x00\xfc\x03\xfe\x03\x04\x01\x82\x00`\x00\x10\xc0\x07\xe0\x07\x00\x06\x00\x02\x00\x01@\x00\x7f\x80?\xc0\x00\xe0\x01\xc0\x03\x80\x03\xc0\x01x\x00\x0f\x80\x01\xc0\x0f\xe0\x0f\x00\x06\xe0\x01\xf0\x00\xc0\x00\x7f\x80\x1f@\x10`\x0c`\x03\xe0\x00p\x00l\x00c\x80 \xc0G\xe0g\x00&\x00\x12\x00\t@\x06\xff\x81\x7f@\x18 \x0e\x90\x05h\x02\x1c\x01\x86\x00\x06\xf0?|>\x02\x10\x01\x08\xff\x83\xff!\x00\x11\x80\xf8|\xf8\x1f\xc0\x00\x0c\x00\x07\x80\x00\xc0\x00\xc0\x00@\x008\x00\x0c'),
	endCols = [2, 7, 14, 21, 29, 37, 39, 44, 49, 56, 64, 67, 75, 79, 87, 95, 101, 109, 117, 125, 133, 141, 149, 157, 165, 169, 173, 179, 187, 193, 200, 208, 216, 224, 232, 240, 247, 255, 263, 271, 277, 283, 291, 298, 306, 314, 322, 330, 338, 346, 354, 362, 370, 378, 386, 394, 402, 409, 414, 422, 427, 433, 441, 445, 453, 461, 469, 477, 485, 493, 501, 509, 515, 522, 529, 535, 543, 551, 559, 567, 575, 583, 591, 599, 607, 615, 623, 631, 639, 645, 650, 652, 657, 665]
)