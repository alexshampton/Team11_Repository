# Jabcode Install
```
sudo apt-get update
sudo apt-get install build-essential cmake libpng-dev zlib1g-dev git
sudo apt-get install libtiff-dev
git clone https://github.com/jabcode/jabcode.git
```
# Steps
Step 1: Build the JAB Code core library by running make command in src/jabcode.

Step 2: Change makefile in src/jabcodeWriter:
```
PREFIX 	=
CC 	= $(PREFIX)gcc
CFLAGS	 = -O2 -std=c11

TARGET = bin/jabcodeWriter

OBJECTS = $(patsubst %.c,%.o,$(wildcard *.c))

$(TARGET): $(OBJECTS)
	$(CC) $^ -L../jabcode/build -ljabcode -L../jabcode -ltiff -lpng16 -lz -lm $(CFLAGS) -o $@

$(OBJECTS): %.o: %.c
	$(CC) -c -I. -I../jabcode -I../jabcode/include $(CFLAGS) $< -o $@

clean:
	rm -f $(TARGET) $(OBJECTS)
```
Step 3: Build the JAB Code writer by running make command in src/jabcodeWriter.

Step 4: Change makefile in src/jabcodeReader:
```
PREFIX 	=
CC 	= $(PREFIX)gcc
CFLAGS	 = -O2 -std=c11

TARGET = bin/jabcodeReader

OBJECTS = $(patsubst %.c,%.o,$(wildcard *.c))

$(TARGET): $(OBJECTS)
	$(CC) $^ -L../jabcode/build -ljabcode -L../jabcode -ltiff -lpng16 -lz -lm  $(CFLAGS) -o $@

$(OBJECTS): %.o: %.c
	$(CC) -c -I. -I../jabcode -I../jabcode/include $(CFLAGS) $< -o $@

clean:
	rm -f $(TARGET) $(OBJECTS)
```
Step 5: Build the JAB Code reader by running make command in src/jabcodeReader.

The built library can be found in src/jabcode/build. The built reader and writer applications can be found in src/jabcodeReader/bin and src/jabcodeWriter/bin.
