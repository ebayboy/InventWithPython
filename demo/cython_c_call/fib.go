package main

import "time"
import "fmt"

func fibonacci(a int) int {
	if a == 0 || a == 1 {
		return 1

	}
	return fibonacci(a-1) + fibonacci(a-2)
}

func main() {
	start := time.Now().UnixNano()
	fmt.Println("ret:", fibonacci(30))
	end := time.Now().UnixNano()
	fmt.Println("cost:", end-start)
}
