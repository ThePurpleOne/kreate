CC       := gcc
CFLAGS := -Wall -Wextra -g -fsanitize=address -fsanitize=leak

BIN     	 := bin
SRC     	 := src
INCLUDE 	 := include
LIBRARIES    := -lm
EXECUTABLE1  := main

# ADD ALL THE SOURCES FOR EXECUTABLE1
SOURCES1 += $(SRC)/jrandom

.PHONY: all run clean # Specify these are not files but internal terms

all: $(BIN)/$(EXECUTABLE1)

run: clean all
	clear
	@echo "########## EXECUTE FIRST PROGRAM ##########"
	./$(BIN)/$(EXECUTABLE1)

# # $^ -> dep
# # $@ -> target
# # $< -> premiere dep
# # Compiles directly the c files
# # Not optimal but succint and simple

# COMPILE FIRST EXECUTABLE
$(BIN)/$(EXECUTABLE1): $(SRC)/$(EXECUTABLE1).c $(SOURCES)
	@echo "########## COMPILING FIRST EXECUTABLE ##########"
	$(CC) $(CFLAGS) -I $(INCLUDE) $^ -o $@ $(LIBRARIES)

clean:
	@echo "########## CLEANING ##########"\n	-rm $(BIN)/*

