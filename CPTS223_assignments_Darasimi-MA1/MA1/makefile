prog: main.o testQueue.o queue.o
	g++ -g main.o testQueue.o queue.o -o MA1_exe

main.o: main.cpp testQueue.h testQueue.cpp queue.h queue.cpp
	g++ -c -g -std=c++11 -Wall main.cpp 

testQueue.o: testQueue.h testQueue.cpp
	g++ -c -g -std=c++11 -Wall testQueue.cpp

queue.o: queue.h queue.cpp
	g++ -c -g -std=c++11 -Wall queue.cpp

clean: 
	-rm *.o

run:
	@./MA1_exe