ean function : deletes all temporary files
clean :
	rm -f *~
	rm -f *#
	rm -f *.o
	rm -f core.*
	rm -f vgcore.*
	rm -f *.gch
	rm -f Amazing*.log
	@echo "Unnecessary Files were deleted from the folder."
	
