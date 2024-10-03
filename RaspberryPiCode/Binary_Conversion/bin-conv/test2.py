fr = open("test.bin", "rb")
fw = open("b.jpeg", "ab")
fw.write(fr.read())