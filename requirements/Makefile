objects = $(wildcard *.in)
outputs = $(objects:.in=.txt)
sync-targets = $(objects:%.in=sync-%)

.PHONY: all check clean $(sync-targets)

all: $(outputs)

%.txt: %.in
	@pip-compile -v --output-file $@ $<

dev.txt: main.txt

check:
	@which pip-compile > /dev/null

clean: check
	-@rm *.txt

$(sync-targets): sync-%: %.txt
	@pip-sync $<
