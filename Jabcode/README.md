# Jabcode Install
```
sudo apt-get update
sudo apt-get install build-essential cmake libpng-dev zlib1g-dev git
git clone https://github.com/jabcode/jabcode.git
```
# Steps
Step 1: Build the JAB Code core library by running make command in src/jabcode.

Step 2: Change make file to:
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

Step 4: Build the JAB Code reader by running make command in src/jabcodeReader.

The built library can be found in src/jabcode/build. The built reader and writer applications can be found in src/jabcodeReader/bin and src/jabcodeWriter/bin.
