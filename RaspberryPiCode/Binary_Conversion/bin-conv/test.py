fr = open("a.jpeg", "rb")
fw = open("test.bin", "ab")
fw.write(fr.read())